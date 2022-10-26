import pylab
import random
import networkx as nx

G = nx.Graph()

# === test random
N = 16
i = 0
W = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

# node_sizes: list[int] = []
# for i in range(N):
#     print(i)
#     node_sizes.append(10*random.randint(1, 10))

S = [40, 80, 60, 30, 100, 20, 90, 15,
     35, 90, 55, 70, 80, 25, 10, 75]

# print(S)
# print(type(S))

# L = {}
# for i in range(N):
#     L[i+1] = str(i+1)


L = {
    1: "Aaaaa",
    2: "Bbbbb",
    3: "Ccccc",
    4: "Ddddd",
    5: "Eeeee",
    6: "Fffff",
    7: "Ggggg",
    8: "Hhhhh",
    9: "Iiiii",
    10: "Jjjjj",
    11: "Kkkkk",
    12: "Lllll",
    13: "Mmmmm",
    14: "Nnnnn",
    15: "Ooooo",
    16: "Ppppp"}


while (i < N):
    i += 1
    j = i
    while (j < N):
        j += 1
        G.add_edge(i, j, color='#23a9dd',
                   weight=random.choice(W))

G = nx.relabel_nodes(G, L)

print(list(G))

# === test 2

# mỗi dòng sẽ định nghĩa 1 cạnh của graph G
#          đỉnh1   đỉnh2  màu cạnh          bề dày cạnh
#          |       |      |                 |
G.add_edge(1,      2,     color='#23a9dd',  weight=0.4)


# G.add_edge(1, 3, color='#23a9dd', weight=0.4)
# G.add_edge(1, 4, color='#23a9dd', weight=0.4)
# G.add_edge(1, 5, color='#23a9dd', weight=0.4)
# G.add_edge(1, 6, color='#23a9dd', weight=0.4)
# G.add_edge(1, 7, color='#23a9dd', weight=0.4)
# G.add_edge(1, 8, color='#23a9dd', weight=0.4)

# G.add_edge(2, 3, color='#23a9dd', weight=0.3)
# G.add_edge(2, 4, color='#23a9dd', weight=0.3)
# G.add_edge(2, 5, color='#23a9dd', weight=0.3)
# G.add_edge(2, 6, color='#23a9dd', weight=0.3)
# G.add_edge(2, 7, color='#23a9dd', weight=0.3)
# G.add_edge(2, 8, color='#23a9dd', weight=0.3)

# G.add_edge(3, 4, color='#23a9dd', weight=0.7)
# G.add_edge(3, 5, color='#23a9dd', weight=0.7)
# G.add_edge(3, 6, color='#23a9dd', weight=0.7)
# G.add_edge(3, 7, color='#23a9dd', weight=0.7)
# G.add_edge(3, 8, color='#23a9dd', weight=0.7)

# G.add_edge(4, 5, color='#23a9dd', weight=0.7)
# G.add_edge(4, 6, color='#23a9dd', weight=0.7)
# G.add_edge(4, 7, color='#23a9dd', weight=0.7)
# G.add_edge(4, 8, color='#23a9dd', weight=0.7)

# G.add_edge(5, 6, color='#23a9dd', weight=0.7)
# G.add_edge(5, 7, color='#23a9dd', weight=0.7)
# G.add_edge(5, 8, color='#23a9dd', weight=0.7)

# G.add_edge(6, 7, color='#23a9dd', weight=0.7)
# G.add_edge(6, 8, color='#23a9dd', weight=0.7)

# G.add_edge(7, 8, color='#23a9dd', weight=0.7)


colors = nx.get_edge_attributes(G, 'color').values()
weights = nx.get_edge_attributes(G, 'weight').values()

pos = nx.circular_layout(G)
nx.draw(G, pos,
        edge_color=colors,
        width=list(weights),
        with_labels=False,
        #    node_size=S,
        node_color='#de8953')

pos_higher = nx.circular_layout(G, 1.12)

nx.draw_networkx_labels(G, pos_higher, font_size=12, font_color="#f92672")

pylab.show()
