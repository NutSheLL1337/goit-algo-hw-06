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

# DFS
dfs_tree = nx.dfs_tree(G, source='User')
print(f"Застосування DFS: {list(dfs_tree.edges())}")  # виведе ребра DFS-дерева з коренем у вузлі User

# BFS
bfs_tree = nx.bfs_tree(G, source='User')
print(f"Застосування BFS: {list(bfs_tree.edges())}")  # виведе ребра BFS-дерева з коренем у вузлі User


# Task 3
# Застосування алгоритму Дейкстри
G.add_edge('User', 'Email', weight=5)
G.add_edge('User', 'IP', weight=10)
G.add_edge('User', 'Phone', weight=10)

shortest_paths = nx.single_source_dijkstra_path(G, source='User')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='User')

print(f"\nНайкоротші шляхи від вузла 'User' до всіх інших вузлів: {shortest_paths}")  # виведе найкоротші шляхи від вузла 'User' до всіх інших вузлів
print(f"\nДовжини найкоротших шляхів від вузла 'User' до всіх інших вузлів: {shortest_path_lengths}")  # виведе довжини найкоротших шляхів від вузла 'User' до всіх інших вузлів


options = {
    "node_color": "yellow",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}
nx.draw(G, **options)
plt.show()

