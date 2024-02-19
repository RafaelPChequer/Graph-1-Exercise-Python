import networkx as nx
import matplotlib.pyplot as plt

# Load Karate Club network from NetworkX library
G = nx.karate_club_graph()

# Print graph summary
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Density:", nx.density(G))

# Calculate some network metrics
avg_degree = sum(dict(G.degree()).values()) / G.number_of_nodes()
clustering_coefficient = nx.average_clustering(G)

print("Average degree:", avg_degree)
print("Clustering coefficient:", clustering_coefficient)

# Plot degree distribution
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_count = {}
for degree in degree_sequence:
    if degree in degree_count:
        degree_count[degree] += 1
    else:
        degree_count[degree] = 1
plt.bar(degree_count.keys(), degree_count.values())
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Count")
plt.show()

# Plot graph using different layouts
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

pos1 = nx.spring_layout(G)
nx.draw(G, pos1, ax=axs[0], node_size=50)
axs[0].set_title("Spring Layout")

pos2 = nx.random_layout(G, seed=42)
nx.draw(G, pos2, ax=axs[1], node_size=50)
axs[1].set_title("Random Layout")

pos3 = nx.circular_layout(G)
nx.draw(G, pos3, ax=axs[2], node_size=50)
axs[2].set_title("Circular Layout")

plt.show()

# Final result discussion

"""This code loads the Karate Club network from NetworkX library and calculates some network metrics, such as the number of nodes, number of edges, density, average degree, and clustering coefficient. It also plots the degree distribution and the graph using different layouts, including spring, random, and circular layouts. The final result shows that the Karate Club network is a small, but densely connected graph with 34 nodes and 78 edges, indicating a high degree of cohesion among the club members. The degree distribution is bimodal, with a few members having a very high degree and most members having a low degree. The different layouts reveal different patterns of connectivity and community structure, with the spring layout emphasizing the clusters and the random layout and circular layout highlighting the diversity of connections. The code provides a fascinating case study of social interactions and demonstrates the power of network analysis for understanding complex systems."""




