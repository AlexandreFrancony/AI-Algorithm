import matplotlib.pyplot as plt
import networkx as nx

# This script visualizes the colored map of South America using NetworkX and Matplotlib,

def display_south_america_graph(result):
    # Define neighbors (same as in create_SouthAmerica_csp)
    neighbours = {
        'CostaRica': ['Panama'],
        'Panama': ['CostaRica', 'Colombia'],
        'Colombia': ['Panama', 'Venezuela', 'Ecuador', 'Peru', 'Brasil'],
        'Venezuela': ['Colombia', 'Guyana', 'Brasil'],
        'Guyana': ['Venezuela', 'Suriname', 'Brasil'],
        'Suriname': ['Guyana', 'GuyaneFr', 'Brasil'],
        'GuyaneFr': ['Suriname', 'Brasil'],
        'Brasil': ['GuyaneFr', 'Suriname', 'Guyana', 'Venezuela', 'Colombia', 'Peru', 'Bolivia', 'Paraguay', 'Argentina', 'Uruguay'],
        'Uruguay': ['Brasil', 'Argentina'],
        'Argentina': ['Uruguay', 'Paraguay', 'Chile', 'Bolivia'],
        'Chile': ['Argentina', 'Bolivia', 'Peru'],
        'Bolivia': ['Chile', 'Argentina', 'Paraguay', 'Peru'],
        'Paraguay': ['Bolivia', 'Argentina', 'Uruguay', 'Brasil'],
        'Peru': ['Bolivia', 'Chile', 'Brasil', 'Ecuador', 'Colombia'],
        'Ecuador': ['Peru', 'Colombia']
    }

    # Create a graph
    G = nx.Graph()

    # Add edges to the graph based on the neighbors
    for country, neighbors in neighbours.items():
        for neighbor in neighbors:
            G.add_edge(country, neighbor)

    # Set positions for the countries
    pos = nx.spring_layout(G, seed=42)

    # Extract the colors from the CSP result
    node_colors = [result[country] for country in G.nodes()]

    # Draw the graph with country labels and CSP result colors
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, font_size=10, font_color='white', font_weight='bold', edge_color='black')
    plt.title('South America Map Coloring (CSP Solution)')
    plt.show()