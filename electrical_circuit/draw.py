import networkx as nx
import matplotlib.pyplot as plt
import re

# Input data
data = """
V1 {R1, C1}
R1 {V1, C1}
C1 {R1, V1}

V1 = PULSE(0 5 0 1n 1n 10u 20u)
R1 = 1k
C1 = 10u
"""

# Parse connections and values
connection_pattern = re.compile(r'(\w+)\s*{\s*([^}]+)}')
value_pattern = re.compile(r'(\w+)\s*=\s*(.+)')

graph = nx.Graph()
component_values = {}

# Parse connections
for match in connection_pattern.finditer(data):
    component = match.group(1)
    connections = [conn.strip() for conn in match.group(2).split(',')]
    for node in connections:
        graph.add_edge(component, node)

# Parse values
for match in value_pattern.finditer(data):
    name, value = match.group(1), match.group(2)
    component_values[name] = value

# Fixed layout: manually place components
pos = {
    'V1': (1, 2),
    'R1': (0, 1),
    'C1': (2, 1),
}

# Draw the graph
plt.figure(figsize=(6, 6))
nx.draw(graph, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=10)

# Draw values as edge labels
edge_labels = {}
for edge in graph.edges:
    for node in edge:
        if node in component_values:
            edge_labels[edge] = component_values[node]
            break

nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color="red")

plt.title("Circuit with Vertical & Diagonal Connections")
plt.axis('off')
plt.tight_layout()
plt.show()
