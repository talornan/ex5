class Node(object):
    random_key = 0

    def __init__(self, key: int = random_key, location: tuple = None):
        self.key = key
        self.location = location
        self.numOfOutEdge = 0
        self.numOfInEdge = 0
        self.tag = -1
        self.from_node = None
        self.visit = False
        self.Weight = 0

    def __str__(self):
        """
        returns: A String representing the vertex.
        """
        return f"str: id:{self.key}, pos:{self.location}"

    def __repr__(self):
        """
        returns: A String representing the vertex.
        """
        return f"{self.key}: |edges out| {self.numOfOutEdge} |edges in| {self.numOfInEdge}"

    def __hash__(self):
        return hash((self.location, self.tag, self.from_node, self.visit, self.numOfInEdge, self.numOfOutEdge, self.key,
                     self.wight))

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        elif self is other:
            return True
        else:
            return self.key == other.key and self.Weight == other.Weight and self.tag == other.tag and self.location == other.location and self.numOfInEdge == other.numOfInEdge and self.numOfOutEdge == other.numOfOutEdge and self.from_node == other.from_node and self.visit == other.visit

    def get_key(self) -> int:
        """
        returns: The key of the vertex.
        """
        return self.key

    def set_key(self, key: int):
        """
        parm: set a new key to vertex .
        """
        self.key = key

    def get_tag(self) -> int:
        return self.tag

    def set_tag(self, tag):
        self.tag = tag

    def isFrom(self):
        """
        returns: The what is the last vertex we visit before visit in current vertex.
        note: Will be used later in the Dijkstra algorithm.
        """
        return self.from_node

    def setFrom(self, from_node):
        """
        parm: set a new node to vertex represent is parents.
        note: Will be used later in the dijkstra algorithm.
        """
        self.from_node = from_node

    def get_pos(self) -> [tuple]:
        """"
        returns: The position (x and y) of the vertex.
        """
        return self.location

    def set_pos(self, x, y):
        """
        parm: A new position of the vertex.
        """
        self.location = (x, y, 0.0)

    def isVisited(self) -> bool:
        """"
        returns: The answer if we had visited in the current vertex or not.
        note: Will be used in AlgoGraph class.
        """
        return self.visit

    def setVisit(self, visit):
        self.visit = visit

    def get_Weight(self) -> [float]:
        """"
        returns: The Weight  of the vertex.
        """
        return self.Weight

    def set_Weight(self, Weight: float):
        """"
         parm: A new Weight of the vertex.
         """
        self.Weight = Weight
