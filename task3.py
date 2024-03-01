import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(["User1", "User2", "User3", "User4", "User5"])
G.add_edge("User1", "User2", weight=5)
G.add_edge("User1", "User3", weight=2)
G.add_edge("User2", "User3", weight=1)
G.add_edge("User3", "User4", weight=3)
G.add_edge("User4", "User5", weight=4)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
edge_labels = nx.get_edge_attributes(G, 'weight') 
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Соц мережа")
plt.show()

# Знаходження найкоротшого шляху в розробленому графі
source = "User1"
shortest_paths = nx.single_source_dijkstra_path(G, source)

# Знайдіть найкоротший шлях між всіма вершинами графа
print("Найкоротші шляхи від вершини", source)
for target, path in shortest_paths.items():
    print(f"Вершина {target}: Шлях {path} з вагою {nx.shortest_path_length(G, source, target, weight='weight')}")