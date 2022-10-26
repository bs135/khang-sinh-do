import csv
import pylab
import networkx as nx
G = nx.Graph()

# === test random
N = 16
i = 0
# W = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
S = [40, 80, 60, 30, 100, 20, 90, 15,
     35, 90, 55, 70, 80, 25, 120]
# === test 2

number = 0.0

L = {1: "Ampi",
     2: "Amox/Clavu",
     3: "AMP/Sulbac",
     4: "Pipera/tazo",
     5: "Ceftazidim",
     6: "Ceftriaxon",
     7: "Cefepim",
     8: "Ertapenem",
     9: "Imipenem",
     10: "Meropenem",
     11: "Amikacin",
     12: "Genta",
     13: "Cipro",
     14: "Levoflox",
     15: "Colistin",
     16: "TMZ"}

row_index = 0
csv_file = csv.reader(open('RawData.csv', "r"), delimiter=",")
for row in csv_file:
    col_count = len(row)
    print(f'row {row_index}: {col_count} items')
    for col_index in range(col_count):
        weight = float(row[col_index])
        if weight > 0 and col_index != row_index:
            print(f'edge {col_index+1} - {row_index+1} -> {weight}')
            G.add_edge(col_index+1, row_index+1,
                       color='#23a9dd', weight=weight)
    row_index += 1

# exit(0)


G = nx.relabel_nodes(G, L)

colors = nx.get_edge_attributes(G, 'color').values()
weights = nx.get_edge_attributes(G, 'weight').values()

pos = nx.circular_layout(G)
nx.draw(G, pos,
        edge_color=colors,
        width=list(weights),
        with_labels=False,
        node_size=S,
        node_color='#de8953')

pos_higher = nx.circular_layout(G, 1.12)

nx.draw_networkx_labels(G, pos_higher, font_size=12, font_color="#f92672")

pylab.show()
