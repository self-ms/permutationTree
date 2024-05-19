import unittest
from permutationsHandler import ListPermutations

class TestListPermutations(unittest.TestCase):
    def test_permutation_iterator(self):
        elements = ['A', 'B', 'C']
        expected_permutations = [
            ['A', 'B', 'C'],
            ['A', 'C', 'B'],
            ['B', 'A', 'C'],
            ['B', 'C', 'A'],
            ['C', 'A', 'B'],
            ['C', 'B', 'A']
        ]
        perm_graph = ListPermutations(elements)
        permutations = list(perm_graph.permutation_iterator())
        self.assertEqual(permutations, expected_permutations)


if __name__ == '__main__':
    unittest.main()
