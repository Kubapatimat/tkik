#!/usr/bin/env python3
"""
Circuitry Editor i Symulacja z podświetlaniem składni, numeracją linii, tematem (dark/light)
oraz podstawowym autocomplete (Ctrl+Space) dla słów kluczowych i symboli zdefiniowanych w kodzie.

Wymaga:
- tkinter (w standardzie Pythona)
- antlr4 Runtime i wygenerowane pliki CircuitryLexer, CircuitryParser, CircuitryParserVisitor
- moduły circuitry.builder, circuitry.error_listener, circuitry.utils, circuitry.mna itd.

Zapisz np. jako `circuit_editor.py` i uruchom `python circuit_editor.py`.
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
from circuitry.builder import CircuitBuilderVisitor
from circuitry.error_listener import FriendlyErrorListener
from circuitry.gen.CircuitryLexer import CircuitryLexer
from circuitry.gen.CircuitryParser import CircuitryParser
from circuitry.gen.CircuitryParserVisitor import CircuitryParserVisitor
from circuitry.utils import to_polar_str
import math


def process_circuit_content(content: str):
    """
    Przetwarza tekst z edytora jako definicję układu.
    Zwraca tuple: (success: bool, warnings: list of (line, col, msg), raw_output: str).
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
            return success, [], str_io.getvalue()

        # Parsowanie ANTLR z treści
        input_stream = InputStream(content)
        listener = FriendlyErrorListener(input_stream)

        lexer = CircuitryLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(listener)

        stream = CommonTokenStream(lexer)
        parser = CircuitryParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)

        try:
            tree = parser.program()
        except RuntimeError as ex:
            msg = str(ex)
            return False, [], msg

            # Sprawdź błędy składni
        if listener.reportAllErrors():
            # zbieramy sformatowane błędy
            errors = listener.format_syntax_errors()
            # np. zwracamy success=False, warnings=[], raw_output jako połączone errors
            raw = "\n\n".join(errors)
            return False, [], raw

        # Wizyta semantyczna
        visitor = CircuitBuilderVisitor(error_listener=listener)
        visitor.visit(tree)
        if listener.semantic_errors:
            sem_errs = listener.format_semantic_errors()
            raw = "\n\n".join(sem_errs)
            # możesz również zebrać warningi i dołączyć
            return False, listener.warnings, raw

        # Zbierz semantyczne warningi
        warnings = getattr(listener, 'warnings', [])

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

        return success, warnings, str_io.getvalue()

    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}", file=sys.stderr)
        success = False
        warnings = getattr(listener, 'warnings', []) if listener else []
        return success, warnings, str_io.getvalue()
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr


