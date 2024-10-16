import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Створюємо граф
G = nx.Graph()

# Додаємо вузли та ребра
G.add_node("User")
G.add_nodes_from(["Email", "Phone", "Address", "IP", "Country", "City"])
G.add_edges_from([("User", "Email"), ("User", "Phone"), ("Email", "Phone"), ("User", "Address"), ("User", "IP"), ("Address", "City"), ("Address", "Country")])

# Виводимо інформацію про граф
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
is_connected = nx.is_connected(G)

print(f"Вузли: {G.nodes()}")
print(f"Ребра: {G.edges()}")
print(f"Кількість вузлів: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Чи є граф сполученим (зв’язним): {is_connected}")

# Реалізація BFS
def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            # Додаємо всіх сусідів, використовуючи graph.neighbors для networkx
            queue.extend(set(graph.neighbors(vertex)) - visited)
    
    return visited

# Реалізація DFS
def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            # Додаємо сусідів до стеку (reversed для послідовності)
            stack.extend(reversed(list(graph.neighbors(vertex))))
    
    return visited

# Викликаємо алгоритми
print("\nDFS:")
dfs_tree = dfs_iterative(G, 'User')

print("\nBFS:")
bfs_tree = bfs_iterative(G, 'User')

# Додаємо ваги до графа для завдання Дейкстри
G.add_edge('User', 'Email', weight=5)
G.add_edge('User', 'IP', weight=10)
G.add_edge('User', 'Phone', weight=10)
G.add_edge('Email', 'Phone', weight=1)
G.add_edge('Address', 'City', weight=2)
G.add_edge('Address', 'Country', weight=4)

# Алгоритм Дейкстри
def dijkstra(graph, start):
    # Ініціалізація відстаней і попередників
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph.nodes()}
    
    # Список вершин для відвідування
    vertices = set(graph.nodes())
    
    while vertices:
        # Знаходимо вершину з мінімальною відстанню
        current_vertex = min(vertices, key=lambda vertex: distances[vertex])
        vertices.remove(current_vertex)

        if distances[current_vertex] == float('infinity'):
            break

        # Оновлюємо відстані до сусідів
        for neighbor in graph.neighbors(current_vertex):
            edge_weight = graph[current_vertex][neighbor].get('weight', 1)
            alternative_route = distances[current_vertex] + edge_weight

            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_vertices[neighbor] = current_vertex

    return distances, previous_vertices

# Виклик алгоритму Дейкстри для стартової вершини 'User'
distances, previous_vertices = dijkstra(G, 'User')

print("\nНайкоротші відстані від 'User':")
print(distances)

# Функція для відтворення шляху
def reconstruct_path(previous_vertices, start, target):
    path = []
    current_vertex = target
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path = path[::-1]  # Перевертаємо шлях
    if path[0] == start:
        return path
    return []

# Приклад відтворення шляху від 'User' до 'City'
print("\nШлях від 'User' до 'City':")
path_to_city = reconstruct_path(previous_vertices, 'User', 'City')
print(path_to_city)

# Візуалізація графа
options = {
    "node_color": "yellow",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}
nx.draw(G, **options)
plt.show()
