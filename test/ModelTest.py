from unittest import TestCase
from graph.Node import Node

node = Node(1, (3.0, 1.0, 5.0))
node1 = Node(2, (0.0, 1.0, 5.0))


class TestMyNode(TestCase):

    def test_getAndSetKey(self):
        self.assertEqual(node.get_key(), 1)
        node.set_key(4)
        self.assertEqual(node.get_key(), 4)

    def test_getAndSetTag(self):
        node.set_tag(1)
        node1.set_tag(4)
        self.assertEqual(node.get_tag(), 1)
        self.assertEqual(node1.get_tag(), 4)

    def test_getAndSetWeight(self):
        node.set_Weight(5.67)
        node1.set_Weight(11.67)
        self.assertEqual(node.get_Weight(), 5.67)
        self.assertEqual(node1.get_Weight(), 11.67)

    def test_getAndSetPos(self):
        node.set_pos(1.0, 1.0)
        node1.set_pos(2.0, 2.0)
        self.assertEqual(node.get_pos(), (1.0, 1.0, 0.0))
        self.assertEqual(node1.get_pos(), (2.0, 2.0, 0.0))

    def test_getAndSetFrom(self):
        node.setFrom(node1)
        node1.setFrom(node)
        self.assertEqual(node.isFrom(), node1)
        self.assertEqual(node1.isFrom(),node)

    def test_getAndSetVisit(self):
        node.setVisit(True)
        node1.setVisit(False)
        self.assertEqual(node.isVisited(), True)
        self.assertEqual(node1.isVisited(), False)