# Opcjonalnie: własny prosty visitor do zbierania symboli w collect_symbols:
class SymbolCollectorVisitor(CircuitryParserVisitor):
    """
    Visitor zbierający nazwy zmiennych, aliasów, komponentów, funkcji, subcircuitów itd.
    Dostosuj metody wg potrzeb i wg wygenerowanej hierarchii kontekstów.
    """
    def __init__(self):
        super().__init__()
        self.symbols = set()

    def visitLetStatement(self, ctx: CircuitryParser.LetStatementContext):
        # letStatement: LET letAssignment (COMMA letAssignment)* SEMICOLON
        for laCtx in ctx.letAssignment():
            # letAssignment: ID ASSIGN expr
            id_term = laCtx.ID()
            if id_term:
                name = id_term.getText()
                self.symbols.add(name)
        return self.visitChildren(ctx)

    def visitAliasStatement(self, ctx: CircuitryParser.AliasStatementContext):
        # aliasStatement: ALIAS aliasAssignment (COMMA aliasAssignment)* SEMICOLON
        for aaCtx in ctx.aliasAssignment():
            # aliasAssignment: ID ASSIGN ID
            id0 = aaCtx.ID(0)
            if id0:
                self.symbols.add(id0.getText())
        return self.visitChildren(ctx)

    def visitComponentStatement(self, ctx: CircuitryParser.ComponentStatementContext):
        # componentStatement: componentType ID ASSIGN expr COLON nodeList SEMICOLON
        ids = ctx.ID()
        # Pierwsze ID to typ, drugie to nazwa instancji
        if len(ids) >= 2:
            inst_name = ids[1].getText()
            self.symbols.add(inst_name)
        return self.visitChildren(ctx)

    def visitFunctionDefinition(self, ctx: CircuitryParser.FunctionDefinitionContext):
        # functionDefinition: FN ID LPAREN ...
        id_term = ctx.ID()
        if id_term:
            name = id_term.getText()
            self.symbols.add(name)
        return self.visitChildren(ctx)

    def visitSubcircuitDefinition(self, ctx: CircuitryParser.SubcircuitDefinitionContext):
        # subcircuitDefinition: SUBCIRCUIT ID LPAREN ...
        id_term = ctx.ID()
        if id_term:
            name = id_term.getText()
            self.symbols.add(name)
        return self.visitChildren(ctx)

    # Dodaj inne metody zbierające nazwy (np. case labels, parametry funkcji itp.) jeśli potrzebujesz.


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

        # Gutter z numerami linii
        self.line_numbers = tk.Text(
            editor_frame, width=4, padx=3, takefocus=0, border=0,
            state='disabled'
        )
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Główny edytor
        self.editor = tk.Text(editor_frame, wrap=tk.WORD, undo=True)
        self.editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar współdzielony
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
        # Tag do pogrubienia
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

        # Handler logowania (opcjonalnie)
        self.text_handler = TextHandler(self.output)
        formatter = logging.Formatter('%(message)s')
        self.text_handler.setFormatter(formatter)

        # --- Lista statycznych słów kluczowych dla autocomplete ---
        self.static_keywords = [
            'alias','let','fn','return','series','parallel','reversed','subcircuit',
            'import','if','else','for','while','do','break','continue',
            'switch','case','default','true','false','transient','ac','dc',
            'measure','pos'
        ]

        # --- Syntax highlighting patterns ---
        # Bazowane na tokenach z gramatyki
        multiline_comment_pattern = r'/\*[\s\S]*?\*/'
        line_comment_pattern = r'//.*'
        string_pattern = r'"([^"\\]|\\.)*"'
        # Słowa kluczowe regex: \b(?:kw1|kw2|...)\b
        kw_pattern = r'\b(?:' + '|'.join(re.escape(kw) for kw in self.static_keywords) + r')\b'
        # Float literal z optional underscore, exponent, suffix
        float_pattern = (
            r'\b[+-]?'
            r'(?:\d[\d_]*)'
            r'(?:\.\d[\d_]*)?'
            r'(?:[eE][+-]?\d+)?'
            r'(?:[fpnu\u03BCmkKMGTP])?'
            r'\b'
        )
        # Operatory
        operator_pattern = r'(\b&&\b|\|\||==|!=|<=|>=|\+\+|--|\+=|-=|\*=|/=|%=|\^=|->|[+\-*/%^!:<>=])'

        # Kolejność: najpierw nie-komentarze, potem komentarze na końcu
        self.syntax_patterns = [
            (re.compile(string_pattern), 'string'),
            (re.compile(kw_pattern), 'keyword'),
            (re.compile(float_pattern), 'number'),
            (re.compile(operator_pattern), 'operator'),
            (re.compile(multiline_comment_pattern), 'comment'),
            (re.compile(line_comment_pattern), 'comment'),
        ]
        # Konfiguracja tagów; kolory nadamy w apply_theme
        self.editor.tag_configure('comment', foreground='#6a9955')
        self.editor.tag_configure('string', foreground='#ce9178')
        self.editor.tag_configure('keyword', foreground='#569cd6')
        self.editor.tag_configure('number', foreground='#b5cea8')
        self.editor.tag_configure('operator', foreground='#d4d4d4')

        # --- Bindowania ---
        # Podświetlanie składni i numeracja linii
        self.editor.bind('<KeyRelease>', self._on_key_release)
        self.editor.bind('<<Modified>>', self._on_modified)
        self.editor.bind('<MouseWheel>', self._on_scroll_event)  # Windows
        self.editor.bind('<Button-4>', self._on_scroll_event)    # Linux scroll up
        self.editor.bind('<Button-5>', self._on_scroll_event)    # Linux scroll down
        self.editor.bind('<Configure>', lambda e: self._update_line_numbers())

        # Autocomplete: Ctrl+Space
        self.editor.bind('<Control-space>', self.show_autocomplete)

        # Inicjalne ustawienia
        self.apply_theme()
        self._update_line_numbers()
        # Wstępne podświetlenie (jeśli w edytorze już coś jest)
        self.highlight_syntax()

    def set_theme(self, theme_name):
        if theme_name not in ('light', 'dark'):
            return
        self.theme = theme_name
        self.apply_theme()
        # po zmianie motywu odśwież highlight
        self.highlight_syntax()

    def apply_theme(self):
        """Ustaw kolory widgetów i tagów wg motywu."""
        if self.theme == 'dark':
            editor_bg = '#1e1e1e'; editor_fg = '#d4d4d4'
            gutter_bg = '#2b2b2b'; gutter_fg = '#858585'
            output_bg = '#252526'; output_fg = '#e5e5e5'
            select_bg = '#264f78'; insert_color = '#ffffff'
            # kolory tagów
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

        # Ustawienia widgetów
        self.editor.config(bg=editor_bg, fg=editor_fg,
                           insertbackground=insert_color,
                           selectbackground=select_bg)
        self.line_numbers.config(bg=gutter_bg, fg=gutter_fg)
        self.output.config(bg=output_bg, fg=output_fg,
                           insertbackground=insert_color,
                           selectbackground=select_bg)
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
        # Zamknij autocomplete, gdy poruszamy kursorem
        if event and event.keysym in ('Up', 'Down', 'Left', 'Right', 'Return', 'Escape'):
            self._hide_popup()
        else:
            # Podświetl składnię
            self.editor.after_idle(self.highlight_syntax)
        self._update_line_numbers()

    def highlight_syntax(self):
        """
        Podświetla składnię według regexów w self.syntax_patterns.
        Komentarze nakładamy jako ostatnie, by mieć priorytet.
        """
        text = self.editor.get('1.0', 'end-1c')
        # Usuń stare tagi
        for _, tag in self.syntax_patterns:
            self.editor.tag_remove(tag, '1.0', tk.END)
        # Najpierw nie-komentarze
        for pattern, tag in self.syntax_patterns:
            if tag == 'comment':
                continue
            for m in pattern.finditer(text):
                start_idx = m.start()
                end_idx = m.end()
                start = f"1.0 + {start_idx}c"
                end = f"1.0 + {end_idx}c"
                try:
                    self.editor.tag_add(tag, start, end)
                except tk.TclError:
                    pass
        # Potem komentarze
        for pattern, tag in self.syntax_patterns:
            if tag != 'comment':
                continue
            for m in pattern.finditer(text):
                start_idx = m.start()
                end_idx = m.end()
                start = f"1.0 + {start_idx}c"
                end = f"1.0 + {end_idx}c"
                try:
                    self.editor.tag_add(tag, start, end)
                except tk.TclError:
                    pass
        # Priorytet
        try:
            self.editor.tag_raise('comment')
        except Exception:
            pass

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
        success, warnings, raw_output = process_circuit_content(content)
        self.root.after(0, lambda: self.display_result(success, warnings, raw_output))

    def display_result(self, success: bool, warnings: list, raw_output: str):
        # Wstaw warningi semantyczne na górze
        if warnings:
            for (line, col, msg) in warnings:
                text = f"⚠️ Warning at line {line}, column {col}:\n    {msg}\n\n"
                self.output.insert(tk.END, text)
            self.output.insert(tk.END, "-"*40 + "\n")
        # Filtrowanie inline-warningów
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
        # Pogrub ostatniej niepustej linii
        all_text = self.output.get(1.0, tk.END).splitlines()
        for idx in range(len(all_text)-1, -1, -1):
            if all_text[idx].strip():
                line_no = idx + 1
                start = f"{line_no}.0"
                end = f"{line_no}.end"
                self.output.tag_add('bold', start, end)
                break
        self.output.see(tk.END)
        if success:
            messagebox.showinfo("Gotowe", "Analiza zakończona pomyślnie.")
        else:
            messagebox.showwarning("Zakończono", "Analiza zakończona z błędami. Sprawdź logi.")
        self.running = False

    def collect_symbols(self):
        """
        Parsuje aktualną zawartość edytora i zwraca zbiór nazw zdefiniowanych:
        aliasy, zmienne let, komponenty, funkcje, subcircuity.
        Używa SymbolCollectorVisitor dla wydajności.
        """
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
            # Błąd składni lub inny: zwracamy pusty lub co udało się zebrać
            pass
        return symbols

    def show_autocomplete(self, event=None):
        """
        Wywoływane na Ctrl+Space: wyciąga prefix przed kursorem i pokazuje listę sugestii.
        """
        # Uzyskaj pozycję kursora i tekst przed nim w bieżącej linii
        idx = self.editor.index(tk.INSERT)  # "line.col"
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

        # Statyczne
        suggestions = []
        for kw in self.static_keywords:
            if prefix == '' or kw.startswith(prefix):
                suggestions.append(kw)
        # Dynamiczne
        symbols = self.collect_symbols()
        for s in symbols:
            if prefix == '' or s.startswith(prefix):
                suggestions.append(s)
        # Unikalne, posortowane
        suggestions = sorted(set(suggestions), key=lambda x: x.lower())
        if not suggestions:
            return "break"
        # Pokaż popup
        self._show_popup(suggestions, start_index, prefix)
        return "break"

    def _show_popup(self, suggestions, start_index, prefix):
        # Usuń istniejący
        if hasattr(self, 'autocomplete_popup') and self.autocomplete_popup:
            try:
                self.autocomplete_popup.destroy()
            except Exception:
                pass

        # Pozycja w pikselach
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

        for item in suggestions:
            lb.insert(tk.END, item)

        if len(suggestions) > 10:
            scrollbar = tk.Scrollbar(popup, orient=tk.VERTICAL, command=lb.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            lb.config(yscrollcommand=scrollbar.set)

        self.autocomplete_popup = popup
        self.autocomplete_listbox = lb
        self.autocomplete_start_index = start_index
        self.autocomplete_prefix = prefix

        # Styl popup wg motywu
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

        # Kliknięcie w edytor poza popup usuwa popup
        self.editor.bind("<Button-1>", lambda e: self._hide_popup())

    def _hide_popup(self):
        if hasattr(self, 'autocomplete_popup') and self.autocomplete_popup:
            try:
                self.autocomplete_popup.destroy()
            except Exception:
                pass
        self.autocomplete_popup = None
        self.autocomplete_listbox = None
        # Odbindowanie, aby nie zostawał stale
        try:
            self.editor.unbind("<Button-1>")
        except Exception:
            pass

    def _on_popup_up(self, event):
        lb = self.autocomplete_listbox
        if not lb:
            return "break"
        idx = lb.curselection()
        if idx:
            i = idx[0]
            if i > 0:
                lb.selection_clear(0, tk.END)
                lb.selection_set(i-1)
        return "break"

    def _on_popup_down(self, event):
        lb = self.autocomplete_listbox
        if not lb:
            return "break"
        idx = lb.curselection()
        if idx:
            i = idx[0]
            if i < lb.size()-1:
                lb.selection_clear(0, tk.END)
                lb.selection_set(i+1)
        return "break"

    def _autocomplete_select(self, event):
        lb = self.autocomplete_listbox
        if not lb:
            return "break"
        sel = lb.curselection()
        if not sel:
            return "break"
        text = lb.get(sel[0])
        try:
            self.editor.delete(self.autocomplete_start_index, tk.INSERT)
            self.editor.insert(self.autocomplete_start_index, text)
        except Exception:
            pass
        self._hide_popup()
        return "break"


def main_gui():
    root = tk.Tk()
    gui = CircuitEditorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main_gui()