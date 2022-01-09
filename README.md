# finalOPPtask - Pokemon game

Name : Tal Ornan ID: 209349356<br />
Name : Tzach Itshak Ofir ID: 208062943<br />


![pokemon-1591427_1920](https://user-images.githubusercontent.com/76403961/148697885-be26bf80-4612-46c3-9d91-225fc1206909.jpg)

Welcome to the OPP_4  project!
Here we explained our implementation to the weighted and directed graph class.

### ****To implement the project we use on 3 classes****
#### **Node:**

This class represents the nodes of our graph.

**Fields:**

1.key- Integer representing the node id.<br />
2.location- holding the pos the node gets from JSON or, if not, get random pos.<br />
3.numOfOutEdge- hold the numbers of edges connected from node_id.<br /> 
4.numOfInEdge- hold the numbers of edges connected into node_id.<br /> 
5.from_node- hold the key Node we visited before the current Node.<br />
6.visit- if we visited in the current node we get true, else, we get false.<br />
7.Weight- hold the weight of edges we had visited until getting the current node.<br />

**Functions**<br />

1.setters/getters.<br />
2. equal, hash, repr - use in tests.<br />

#### **DiGraph<br />**
This class represents the graph.<br />

**Fields:**<br />
1.dict_vertices- A dictionary of all vertices -> {key: Node}.<br />
2.dict_edges_in- A dictionary of all-in edges -> {key: source's node id, value: edge's weight}.<br />
3.dict_edge_out- A dictionary of all-out edges -> {key: destination's node id, value: edge's weight}.<br />
4.MC- graph's mode counter.<br />
5.num vertices- hold the number of vertices in the graph<br />
6.numOfEdge- hold the number of edge's in the graph<br />

**Functions**<br />
1.getNode - get vertex by id.<br />
2.v_size - the number of vertices in this graph.<br />
3.e_size - Returns the number of edges in this graph.<br />
4.get_mc - Returns the current version of this graph.<br />
5.get_all_v - Return the graph's node's dictionary.<br />
6.add_edge -  Adds an edge to the graph.<br />
7.remove_edge - Removes a node from the graph.<br />
8.add_node - Adds a node to the graph.<br />
9.remove_node - emoves a node from the graph.<br />
10.all_in_edges_of_node -  return a dictionary of all the nodes connected to (into) node_id each node is represented using a pair (other_node_id, weight).<br />
11.all_out_edges_of_node -  return a dictionary of all the nodes connected from node_id, each node is represented using a pair.<br />

#### **GraphAlgo<br />**
This class represents the algorithms applicable to DiGraph.<br />

**Fields:**<br />
1.graph - DiGraph.<br />

****Functions****<br />

**functions from interface:**<br />

1.get_graph - return: the directed graph on which the algorithm works on.<br />
2.load_from_json - Loads a graph from a JSON file.<br />
3.save_to_json -  Saves the graph in JSON format to a file.<br />
4.shortest_path - Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm.<br />
5. TSP - Finds the shortest path that visits all the nodes in the list.<br />
6.CenterPoint -  Finds the node that has the shortest distance to its farthest node.<br />
7.plot_graph -  Plots the graph. If the nodes have a position, the nodes will be placed there.<br />

**functions to help implement the interface  :**<br />

1.Dijkstra - see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm.<br />
2.isConnected - Returns true if and only if (iff) there is a valid path from each node to each other node.<br />
3.getMinWeightFromDic -get the min weight of node - use in Dijkstra algorithem.<br />
4.BFS - see https://en.wikipedia.org/wiki/Breadth-first_search.<br />
5.is strongly connected - check if the graph is connected- every vertex can go to all the other vertexes.<br />

## ****GraphAlgo implemtion****

#### ****isConnected(self):**** <br />
1.Scanners the node key in the vertex dictionary.<br />
2.Scanners the node value in the vertex dictionary.<br />
3.check if the cur vertex is strongly connected to the other's vertexes. if there is some vertex that isn't, return false. else ' return true.<br />

#### ****shortest_path:****<br />
first, we define a new list to contain the path and then check if src and dest are equals, if yes, add src value to the path list and return the list and 0. if not we checked if src and dest Exist. then we activate the Dijkstra function to get the shortest path and add the path we get to the path list. In the end, we add src to the path and reverse the path list. then we return to the path. if there is a path between src and dest the function returns the path if not the return - float('inf'), empty path list.<br />

#### ****TSP:****
first, define a new list to contain the path. then go over the Vertices of the graph and update visit status to false. if there is no value's in cities return an empty list. next, we define a new node as the value of the cities list in the first place and update the prev visit status to true. in addition, I add to TCP prev cities in the first place/ To the end, I go over cities size and go in the Shortest Path from prev to curr vertex, I update all the vertex I pass as visited and not go over them again.<br />

#### ****CenterPoint:****
first, define a new dictionary - distance check if the graph is connected, if not the distance dictionary is empty. then go over Vertices value and add for every vertex its distance from all the other vertexes. The next step is to put the distance in the distance dictionary in the place of the current vertex key  And to end I check what node has the shortest path from the other by comparing the values is in the dictionary.<br />

#### ****Dijkstra:****
Based on this https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm. To create this method we used dictionary structure and add to it all the nodes in the graph in their node key place. in addition, we update their Weight to INF their From field to None and their visit status to False.  then update src weight to 0 and put src in the dictionary.
then while there is a vertex in the new dictionary we check if we visited if not delete it from the dictionary and go over the edges from the cur vertex.
and made Dijkstra calculate to find the shortest path.<br />


#### ****BFS:****
Based on this https://en.wikipedia.org/wiki/Breadth-first_search. an iterative method to implement BFS. In the first node, I change the visit statue to True and add this node to the new List. and then if the List is not empty I remove the last element and go over is NeighborsNode if I do not visit some of their neighbor I change is visit status to true and add it to List.<br />

#### ****isStronglyConnected:**** 
Used the bfs algo in recursive to validate there is a path to each node.<br />
