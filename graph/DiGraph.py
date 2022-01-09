from Node import Node


class DiGraph(object):

    def __init__(self):
        self.dict_vertices = {}
        self.dict_edges_in = {}
        self.dict_edge_out = {}
        self.MC = 0
        self.numOfVertices = 0
        self.numOfEdge = 0

    def __repr__(self):
        return f"Graph: |V|={self.numOfVertices} , |E|={self.numOfEdge}"

    def getNode(self, Node_Key):
        """
        returns: the vertex by getting is id/key from vertices dictionary.
        """
        if Node_Key in self.dict_vertices:
            return self.dict_vertices[Node_Key]

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.numOfVertices

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.numOfEdge

    def get_all_v(self) -> dict:
        """
        return a dictionary of all the nodes in the Graph, each node is represented using a pair
        (node_id, node_data)
         """
        return self.dict_vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        if id1 not in self.dict_edges_in.keys():
            return {}
        return self.dict_edges_in.get(id1)

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.MC

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        if id1 not in self.dict_edge_out.keys():
            return {}
        return self.dict_edge_out.get(id1)

    def get_all_edges(self) -> dict:

        return self.dict_edge_out;

    def add_edge(self, id1: int, id2: int, Weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 == id2:
            return False
        if id2 not in self.dict_vertices:
            return False
        if id1 not in self.dict_vertices:
            return False
        if id2 in self.all_out_edges_of_node(id1).keys():
            return False
        if id1 not in self.dict_edge_out.keys():
            self.dict_edge_out[id1] = {id2: Weight}
        else:
            self.dict_edge_out[id1].update({id2: Weight})
        if id2 not in self.dict_edges_in.keys():
            self.dict_edges_in[id2] = {id1: Weight}
        else:
            self.dict_edges_in[id2].update({id1: Weight})
        self.MC += 1
        self.numOfEdge += 1
        self.getNode(id2).numOfInEdge += 1
        self.getNode(id1).numOfOutEdge += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
         @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if node_id in self.dict_vertices.keys():
            return False
        self.dict_vertices[node_id] = Node(node_id, pos)
        self.MC += 1
        self.numOfVertices += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if node_id not in self.dict_vertices.keys():
            return False
        if node_id in self.dict_edge_out.keys():
            keyValue = list(self.all_out_edges_of_node(node_id).keys())
            for edge in keyValue:
                self.remove_edge(node_id, edge)
            self.dict_edge_out.pop(node_id)
        if node_id in self.dict_edges_in.keys():
            keyValue = list(self.all_in_edges_of_node(node_id).keys())
            for edge in keyValue:
                self.remove_edge(edge, node_id)
            self.dict_edges_in.pop(node_id)
        del self.dict_vertices[node_id]
        self.MC += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
         Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 not in self.dict_vertices:
            return False
        if node_id1 not in self.dict_vertices:
            return False
        if node_id1 == node_id2:
            return False
        if node_id2 in self.all_out_edges_of_node(node_id1).keys():
            self.getNode(node_id1).numOfOutEdge -= 1
            self.getNode(node_id2).numOfInEdge -= 1
            self.dict_edge_out[node_id1].pop(node_id2)
            self.dict_edges_in[node_id2].pop(node_id1)
        self.MC += 1
        self.numOfEdge -= 1
        return True
