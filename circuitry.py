# File: circuitry.py
#!/usr/bin/env python3
"""
Circuitry: moduł zawierający GUI edytora i symulacji układów, wraz z obsługą błędów i warningów.
Zawiera:
- FriendlyErrorListener (ANTLR ErrorListener)
- process_circuit_content
- SymbolCollectorVisitor
- TextHandler (logowanie do Tkinter)
- CircuitEditorGUI
- main()

Aby użyć: `python circuitry.py`
Wymaga:
- tkinter
- antlr4 Runtime i wygenerowane pliki CircuitryLexer, CircuitryParser, CircuitryParserVisitor
- moduły circuitry.builder, circuitry.utils, circuitry.mna
"""
import threading
import sys
import logging
import io
import re
import tkinter as tk
from tkinter import scrolledtext, messagebox
from antlr4 import InputStream, CommonTokenStream

# Importy z Twojego modułu Circuitry:
# Zakładamy, że pliki wygenerowane przez ANTLR są dostępne w module circuitry.gen
try:
    from circuitry.builder import CircuitBuilderVisitor
    from circuitry.utils import to_polar_str
    from circuitry.gen.CircuitryLexer import CircuitryLexer
    from circuitry.gen.CircuitryParser import CircuitryParser
    from circuitry.gen.CircuitryParserVisitor import CircuitryParserVisitor
except ImportError:
    # Jeśli moduł inaczej zorganizowany, użytkownik powinien dostosować importy
    raise
import math
from antlr4.error.ErrorListener import ErrorListener

# ---------- FriendlyErrorListener ----------
class FriendlyErrorListener(ErrorListener):
    def __init__(self, input_stream: InputStream, print_errors: bool = False, suppress_warnings: bool = True):
        super().__init__()
        data = input_stream.getText(0, input_stream.size)
        self.lines = data.splitlines()
        self.had_error = False
        self.warnings = []
        self.errors = []  # zbieramy błędy składniowe i semantyczne
        self.print_errors = print_errors
        self.suppress_warnings = suppress_warnings

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.had_error = True
        error_info = {
            'type': 'syntax',
            'line': line,
            'column': column,
            'msg': msg,
        }
        self.errors.append(error_info)
        if self.print_errors:
            RED    = "\033[31m"
            BOLD   = "\033[1m"
            YELLOW = "\033[33m"
            RESET  = "\033[0m"
            ICON   = "❌"
            header = f"{RED}{BOLD}{ICON} Syntax error at line {line}, column {column}:{RESET}"
            details = f"{RED}{msg}{RESET}"
            src_line = ""
            if 1 <= line <= len(self.lines):
                src_line = self.lines[line - 1].replace("\t", "    ")
            pointer = ""
            if src_line:
                pointer = " " * (column + 4) + f"{YELLOW}^{RESET}"
            print(header)
            print(f"    {details}")
            if src_line:
                print(f"    {src_line}")
                print(pointer)
            print()

    def warning(self, line: int, column: int, msg: str):
        # Zbieramy warningi, ale nie drukujemy, jeśli suppress_warnings=True
        self.warnings.append((line, column, msg))
        if not self.suppress_warnings:
            YELLOW = "\033[33m"
            BOLD   = "\033[1m"
            RESET  = "\033[0m"
            ICON   = "⚠️"
            header = f"{YELLOW}{BOLD}{ICON} Warning at line {line}, column {column}:{RESET}"
            details = f"{YELLOW}{msg}{RESET}"
            print(header)
            print(f"    {details}\n")

    def semanticError(self, line: int, column: int, msg: str):
        self.had_error = True
        error_info = {
            'type': 'semantic',
            'line': line,
            'column': column,
            'msg': msg,
        }
        self.errors.append(error_info)
        if self.print_errors:
            RED    = "\033[31m"
            BOLD   = "\033[1m"
            RESET  = "\033[0m"
            ICON   = "❌"
            header = f"{RED}{BOLD}{ICON} Semantic error at line {line}, column {column}:{RESET}"
            details = f"{RED}{msg}{RESET}"
            print(header)
            print(f"    {details}\n")

    def reportAllErrors(self) -> bool:
        if self.had_error:
            if self.print_errors:
                print("Kompilacja przerwana z powodu błędów składniowych lub semantycznych.")
            return True
        return False

    def getErrors(self):
        return self.errors

