from unittest import TestCase
from graph.GraphAlgo import *

graph = DiGraph()
node2 = Node(2, (3.19589389346247, 3.10152879327731, 0.0))
graph.add_node(0, (1.19589389346247, 1.10152879327731, 0.0))
graph.add_node(1, (2.19589389346247, 2.10152879327731, 0.0))
graph.add_node(2)
graph.add_node(3, (4.19589389346247, 4.10152879327731, 0.0))
graph.add_node(4, (5.19589389346247, 5.10152879327731, 0.0))
graph.add_node(5, (6.19589389346247, 6.10152879327731, 0.0))


class test_GraphAlgo(TestCase):

    def test_shortest_path(self):

        graph.add_edge(0, 2, 1.0)
        graph.add_edge(0, 3, 2.0)
        graph.add_edge(3, 4, 3.0)
        graph.add_edge(0, 1, 4.0)
        graph.add_edge(1, 3, 5.0)
        graph.add_edge(1, 4, 6.0)
        graph.add_edge(1, 5, 7.0)
        graph.add_edge(2, 4, 8.0)
        graph.add_edge(3, 5, 9.0)
        graph.add_edge(4, 5, 10.0)
        graph.add_edge(4, 6, 11.0)
        graph.add_edge(4, 7, 12.0)
        graph.add_edge(5, 6, 13.0)
        graph.add_edge(6, 7, 14.0)
        graphAl = GraphAlgo(graph)
        lst = []
        self.assertEquals((0, lst), graphAl.shortest_path(0, 0))
        lst1 = []
        lst.append(1)
        lst2 = [0, 2]
        self.assertEqual((1.0, lst2), graphAl.shortest_path(0, 2))

    def test_center(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        for x in range(4):
            g.add_node(x)
        g.add_edge(0, 1, 5)
        g.add_edge(1, 2, 2)
        g.add_edge(1, 2, 8)
        g.add_edge(2, 3, 1)
        g.add_edge(1, 0, 1)
        g.add_edge(2, 0, 3)
        g.add_edge(3, 1, 3)
        ans = 1
        ans2 = ga.centerPoint()
        self.assertTrue(ans, ans2)

    def test_isConnectTrue(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        for x in range(4):
            g.add_node(x)
        g.add_edge(0, 1, 1.3118716362419698)
        g.add_edge(0, 2, 1.23)
        g.add_edge(1, 2, 2.13)
        g.add_edge(2, 3, 3.123)
        g.add_edge(1, 0, 3.123)
        g.add_edge(2, 0, 3.123)
        g.add_edge(3, 0, 3.123)
        self.assertEqual(True, ga.isConnected())

    def test_tcp(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        for x in range(8):
            g.add_node(x)

        g.add_edge(0, 1, 9.31)
        g.add_edge(1, 0, 6.3118)
        g.add_edge(1, 2, 5.3)
        g.add_edge(2, 1, 4.311)
        g.add_edge(2, 0, 7.311)
        g.add_edge(3, 2, 2.311)
        g.add_edge(3, 0, 1.31)
        g.add_edge(0, 4, 3.123)

        citis = []
        temp = []
        temp.append(2)
        temp.append(0)
        temp.append(4)
        citis.append(2)
        citis.append(4)

        self.assertEqual(temp, ga.TSP(citis))

    def test_loadjson(self):
        import os
        print(os.getcwd())
        g = DiGraph()
        ga = GraphAlgo(g)
        expected_file_name = os.getcwd() + "/data/A0.json"
        actual_file_name = os.getcwd() + "\data\Expected.json"
        ga.load_from_json(expected_file_name)
        ga.save_to_json(actual_file_name)

        expected_file = open(expected_file_name)
        expected = json.load(expected_file)
        actual_file = open(actual_file_name)
        actual = json.load(actual_file)

        a, b = json.dumps(actual, sort_keys=True), json.dumps(expected, sort_keys=True)
        self.assertEqual(a == b, True)

    def test_plot(self):
        import os
        print(os.getcwd())
        g = DiGraph()
        ga = GraphAlgo(g)
        expected_file_name = os.getcwd() + "/data/A0.json"
        actual_file_name = os.getcwd() + "/data/Expected.json"
        ga.load_from_json(expected_file_name)
