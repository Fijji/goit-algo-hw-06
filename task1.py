import networkx as nx
import matplotlib.pyplot as plt

# Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (соціальної мережі)
G = nx.Graph()
G.add_nodes_from(["User1", "User2", "User3", "User4", "User5"])
G.add_edges_from([("User1", "User2"), ("User1", "User3"), ("User2", "User3"), ("User3", "User4"), ("User4", "User5")])
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
plt.title("Соц мережа")
plt.show()

# Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Список вершин:", list(G.nodes()))
print("Список ребер:", list(G.edges()))
print("Ступінь вершин:", dict(G.degree()))