# ---------- process_circuit_content ----------
def process_circuit_content(content: str):
    """
    Przetwarza tekst z edytora jako definicję układu.
    Zwraca tuple: (success: bool, warnings: list of (line, col, msg), errors: list, raw_output: str).
    """
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    str_io = io.StringIO()
    sys.stdout = str_io
    sys.stderr = str_io

    listener = None
    success = True
    try:
        if not content.strip():
            print("Error: Definicja układu jest pusta.")
            success = False
            return success, [], [], str_io.getvalue()

        # Parsowanie ANTLR z treści
        input_stream = InputStream(content)
        # suppress_warnings=True, print_errors=False
        listener = FriendlyErrorListener(input_stream, print_errors=False, suppress_warnings=True)

        lexer = CircuitryLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(listener)

        stream = CommonTokenStream(lexer)
        parser = CircuitryParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)

        tree = parser.program()

        # Sprawdź błędy składni lub semantyczne
        if listener.reportAllErrors():
            success = False
            warnings = getattr(listener, 'warnings', [])
            errors = listener.getErrors()
            return success, warnings, errors, str_io.getvalue()

        # Wizyta semantyczna
        visitor = CircuitBuilderVisitor(error_listener=listener)
        visitor.visit(tree)

        # Zbierz semantyczne warningi i błędy
        warnings = getattr(listener, 'warnings', [])
        errors = listener.getErrors()
        if errors:
            success = False
            return success, warnings, errors, str_io.getvalue()

        # Symulacje
        simulations = visitor.simulations
        if not simulations:
            print("Brak definicji symulacji w tekście.")
        for sim in simulations:
            sim_type = sim.get("type", "dc").lower()
            sim_params = sim.get("params", {})
            if sim_type == "dc":
                from circuitry.mna import dc_solve, element_voltage, element_current
                ground, nodes, vs_list, solution, node_map, n = dc_solve(
                    components=visitor.components,
                    aliases=visitor.aliases,
                    tol=1e-8,
                    max_iter=50,
                )
                omega = None
            elif sim_type == "ac":
                from circuitry.mna import ac_solve, element_voltage, element_current
                frequency = sim_params[0]
                ground, nodes, vs_list, solution, node_map, n = ac_solve(
                    components=visitor.components,
                    aliases=visitor.aliases,
                    frequency=frequency,
                    tol=1e-8,
                    max_iter=50,
                )
                omega = 2 * math.pi * frequency
            else:
                print(f"Error: Nieobsługiwany typ symulacji '{sim_type}'.")
                success = False
                continue

            print(f"\n=== Symulacja {sim_type.upper()} ===")
            print(f"Ground: {ground} = 0 V")
            print("Node voltages:")
            for node, v in zip(nodes, solution[:len(nodes)]):
                if sim_type == "ac":
                    print(f"  {node}: {to_polar_str(v)} V")
                else:
                    print(f"  {node}: {v:.6f} V")

            print("Voltage source currents:")
            for vs, i in zip(vs_list, solution[len(nodes):]):
                if sim_type == "ac":
                    print(f"  {vs.name}: {to_polar_str(i)} A")
                else:
                    print(f"  {vs.name}: {i:.6f} A")

            print("Element voltages i prądy:")
            for comp in visitor.components:
                v = element_voltage(comp, node_map, ground, solution, visitor.aliases)
                i = element_current(
                    comp, node_map, ground, solution, vs_list, n,
                    visitor.aliases, omega=omega
                )
                if sim_type == "ac":
                    v_str = to_polar_str(v) if isinstance(v, complex) else f"{v:.6f} V"
                    i_str = to_polar_str(i) if isinstance(i, complex) else (
                        f"{i:.6f} A" if i is not None else "N/A")
                else:
                    v_str = f"{v:.6f} V"
                    i_str = f"{i:.6f} A" if i is not None else "N/A"
                print(f"  {comp.name}: Voltage = {v_str}, Current = {i_str}")

        return success, warnings, errors, str_io.getvalue()

    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}", file=sys.stderr)
        success = False
        warnings = getattr(listener, 'warnings', []) if listener else []
        errors = listener.getErrors() if listener else []
        return success, warnings, errors, str_io.getvalue()
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

