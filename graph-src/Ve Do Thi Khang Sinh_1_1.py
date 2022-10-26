import csv
import pylab
import random
import networkx as nx
import sys
G = nx.Graph()

# === test random
N = 16
i = 0
#W = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
S = [40, 80, 60, 30, 100, 20, 90, 15,
     35, 90, 55, 70, 80, 25, 10, 75]
# === test 2

number = 0.0

# for row in csv_file:
# if current rows 2nd value is equal to input, print that row
# if number == row[1]:
#print (row[0])
# do somethinngs
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
col_index = 0
row_index = 0
csv_file = csv.reader(open('RawData.csv', "r"), delimiter=",")
while (i < N):
    i += 1
    j = i
    while (j < N):
        j += 1
        for row in csv_file:
            while (row_index < (N-1)):
                col_index = row_index + 1
                while (row_index < N):
                    # weight = row[row_index]
                    # G.add_edge(col_index, row_index, color='#23a9dd', weight=0.4)
                    row_index = row_index + 1
                    print(f'col_index = {col_index}')
                col_index = col_index + 1

exit(0)
# G.add_edge(0, 1, color='#23a9dd', weight=0.4)
# G.add_edge(0, 2, color='#23a9dd', weight=0.37)
# G.add_edge(0, 3, color='#23a9dd', weight=0.31)
# G.add_edge(0, 4, color='#23a9dd', weight=0.3)
# G.add_edge(0, 5, color='#23a9dd', weight=0.26)
# G.add_edge(0, 6, color='#23a9dd', weight=0.31)
# G.add_edge(0, 7, color='#23a9dd', weight=0.29)
# G.add_edge(0, 8, color='#23a9dd', weight=0.27)
# G.add_edge(0, 9, color='#23a9dd', weight=0.04)
# G.add_edge(0, 10, color='#23a9dd', weight=0.0)
# G.add_edge(0, 11, color='#23a9dd', weight=0.11)
# G.add_edge(0, 12, color='#23a9dd', weight=0.41)
# G.add_edge(0, 13, color='#23a9dd', weight=0.33)
# G.add_edge(0, 14, color='#23a9dd', weight=0)
# G.add_edge(0, 15, color='#23a9dd', weight=0.28)

# G.add_edge(1, 2, color='#23a9dd', weight=0.29)
# G.add_edge(1, 3, color='#23a9dd', weight=0.28)
# G.add_edge(1, 4, color='#23a9dd', weight=0.25)
# G.add_edge(1, 5, color='#23a9dd', weight=0.29)
# G.add_edge(1, 6, color='#23a9dd', weight=0.4)
# G.add_edge(1, 7, color='#23a9dd', weight=0.4)
# G.add_edge(1, 8, color='#23a9dd', weight=0.4)
# G.add_edge(1, 9, color='#23a9dd', weight=0.4)
# G.add_edge(1, 10, color='#23a9dd', weight=0.4)
# G.add_edge(1, 11, color='#23a9dd', weight=0.4)
# G.add_edge(1, 12, color='#23a9dd', weight=0.4)
# G.add_edge(1, 13, color='#23a9dd', weight=0.4)
# G.add_edge(1, 14, color='#23a9dd', weight=0.4)
# G.add_edge(1, 15, color='#23a9dd', weight=0.4)

# G.add_edge(2, 3, color='#23a9dd', weight=0.4)
# G.add_edge(2, 4, color='#23a9dd', weight=0.4)
# G.add_edge(2, 5, color='#23a9dd', weight=0.4)
# G.add_edge(2, 6, color='#23a9dd', weight=0.4)
# G.add_edge(2, 7, color='#23a9dd', weight=0.4)
# G.add_edge(2, 8, color='#23a9dd', weight=0.4)
# G.add_edge(2, 9, color='#23a9dd', weight=0.4)
# G.add_edge(2, 10, color='#23a9dd', weight=0.4)
# G.add_edge(2, 11, color='#23a9dd', weight=0.4)
# G.add_edge(2, 12, color='#23a9dd', weight=0.4)
# G.add_edge(2, 13, color='#23a9dd', weight=0.4)
# G.add_edge(2, 14, color='#23a9dd', weight=0.4)
# G.add_edge(2, 15, color='#23a9dd', weight=0.4)

# G.add_edge(3, 4, color='#23a9dd', weight=0.4)
# G.add_edge(3, 5, color='#23a9dd', weight=0.4)
# G.add_edge(3, 6, color='#23a9dd', weight=0.4)
# G.add_edge(3, 7, color='#23a9dd', weight=0.4)
# G.add_edge(3, 8, color='#23a9dd', weight=0.4)
# G.add_edge(3, 9, color='#23a9dd', weight=0.4)
# G.add_edge(3, 10, color='#23a9dd', weight=0.4)
# G.add_edge(3, 11, color='#23a9dd', weight=0.4)
# G.add_edge(3, 12, color='#23a9dd', weight=0.4)
# G.add_edge(3, 13, color='#23a9dd', weight=0.4)
# G.add_edge(3, 14, color='#23a9dd', weight=0.4)
# G.add_edge(3, 15, color='#23a9dd', weight=0.4)

