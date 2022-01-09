import heapq
import json
import heapq
import queue
import sys
from collections import defaultdict
from typing import List
import copy
import json
from igraph import *
import random
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from Node import Node


class GraphAlgo(object):
    def __init__(self, graph=None):
        self.graph: DiGraph = graph

    def isConnected(self):
        """
        Returns true if and only if (iff) there is a valid path from each node to each
        other node. NOTE: assume directional graph (all n*(n-1) ordered pairs).
        @return
        """
        for key in self.graph.get_all_v().keys():
            for node in self.graph.get_all_v().values():
                node.setVisit(False)
            if not self.isStronglyConnected(key):
                return False
        return True

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
         """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        # Opening JSON file
        f = open(file_name)

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        f.close()
        new_graph = DiGraph()

        for node in data["Nodes"]:
            if "pos" not in node:
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                z = random.randint(1, 10)
            else:
                pos = node["pos"].split(",")
                x = float(pos[0])
                y = float(pos[1])
                z = float(pos[2])
            id = node["id"]
            new_graph.add_node(id, (x, y, z))
        for edge in data["Edges"]:
            source = edge["src"]
            dest = edge["dest"]
            weight = edge["w"]
            new_graph.add_edge(source, dest, weight)

        self.graph = new_graph

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
         @return: True if the save was successful, False o.w.
         """
        nodes = []
        for node in self.graph.get_all_v().values():
            pos = node.get_pos()
            id = node.get_key()
            pos_str = str(pos[0]) + "," + str(pos[1]) + "," + str(pos[2])
            nodes.append({"id": id, "pos": pos_str})
        edges = []
        for source, edges_nei in self.graph.get_all_edges().items():
            for edge, weight in edges_nei.items():
                dest = edge
                weight = weight
                edges.append({"src": source, "dest": dest, "w": weight})

        res = {"Nodes": nodes, "Edges": edges}
        with open(file_name, 'w') as outfile:
            json.dump(res, outfile)
        outfile.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
         """
        path = []
        i = 1
        if id1 == id2:
            return 0, path
        if id1 not in self.graph.get_all_v().keys() or id2 not in self.graph.get_all_v().keys():
            return float('inf'), path
        src: Node = self.graph.getNode(id1)
        self.dijkstra(src)
        dest: Node = self.graph.getNode(id2)
        if dest.get_Weight() == float("inf"):
            return float("inf"), []
        while dest is not None:
            path.insert(i, dest.get_key())
            dest = self.graph.getNode(dest.isFrom())
            i += 1

        reversed_path = path[::-1]
        if id1 not in reversed_path:
            reversed_path.insert(0, id1)
        return self.graph.getNode(id2).get_Weight(), reversed_path

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        tcp = []
        for node in self.graph.dict_vertices.values():
            node.setVisit(False)
        if len(node_lst) == 0:
            return tcp
        prev: Node = self.graph.getNode(node_lst.pop(0))
        prev.setVisit(True)
        tcp.append(prev.get_key())
        for i in range(len(node_lst)):
            curr = node_lst[i]
            if not self.graph.getNode(curr).isVisited():
                graph_copy = copy.deepcopy(self.graph)
                algo_graph = GraphAlgo(graph_copy)
                res = algo_graph.shortest_path(prev.get_key(), curr)[1]
                for node in res:
                    node = self.graph.getNode(node)
                    if node.get_key() != prev.get_key():
                        node.setVisit(True)
                        tcp.append(node.get_key())
                prev = self.graph.getNode(curr)
        return tcp

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        if self.isConnected():
            distance = {}
            for node in self.graph.dict_vertices.values():
                copyNode = self.graph.getNode(node.get_key())
                dis = float('-inf')
                self.dijkstra(copyNode)
                for n in self.graph.dict_vertices.values():
                    shortest = n.get_Weight()
                    dis = max(dis, shortest)
                distance[node.get_key()] = dis
            min_key = None
            min_weight = float('inf')
            for key, weight in distance.items():
                if weight < min_weight:
                    min_key = key
                    min_weight = weight

            return min_key, min_weight

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        graph = Graph(directed=True)
        graph.add_vertices(len(self.graph.get_all_v().values()))
        graph.vs["name"] = [str(i) for i in range(len(self.graph.get_all_v().values()))]

        edges = []
        for source, edges_nei in self.graph.get_all_edges().items():
            for edge, weight in edges_nei.items():
                dest = edge
                edges.append((source, dest))
        graph.add_edges(edges)

        layout = graph.layout("kk")
        graph.vs["label"] = graph.vs["name"]

        plot(graph, layout=layout)
        pass

    def dijkstra(self, src: Node):
        """
        Based on this https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm.
         """
        dic = {}
        src.setVisit(True)
        src.setFrom(None)
        for node in self.graph.get_all_v().values():
            if node is not src:
                node.set_Weight(float('inf'))
                node.setFrom(None)
                node.setVisit(False)
                dic[node.get_key()] = node
        src.set_Weight(0)
        dic[src.get_key()] = src
        while len(dic) > 0:
            cur: Node = self.getMinWeightFromDic(dic)
            del dic[cur.get_key()]
            for nei, edge in self.graph.all_out_edges_of_node(cur.get_key()).items():
                neiNode: Node = self.graph.getNode(nei)
                distance: float = cur.get_Weight() + edge
                if neiNode.get_Weight() > distance:
                    neiNode.set_Weight(distance)
                    neiNode.setFrom(cur.get_key())

    def getMinWeightFromDic(self, dic):
        """
        get the min weight of node - use in Dijkstra algorithem.
        """
        minWeight = None
        for node in dic.values():
            if minWeight is None:
                minWeight = node
            else:
                if node.get_Weight() < minWeight.get_Weight():
                    minWeight = node
        return minWeight

    def BFS(self, vertex: Node):
        """
        Based on this https://en.wikipedia.org/wiki/Breadth-first_search. an iterative method to implement BFS
         """
        vertex.setVisit(True)
        bds_queue = [vertex]
        for node in self.graph.get_all_v().values():
            node.setVisit(False)
        while len(bds_queue) > 0:
            vertex = bds_queue.pop()
            for neighbour, Weight in self.graph.all_out_edges_of_node(vertex.get_key()).items():
                neighbour = self.graph.getNode(neighbour)
                if not neighbour.isVisited():
                    neighbour.setVisit(True)
                    bds_queue.insert(0, neighbour)

    def isStronglyConnected(self, key: int):
        """
         Used the bfs algo in recursive to validate there is a path to each node.
         """
        self.BFS(self.graph.getNode(key))
        for node in self.graph.get_all_v().values():
            if not node.isVisited():
                return False

        return True
