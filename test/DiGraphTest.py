from unittest import TestCase
from graph.DiGraph import *


class TestDiGraph(TestCase):
    def create_graph(self):
        graph = DiGraph()
        graph.add_node(0, (1.19589389346247, 1.10152879327731))
        graph.add_node(1, (2.19589389346247, 2.10152879327731))
        graph.add_node(2, (3.19589389346247, 3.10152879327731, 0.0))
        graph.add_node(3, (4.19589389346247, 4.10152879327731))
        graph.add_node(4, (5.19589389346247, 5.10152879327731))
        graph.add_node(5, (6.19589389346247, 6.10152879327731))
        return graph

    def test_getNode(self):
        graph = self.create_graph()
        self.assertEqual(graph.getNode(2), Node(2, (3.19589389346247, 3.10152879327731, 0.0)))

    def test_v_size(self):
        graph = self.create_graph()

        self.assertEqual(graph.v_size(), 6)

    def test_e_size(self):
        graph = self.create_graph()

        graph.add_edge(2, 3, 3.6)
        graph.add_edge(2, 4, 4.1)
        self.assertEqual(graph.e_size(), 2)

    def test_get_mc(self):
        graph = self.create_graph()

        self.assertEqual(graph.get_mc(), 6)
        graph.add_edge(2, 3, 3.6)
        graph.add_edge(2, 4, 4.1)
        self.assertEqual(graph.get_mc(), 8)

    def test_add_edge(self):
        graph = self.create_graph()

        graph.add_edge(2, 3, 3.6)
        graph.add_edge(2, 4, 4.1)
        self.assertEqual(graph.all_out_edges_of_node(2)[3], 3.6)
        self.assertEqual(graph.all_out_edges_of_node(2)[4], 4.1)

    def test_add_node(self):
        graph = self.create_graph()

        self.assertEqual(graph.get_all_v()[0], Node(0, (1.19589389346247, 1.10152879327731)))

    def test_remove_node(self):
        graph = self.create_graph()

        self.assertEqual(True, graph.remove_node(0))

    def test_remove_edge(self):
        graph = self.create_graph()

        self.assertEqual(True, graph.remove_edge(2, 4))
        self.assertEqual(True, graph.remove_edge(2, 3))

    def test_get_all_v(self):
        graph = self.create_graph()

        graph.remove_node(0)
        graph.remove_node(1)
        graph.remove_node(2)
        graph.remove_node(3)
        self.assertEqual(graph.get_all_v(), {4: Node(4, (5.19589389346247, 5.10152879327731)),
                                             5: Node(5, (6.19589389346247, 6.10152879327731))})

    def test_all_in_edges_of_node(self):
        graph = self.create_graph()

        graph.add_edge(2, 3, 3.6)
        graph.add_edge(2, 4, 4.1)
        self.assertEqual(graph.all_in_edges_of_node(3), {2: 3.6})
        self.assertEqual(graph.all_in_edges_of_node(4), {2: 4.1})

    def test_all_out_edges_of_node(self):
        graph = self.create_graph()

        graph.add_edge(2, 3, 3.6)
        graph.add_edge(2, 4, 4.1)
        self.assertEqual(graph.all_out_edges_of_node(2), {3: 3.6, 4: 4.1})