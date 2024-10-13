import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("User")
G.add_nodes_from(["Email", "Phone", "Address", "IP", "Country", "City"])
G.add_edges_from([("User", "Email"), ("User", "Phone"), ("Email", "Phone"), ("User", "Address"), ("User", "IP"), ("Address", "City"), ("Address", "Country") ])

num_nodes = G.number_of_nodes()  # 4
num_edges = G.number_of_edges()  # 4
is_connected = nx.is_connected(G)  # True

print(f"Вузли: {G.nodes()}")
print(f"Ребра: {G.edges()}")


print(f"Кількість вузлів: {num_nodes}\n"
      f"Кількість ребер: {num_edges}\n"
      f"Чи є граф сполученим (зв’язним): {is_connected}")


options = {
    "node_color": "yellow",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}
nx.draw(G, **options)
plt.show()


"""
Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.

Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. 
Поясніть, чому шляхи для алгоритмів саме такі."""

# DFS
dfs_tree = nx.dfs_tree(G, source='User')
print(list(dfs_tree.edges()))  # виведе ребра DFS-дерева з коренем у вузлі User

# BFS
bfs_tree = nx.bfs_tree(G, source='User')
print(list(bfs_tree.edges()))  # виведе ребра BFS-дерева з коренем у вузлі User