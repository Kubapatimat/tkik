import ply.lex as lex
import ply.yacc as yacc
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Rectangle, Circle, Arrow

# Lexer implementation
tokens = (
    'NUMBER',
    'IDENTIFIER',
    'LET',
    'EQUALS',
    'COMMA',
    'COLON',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'ARROW',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'SUBCIRCUIT',
    'SERIES',
    'PARALLEL',
    'TRANSIENT',
    'OP',
    'AC',
)

reserved = {
    'let': 'LET',
    'subcircuit': 'SUBCIRCUIT',
    'series': 'SERIES',
    'parallel': 'PARALLEL',
    'transient': 'TRANSIENT',
    'op': 'OP',
    'ac': 'AC',
}

t_EQUALS = r'='
t_COMMA = r','
t_COLON = r':'
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ARROW = r'->'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'(\d+\.\d*|\.\d+|\d+)([kMGTPmunμpf])?'
    value = t.value
    multipliers = {
        'k': 1e3, 'M': 1e6, 'G': 1e9, 'T': 1e12, 'P': 1e15,
        'm': 1e-3, 'u': 1e-6, 'μ': 1e-6, 'n': 1e-9, 'p': 1e-12, 'f': 1e-15
    }
    
    suffix = value[-1] if value[-1] in multipliers else None
    if suffix:
        num_value = float(value[:-1])
        t.value = num_value * multipliers[suffix]
    else:
        t.value = float(value)
    return t

def t_COMMENT(t):
    r'/\*(.|\n)*?\*/|//.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser implementation
def p_program(p):
    '''program : statements'''
    p[0] = {'type': 'program', 'statements': p[1]}

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : component_decl
                 | let_statement'''
    p[0] = p[1]

def p_let_statement(p):
    '''let_statement : LET IDENTIFIER EQUALS expression
                     | LET IDENTIFIER EQUALS expression COMMA IDENTIFIER EQUALS expression'''
    if len(p) == 5:
        p[0] = {'type': 'let', 'assignments': [(p[2], p[4])]}
    else:
        p[0] = {'type': 'let', 'assignments': [(p[2], p[4]), (p[6], p[8])]}

def p_component_decl(p):
    '''component_decl : IDENTIFIER EQUALS component_value
                      | IDENTIFIER EQUALS component_value COLON node_ref COMMA node_ref'''
    if len(p) == 4:
        p[0] = {'type': 'component', 'name': p[1], 'value': p[3]}
    else:
        p[0] = {'type': 'component', 'name': p[1], 'value': p[3], 
                'node1': p[5], 'node2': p[7]}

def p_component_value(p):
    '''component_value : IDENTIFIER
                       | NUMBER'''
    p[0] = p[1]

def p_node_ref(p):
    '''node_ref : IDENTIFIER'''
    p[0] = {'type': 'node_ref', 'name': p[1]}

def p_expression(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = {'type': 'binary_op', 'op': p[2], 'left': p[1], 'right': p[3]}

def p_term(p):
    '''term : factor
            | term TIMES factor
            | term DIVIDE factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = {'type': 'binary_op', 'op': p[2], 'left': p[1], 'right': p[3]}

def p_factor(p):
    '''factor : NUMBER
              | IDENTIFIER
              | LPAREN expression RPAREN
              | PLUS factor
              | MINUS factor'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = {'type': 'unary_op', 'op': p[1], 'operand': p[2]}

def p_error(p):
    if p:
        print(f"Syntax error at token {p.type} ({p.value}) at line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

# Visualization function
def visualize_circuit(parsed_data):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Node positions (manually specified for clean layout)
    node_positions = {}
    components = []
    
    # First pass: collect nodes and components
    for stmt in parsed_data['statements']:
        if stmt['type'] == 'component' and 'node1' in stmt and 'node2' in stmt:
            node1 = stmt['node1']['name']
            node2 = stmt['node2']['name']
            components.append((node1, node2, stmt['name'], stmt['value']))
    
    # Determine unique nodes and assign positions
    all_nodes = set()
    for node1, node2, _, _ in components:
        all_nodes.add(node1)
        all_nodes.add(node2)
    
    # Assign positions in a grid-like fashion
    nodes = list(all_nodes)
    grid_size = int(len(nodes)**0.5) + 1
    for i, node in enumerate(nodes):
        row = i // grid_size
        col = i % grid_size
        node_positions[node] = (col * 2, -row * 2)  # x, y coordinates
    
    # Draw nodes (connection points)
    for node, pos in node_positions.items():
        ax.add_patch(Circle(pos, radius=0.1, color='black'))
        ax.text(pos[0], pos[1], node, ha='center', va='center', color='white', fontsize=8)
    
    # Draw components with Manhattan routing
    for node1, node2, name, value in components:
        x1, y1 = node_positions[node1]
        x2, y2 = node_positions[node2]
        
        # Manhattan-style routing (vertical first then horizontal)
        if abs(x1 - x2) < abs(y1 - y2):
            # Vertical then horizontal
            mid_y = (y1 + y2) / 2
            ax.plot([x1, x1], [y1, mid_y], 'k-', lw=2)  # Vertical
            ax.plot([x1, x2], [mid_y, mid_y], 'k-', lw=2)  # Horizontal
            ax.plot([x2, x2], [mid_y, y2], 'k-', lw=2)  # Vertical
        else:
            # Horizontal then vertical
            mid_x = (x1 + x2) / 2
            ax.plot([x1, mid_x], [y1, y1], 'k-', lw=2)  # Horizontal
            ax.plot([mid_x, mid_x], [y1, y2], 'k-', lw=2)  # Vertical
            ax.plot([mid_x, x2], [y2, y2], 'k-', lw=2)  # Horizontal
        
        # Add component label at midpoint
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        ax.text(mid_x, mid_y, f"{name}\n{value}", 
                ha='center', va='center', 
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
    
    plt.tight_layout()
    plt.show()

# Example usage with parser
if __name__ == "__main__":
    data = """
    V = 10 : IN, GND
    R1 = 1k : IN, OUT
    R2 = 2k : OUT, GND
    C1 = 100u : OUT, GND
    """

    data_voltage_divider = """
    V = 5 : VCC, GND
    R1 = 1k : VCC, MID
    R2 = 2k : MID, GND
    """

    data_rc_low_pass_filter = """
    Vin = sine(1, 1k) : IN, GND
    R1 = 1k : IN, OUT
    C1 = 100n : OUT, GND
    """

    data_series_rlc_circiut = """
    V = pulse(0,5,0,1m,1m) : IN, GND
    R1 = 100 : IN, N1
    L1 = 10m : N1, N2
    C1 = 1u : N2, GND
    """

    data_pararell_components = """
    V = 12 : VCC, GND
    R1 = 1k : VCC, N1
    R2 = 2k : N1, GND
    R3 = 3k : N1, GND
    """

    data_voltage_source_with_nultiple_loads = """
    V = 9 : BAT, GND
    R1 = 100 : BAT, LED1
    D1 = LED : LED1, GND
    R2 = 200 : BAT, LED2
    D2 = LED : LED2, GND
    """

    data_wheatstone_bridge = """`
    V = 5 : VCC, GND
    R1 = 1000 : VCC, A
    R2 = 1000 : A, GND
    R3 = 2000 : VCC, B
    R4 = 2000 : B, GND
    RG = 100 : A, B
    """
    
    # Parse the circuit description
    result = parser.parse(data_wheatstone_bridge)
    print("Parsed result:", result)
    
    # Visualize the circuit with Manhattan routing
    visualize_circuit(result)