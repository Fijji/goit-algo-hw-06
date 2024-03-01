import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(["User1", "User2", "User3", "User4", "User5"])
G.add_edges_from([("User1", "User2"), ("User1", "User3"), ("User2", "User3"), ("User3", "User4"), ("User4", "User5")])

# Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.
dfs_paths = list(nx.dfs_edges(G, source="User1"))
bfs_paths = list(nx.bfs_edges(G, source="User1"))

print("DFS шляхи:", dfs_paths)
print("BFS шляхи:", bfs_paths)

nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
plt.title("Соц мережа")
plt.show()