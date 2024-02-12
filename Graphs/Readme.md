# Graph related Python notebooks

The file named `Tarea Algoritmos Elementales de grafos - Tulio Muñoz Magaña.ipynb` implements the elemental graph searching algorithms (DFS and BFS). the algorithms draw the graphs all over the process indicating 
the active nodes, the unvisited ones and the visited ones. This is useful (and it is made in the script) for implementing an algorithm which finds the the number of connected components of the graph.

The file named `Tarea MST y Kruskal - Tulio Muñoz Magaña.ipynb` implements the Kruskal algorithm, which finds a minimum spanning tree of the given graph (This graph must have 
wheighted edges). The minimum spanning tree is then used for a clustering task. This is made throwing out the edges with the greatest weights in the tree and define 
the connected components of the new graph as the clusters. Doing this, we get to a
clustering which have the greatest possible distance between clusters, the reason for this is beacause the spanning tree that we found was minimum. The other files in this directory
are files necessary for this notebook.
