import unittest
from algorithm import *


class MyTestCase(unittest.TestCase):

    def test_checking_connectivity(self):
        # test as described in documentation
        # graph depicted on fig. 6 in documentation
        full_adjacency_matrix_sample = np.array([
            [-1,-1, 0, 0],  # a
            [-1, 0,-1, 0],  # b
            [ 0,-1,-1, 0],  # c
            [ 0, 0, 0,-1],  # d
            [ 0, 0, 0,-1]   # e
        ])
        labels = ["a", "b", "c", "d", "e"]
        weights = [1, 1, 1, 1, 1]
        graph = PartiallyDirectedGraph(full_adjacency_matrix_sample, labels, weights)
        # graph.plot()
        self.assertEqual(False, graph.is_connected())

    def test_transforming_g_to_g1(self):
        # graph depicted on fig. 2 in documentation
        full_adjacency_matrix_sample = np.array([
            [ 1, 0,-1],  # a
            [-1,-1, 0],  # b
            [ 0,-1, 1]   # c
        ])
        labels = ["a", "b", "c"]
        weights = [1, 1, 1]
        g = PartiallyDirectedGraph(full_adjacency_matrix_sample, labels, weights)
        # g.plot()
        g1 = G1(g)
        # g1.plot(edge_label="transformed")
        # g1.plot(edge_label="directed")
        g1_expected = Graph([(0,1), (1,2), (2,0)], directed=True)
        g1_expected.vs["label"] = labels
        g1_expected.es["weight"] = weights
        self.assertEqual(g1_expected.get_adjacency(), g1.graph.get_adjacency())


if __name__ == '__main__':
    unittest.main()