# ---------- SymbolCollectorVisitor ----------
class SymbolCollectorVisitor(CircuitryParserVisitor):
    """Visitor zbierający nazwy zmiennych, aliasów, komponentów, funkcji, subcircuitów."""
    def __init__(self):
        super().__init__()
        self.symbols = set()

    def visitLetStatement(self, ctx):
        # letStatement: LET letAssignment (COMMA letAssignment)* SEMICOLON
        for laCtx in ctx.letAssignment():
            id_term = laCtx.ID()
            if id_term:
                name = id_term.getText()
                self.symbols.add(name)
        return self.visitChildren(ctx)

    def visitAliasStatement(self, ctx):
        for aaCtx in ctx.aliasAssignment():
            id0 = aaCtx.ID(0)
            if id0:
                self.symbols.add(id0.getText())
        return self.visitChildren(ctx)

    def visitComponentStatement(self, ctx):
        ids = ctx.ID()
        if len(ids) >= 2:
            inst_name = ids[1].getText()
            self.symbols.add(inst_name)
        return self.visitChildren(ctx)

    def visitFunctionDefinition(self, ctx):
        id_term = ctx.ID()
        if id_term:
            self.symbols.add(id_term.getText())
        return self.visitChildren(ctx)

    def visitSubcircuitDefinition(self, ctx):
        id_term = ctx.ID()
        if id_term:
            self.symbols.add(id_term.getText())
        return self.visitChildren(ctx)

# ---------- TextHandler ----------
class TextHandler(logging.Handler):
    """Handler logujący do tkinter.Text lub scrolledtext."""
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget
    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text_widget.insert(tk.END, msg + '\n')
            self.text_widget.see(tk.END)
        try:
            self.text_widget.after(0, append)
        except RuntimeError:
            pass