# G.add_edge(4, 5, color='#23a9dd', weight=0.4)
# G.add_edge(4, 6, color='#23a9dd', weight=0.4)
# G.add_edge(4, 7, color='#23a9dd', weight=0.4)
# G.add_edge(4, 8, color='#23a9dd', weight=0.4)
# G.add_edge(4, 9, color='#23a9dd', weight=0.4)
# G.add_edge(4, 10, color='#23a9dd', weight=0.4)
# G.add_edge(4, 11, color='#23a9dd', weight=0.4)
# G.add_edge(4, 12, color='#23a9dd', weight=0.4)
# G.add_edge(4, 13, color='#23a9dd', weight=0.4)
# G.add_edge(4, 14, color='#23a9dd', weight=0.4)
# G.add_edge(4, 15, color='#23a9dd', weight=0.4)

# G.add_edge(5, 6, color='#23a9dd', weight=0.4)
# G.add_edge(5, 7, color='#23a9dd', weight=0.4)
# G.add_edge(5, 8, color='#23a9dd', weight=0.4)
# G.add_edge(5, 9, color='#23a9dd', weight=0.4)
# G.add_edge(5, 10, color='#23a9dd', weight=0.4)
# G.add_edge(5, 11, color='#23a9dd', weight=0.4)
# G.add_edge(5, 12, color='#23a9dd', weight=0.4)
# G.add_edge(5, 13, color='#23a9dd', weight=0.4)
# G.add_edge(5, 14, color='#23a9dd', weight=0.4)
# G.add_edge(5, 15, color='#23a9dd', weight=0.4)

# G.add_edge(6, 7, color='#23a9dd', weight=0.4)
# G.add_edge(6, 8, color='#23a9dd', weight=0.4)
# G.add_edge(6, 9, color='#23a9dd', weight=0.4)
# G.add_edge(6, 10, color='#23a9dd', weight=0.4)
# G.add_edge(6, 11, color='#23a9dd', weight=0.4)
# G.add_edge(6, 12, color='#23a9dd', weight=0.4)
# G.add_edge(6, 13, color='#23a9dd', weight=0.4)
# G.add_edge(6, 14, color='#23a9dd', weight=0.4)
# G.add_edge(6, 15, color='#23a9dd', weight=0.4)

# G.add_edge(7, 8, color='#23a9dd', weight=0.4)
# G.add_edge(7, 9, color='#23a9dd', weight=0.4)
# G.add_edge(7, 10, color='#23a9dd', weight=0.4)
# G.add_edge(7, 11, color='#23a9dd', weight=0.4)
# G.add_edge(7, 12, color='#23a9dd', weight=0.4)
# G.add_edge(7, 13, color='#23a9dd', weight=0.4)
# G.add_edge(7, 14, color='#23a9dd', weight=0.4)
# G.add_edge(7, 15, color='#23a9dd', weight=0.4)

# G.add_edge(8, 9, color='#23a9dd', weight=0.4)
# G.add_edge(8, 10, color='#23a9dd', weight=0.4)
# G.add_edge(8, 11, color='#23a9dd', weight=0.4)
# G.add_edge(8, 12, color='#23a9dd', weight=0.4)
# G.add_edge(8, 13, color='#23a9dd', weight=0.4)
# G.add_edge(8, 14, color='#23a9dd', weight=0.4)
# G.add_edge(8, 15, color='#23a9dd', weight=0.4)

# G.add_edge(9, 10, color='#23a9dd', weight=0.4)
# G.add_edge(9, 11, color='#23a9dd', weight=0.4)
# G.add_edge(9, 12, color='#23a9dd', weight=0.4)
# G.add_edge(9, 13, color='#23a9dd', weight=0.4)
# G.add_edge(9, 14, color='#23a9dd', weight=0.4)
# G.add_edge(9, 15, color='#23a9dd', weight=0.4)

# G.add_edge(10, 11, color='#23a9dd', weight=0.4)
# G.add_edge(10, 12, color='#23a9dd', weight=0.4)
# G.add_edge(10, 13, color='#23a9dd', weight=0.4)
# G.add_edge(10, 14, color='#23a9dd', weight=0.4)
# G.add_edge(10, 15, color='#23a9dd', weight=0.4)

# G.add_edge(11, 12, color='#23a9dd', weight=0.4)
# G.add_edge(11, 13, color='#23a9dd', weight=0.4)
# G.add_edge(11, 14, color='#23a9dd', weight=0.4)
# G.add_edge(11, 15, color='#23a9dd', weight=0.4)

# G.add_edge(12, 13, color='#23a9dd', weight=0.4)
# G.add_edge(12, 14, color='#23a9dd', weight=0.4)
# G.add_edge(12, 15, color='#23a9dd', weight=0.4)

# G.add_edge(13, 14, color='#23a9dd', weight=0.4)
# G.add_edge(13, 15, color='#23a9dd', weight=0.4)

# G.add_edge(14, 15, color='#23a9dd', weight=0.4)


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