# ---------- CircuitEditorGUI ----------
class CircuitEditorGUI:
    def __init__(self, root):
        self.root = root
        root.title("Circuitry Editor i Symulacja z autocomplete")
        self.theme = 'dark'
        self.running = False

        # Menu z wyborem motywu
        menubar = tk.Menu(root)
        theme_menu = tk.Menu(menubar, tearoff=0)
        theme_menu.add_command(label="Light", command=lambda: self.set_theme('light'))
        theme_menu.add_command(label="Dark", command=lambda: self.set_theme('dark'))
        menubar.add_cascade(label="Theme", menu=theme_menu)
        root.config(menu=menubar)

        # Główne panele
        paned = tk.PanedWindow(root, orient=tk.VERTICAL)
        paned.pack(fill=tk.BOTH, expand=True)

        # --- Edytor z numeracją linii ---
        frame_editor = tk.Frame(paned)
        lbl = tk.Label(frame_editor, text="Edytor definicji układu (.cty):")
        lbl.pack(anchor=tk.W, padx=5, pady=(5,0))

        editor_frame = tk.Frame(frame_editor)
        editor_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.line_numbers = tk.Text(
            editor_frame, width=4, padx=3, takefocus=0, border=0,
            state='disabled'
        )
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        self.editor = tk.Text(editor_frame, wrap=tk.WORD, undo=True)
        self.editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(editor_frame, orient=tk.VERTICAL, command=self._on_scroll)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.editor.configure(yscrollcommand=self._on_yscroll)
        self.line_numbers.configure(yscrollcommand=self._on_yscroll)

        paned.add(frame_editor, stretch='always')

        # --- Pole na logi/wyniki ---
        frame_output = tk.Frame(paned)
        lbl2 = tk.Label(frame_output, text="Logi / Wyniki:")
        lbl2.pack(anchor=tk.W, padx=5, pady=(5,0))
        self.output = scrolledtext.ScrolledText(frame_output, wrap=tk.WORD, height=10, state=tk.NORMAL)
        self.output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        bold_font = ('TkDefaultFont', 10, 'bold')
        self.output.tag_configure('bold', font=bold_font)
        paned.add(frame_output, stretch='always')

        # --- Dolny pasek przycisków ---
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(fill=tk.X, padx=5, pady=5)
        btn_run = tk.Button(frame_buttons, text="Uruchom symulację", command=self.run_content)
        btn_run.pack(side=tk.LEFT)
        btn_clear_editor = tk.Button(frame_buttons, text="Wyczyść edytor", command=self._clear_editor)
        btn_clear_editor.pack(side=tk.LEFT, padx=5)
        btn_clear_output = tk.Button(frame_buttons, text="Wyczyść logi", command=lambda: self.output.delete(1.0, tk.END))
        btn_clear_output.pack(side=tk.LEFT, padx=5)

        # Handler logowania
        self.text_handler = TextHandler(self.output)
        formatter = logging.Formatter('%(message)s')
        self.text_handler.setFormatter(formatter)

        # Statyczne słowa kluczowe dla autocomplete
        self.static_keywords = [
            'alias','let','fn','return','series','parallel','reversed','subcircuit',
            'import','if','else','for','while','do','break','continue',
            'switch','case','default','true','false','transient','ac','dc',
            'measure','pos'
        ]

        # Syntax highlighting patterns
        multiline_comment_pattern = r'/\*[\s\S]*?\*/'
        line_comment_pattern = r'//.*'
        string_pattern = r'"([^"\\]|\\.)*"'
        kw_pattern = r'\b(?:' + '|'.join(re.escape(kw) for kw in self.static_keywords) + r')\b'
        float_pattern = (
            r'\b[+-]?'
            r'(?:\d[\d_]*)'
            r'(?:\.\d[\d_]*)?'
            r'(?:[eE][+-]?\d+)?'
            r'(?:[fpnu\u03BCmkKMGTP])?'
            r'\b'
        )
        operator_pattern = r'(\b&&\b|\|\||==|!=|<=|>=|\+\+|--|\+=|-=|\*=|/=|%=|\^=|->|[+\-*/%^!:<>=])'
        self.syntax_patterns = [
            (re.compile(string_pattern), 'string'),
            (re.compile(kw_pattern), 'keyword'),
            (re.compile(float_pattern), 'number'),
            (re.compile(operator_pattern), 'operator'),
            (re.compile(multiline_comment_pattern), 'comment'),
            (re.compile(line_comment_pattern), 'comment'),
        ]
        self.editor.tag_configure('comment', foreground='#6a9955')
        self.editor.tag_configure('string', foreground='#ce9178')
        self.editor.tag_configure('keyword', foreground='#569cd6')
        self.editor.tag_configure('number', foreground='#b5cea8')
        self.editor.tag_configure('operator', foreground='#d4d4d4')

        # Bindowania
        self.editor.bind('<KeyRelease>', self._on_key_release)
        self.editor.bind('<<Modified>>', self._on_modified)
        self.editor.bind('<MouseWheel>', self._on_scroll_event)
        self.editor.bind('<Button-4>', self._on_scroll_event)
        self.editor.bind('<Button-5>', self._on_scroll_event)
        self.editor.bind('<Configure>', lambda e: self._update_line_numbers())
        self.editor.bind('<Control-space>', self.show_autocomplete)

        # Inicjalne ustawienia
        self.apply_theme()
        self._update_line_numbers()
        self.highlight_syntax()

    def set_theme(self, theme_name):
        if theme_name not in ('light', 'dark'):
            return
        self.theme = theme_name
        self.apply_theme()
        self.highlight_syntax()

    def apply_theme(self):
        if self.theme == 'dark':
            editor_bg = '#1e1e1e'; editor_fg = '#d4d4d4'
            gutter_bg = '#2b2b2b'; gutter_fg = '#858585'
            output_bg = '#252526'; output_fg = '#e5e5e5'
            select_bg = '#264f78'; insert_color = '#ffffff'
            self.editor.tag_configure('comment', foreground='#6a9955')
            self.editor.tag_configure('string', foreground='#ce9178')
            self.editor.tag_configure('keyword', foreground='#569cd6')
            self.editor.tag_configure('number', foreground='#b5cea8')
            self.editor.tag_configure('operator', foreground='#d4d4d4')
        else:
            editor_bg = '#ffffff'; editor_fg = '#000000'
            gutter_bg = '#f0f0f0'; gutter_fg = '#555555'
            output_bg = '#ffffff'; output_fg = '#000000'
            select_bg = '#cce8ff'; insert_color = '#000000'
            self.editor.tag_configure('comment', foreground='#008000')
            self.editor.tag_configure('string', foreground='#a31515')
            self.editor.tag_configure('keyword', foreground='#0000ff')
            self.editor.tag_configure('number', foreground='#098658')
            self.editor.tag_configure('operator', foreground='#333333')
        self.editor.config(bg=editor_bg, fg=editor_fg, insertbackground=insert_color, selectbackground=select_bg)
        self.line_numbers.config(bg=gutter_bg, fg=gutter_fg)
        self.output.config(bg=output_bg, fg=output_fg, insertbackground=insert_color, selectbackground=select_bg)
        try:
            bg_root = editor_bg if self.theme=='dark' else '#f0f0f0'
            self.root.config(bg=bg_root)
        except Exception:
            pass

    def _clear_editor(self):
        self.editor.delete(1.0, tk.END)
        self._update_line_numbers()

    def _on_scroll(self, *args):
        self.editor.yview(*args)
        self.line_numbers.yview(*args)

    def _on_yscroll(self, first, last):
        try:
            self.scrollbar.set(first, last)
        except Exception:
            pass
        self.line_numbers.yview_moveto(first)

    def _on_scroll_event(self, event):
        self._update_line_numbers()
        return

    def _on_modified(self, event=None):
        if self.editor.edit_modified():
            self._update_line_numbers()
            self.editor.edit_modified(False)

    def _on_key_release(self, event=None):
        if event and event.keysym in ('Up', 'Down', 'Left', 'Right', 'Return', 'Escape'):
            self._hide_popup()
        else:
            self.editor.after_idle(self.highlight_syntax)
        self._update_line_numbers()

    def highlight_syntax(self):
        text = self.editor.get('1.0', 'end-1c')
        for _, tag in self.syntax_patterns:
            self.editor.tag_remove(tag, '1.0', tk.END)
        # Najpierw nie-komentarze
        for pattern, tag in self.syntax_patterns:
            if tag == 'comment': continue
            for m in pattern.finditer(text):
                start = f"1.0 + {m.start()}c"
                end = f"1.0 + {m.end()}c"
                try: self.editor.tag_add(tag, start, end)
                except tk.TclError: pass
        # Potem komentarze
        for pattern, tag in self.syntax_patterns:
            if tag != 'comment': continue
            for m in pattern.finditer(text):
                start = f"1.0 + {m.start()}c"
                end = f"1.0 + {m.end()}c"
                try: self.editor.tag_add(tag, start, end)
                except tk.TclError: pass
        try: self.editor.tag_raise('comment')
        except Exception: pass

    def _update_line_numbers(self):
        line_count = int(self.editor.index('end-1c').split('.')[0])
        lines = "\n".join(str(i) for i in range(1, line_count+1))
        self.line_numbers.config(state='normal')
        self.line_numbers.delete(1.0, tk.END)
        self.line_numbers.insert(1.0, lines + '\n')
        self.line_numbers.config(state='disabled')
        try:
            first, _ = self.editor.yview()
            self.line_numbers.yview_moveto(first)
        except Exception:
            pass

    def run_content(self):
        if self.running:
            messagebox.showinfo("Info", "Analiza w toku. Proszę czekać.")
            return
        content = self.editor.get(1.0, tk.END)
        self.output.delete(1.0, tk.END)
        thread = threading.Thread(target=self._run_thread, args=(content,))
        thread.daemon = True
        self.running = True
        thread.start()

    def _run_thread(self, content):
        success, warnings, errors, raw_output = process_circuit_content(content)
        self.root.after(0, lambda: self.display_result(success, warnings, errors, raw_output))

    def display_result(self, success: bool, warnings: list, errors: list, raw_output: str):
        # Nie wyświetlamy warningów
        if errors:
            self.output.insert(tk.END, "❌ Wystąpiły błędy w definicji. Analiza przerwana.\n")
        else:
            lines = raw_output.splitlines()
            filtered = []
            i = 0
            while i < len(lines):
                line = lines[i]
                if 'Warning at line' in line:
                    i += 1
                    while i < len(lines) and (lines[i].startswith(' ') or lines[i].strip()=='' or '\x1b' in lines[i]):
                        i += 1
                else:
                    filtered.append(line)
                    i += 1
            for l in filtered:
                self.output.insert(tk.END, l + "\n")
        all_text = self.output.get(1.0, tk.END).splitlines()
        for idx in range(len(all_text)-1, -1, -1):
            if all_text[idx].strip():
                line_no = idx + 1
                start = f"{line_no}.0"
                end = f"{line_no}.end"
                self.output.tag_add('bold', start, end)
                break
        self.output.see(tk.END)
        if success and not errors:
            messagebox.showinfo("Gotowe", "Analiza zakończona pomyślnie.")
        else:
            messagebox.showwarning("Zakończono", "Analiza zakończona z błędami. Sprawdź logi.")
        self.running = False

    def collect_symbols(self):
        content = self.editor.get('1.0', tk.END)
        symbols = set()
        try:
            input_stream = InputStream(content)
            listener = FriendlyErrorListener(input_stream)
            lexer = CircuitryLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(listener)
            stream = CommonTokenStream(lexer)
            parser = CircuitryParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(listener)
            tree = parser.program()
            collector = SymbolCollectorVisitor()
            collector.visit(tree)
            symbols = collector.symbols
        except Exception:
            pass
        return symbols

    def show_autocomplete(self, event=None):
        idx = self.editor.index(tk.INSERT)
        line_no, col = idx.split('.')
        line_start = f"{line_no}.0"
        text_before = self.editor.get(line_start, idx)
        m = re.search(r'([A-Za-z_][A-Za-z0-9_]*)$', text_before)
        if m:
            prefix = m.group(1)
            start_col = int(col) - len(prefix)
            start_index = f"{line_no}.{start_col}"
        else:
            prefix = ''
            start_index = idx
        suggestions = []
        for kw in self.static_keywords:
            if prefix == '' or kw.startswith(prefix): suggestions.append(kw)
        symbols = self.collect_symbols()
        for s in symbols:
            if prefix == '' or s.startswith(prefix): suggestions.append(s)
        suggestions = sorted(set(suggestions), key=lambda x: x.lower())
        if not suggestions: return "break"
        self._show_popup(suggestions, start_index, prefix)
        return "break"

    def _show_popup(self, suggestions, start_index, prefix):
        if hasattr(self, 'autocomplete_popup') and self.autocomplete_popup:
            try: self.autocomplete_popup.destroy()
            except: pass
        try:
            bbox = self.editor.bbox(tk.INSERT)
            if bbox:
                x, y, width, height = bbox
                abs_x = self.editor.winfo_rootx() + x
                abs_y = self.editor.winfo_rooty() + y + height
            else:
                abs_x = self.editor.winfo_rootx()
                abs_y = self.editor.winfo_rooty()
        except Exception:
            abs_x = self.editor.winfo_rootx()
            abs_y = self.editor.winfo_rooty()
        popup = tk.Toplevel(self.root)
        popup.wm_overrideredirect(True)
        popup.wm_geometry(f"+{abs_x}+{abs_y}")
        lb = tk.Listbox(popup, exportselection=False)
        lb.pack(side=tk.LEFT, fill=tk.BOTH)
        for item in suggestions: lb.insert(tk.END, item)
        if len(suggestions) > 10:
            scrollbar = tk.Scrollbar(popup, orient=tk.VERTICAL, command=lb.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            lb.config(yscrollcommand=scrollbar.set)
        self.autocomplete_popup = popup
        self.autocomplete_listbox = lb
        self.autocomplete_start_index = start_index
        self.autocomplete_prefix = prefix
        if self.theme == 'dark':
            lb.config(bg='#2b2b2b', fg='#d4d4d4', selectbackground='#264f78')
        else:
            lb.config(bg='#ffffff', fg='#000000', selectbackground='#cce8ff')
        lb.focus_set()
        lb.selection_set(0)
        lb.bind("<Return>", self._autocomplete_select)
        lb.bind("<Double-Button-1>", self._autocomplete_select)
        lb.bind("<Escape>", lambda e: self._hide_popup())
        lb.bind("<Up>", self._on_popup_up)
        lb.bind("<Down>", self._on_popup_down)
        self.editor.bind("<Button-1>", lambda e: self._hide_popup())

    def _hide_popup(self):
        if hasattr(self, 'autocomplete_popup') and self.autocomplete_popup:
            try: self.autocomplete_popup.destroy()
            except: pass
        self.autocomplete_popup = None
        self.autocomplete_listbox = None
        try: self.editor.unbind("<Button-1>")
        except: pass

    def _on_popup_up(self, event):
        lb = self.autocomplete_listbox
        if not lb: return "break"
        idx = lb.curselection()
        if idx:
            i = idx[0]
            if i > 0:
                lb.selection_clear(0, tk.END)
                lb.selection_set(i-1)
        return "break"

    def _on_popup_down(self, event):
        lb = self.autocomplete_listbox
        if not lb: return "break"
        idx = lb.curselection()
        if idx:
            i = idx[0]
            if i < lb.size()-1:
                lb.selection_clear(0, tk.END)
                lb.selection_set(i+1)
        return "break"

    def _autocomplete_select(self, event):
        lb = self.autocomplete_listbox
        if not lb: return "break"
        sel = lb.curselection()
        if not sel: return "break"
        text = lb.get(sel[0])
        try:
            self.editor.delete(self.autocomplete_start_index, tk.INSERT)
            self.editor.insert(self.autocomplete_start_index, text)
        except Exception:
            pass
        self._hide_popup()
        return "break"

# ---------- main ----------
def main():
    root = tk.Tk()
    gui = CircuitEditorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
