from ChomskyNormalForm import Grammar
import unittest

class TestGrammar(unittest.TestCase):
    def setUp(self):
        self.g = Grammar()
        self.P1, self.P2, self.P3, self.P4, self.P5 = self.g.Return_Productions()

    def test_remove_epsilon(self):
        # Test Remove_Epsilon method
        expected_result = {'S': ['aB', 'bA', 'a', 'Sa', 'bBA', 'b', '', 'bA', 'b', 'bS', 'aD'], 'A': ['Sa', 'bBA', 'b', '', 'bA', 'b', 'bS', 'aD'], 'B': ['b', 'bS', 'aD'], 'D': ['AA'], 'C': ['Ba', 'a']}
        self.assertEqual(self.P1, expected_result)

    def test_eliminate_unit_prod(self):
        # Test Eliminate_Unit_Prod method
        expected_result = {'S': ['aB', 'bA', 'a', 'Sa', 'bBA', 'b', '', 'bA', 'b', 'bS', 'aD'], 'A': ['Sa', 'bBA', 'b', '', 'bA', 'b', 'bS', 'aD'], 'B': ['b', 'bS', 'aD'], 'D': ['AA'], 'C': ['Ba', 'a']}
        self.assertEqual(self.P2, expected_result)

    def test_eliminate_inaccesible(self):
        # Test Eliminate_Inaccesible_Symbols method
        expected_result = {'S': ['aB', 'bA', 'a', 'Sa', 'bBA', 'b', '', 'bA', 'b', 'bS', 'aD'], 'A': ['Sa', 'bBA', 'b', '', 'bA', 'b', 'bS', 'aD'], 'B': ['b', 'bS', 'aD'], 'D': ['AA']}
        self.assertEqual(self.P3, expected_result)

    def test_remove_nonprod(self):
        # Test Remove_Nonproductive method
        expected_result = {'S': ['aB', 'bA', 'a', 'Sa', 'bBA', 'b', '', 'bA', 'b', 'bS', 'aD'], 'A': ['Sa', 'bBA', 'b', '', 'bA', 'b', 'bS', 'aD'], 'B': ['b', 'bS', 'aD'], 'D': ['AA']}
        self.assertEqual(self.P4, expected_result)

    def test_obtain_cnf(self):
        # Test ObtainCNF method
        expected_result = {'S': ['CE', 'FG', 'a', 'HC', 'FI', 'b', 'JJ', 'FG', 'b', 'FH', 'CK'], 'A': ['HC', 'FI', 'b', 'JJ', 'FG', 'b', 'FH', 'CK'], 'B': ['b', 'FH', 'CK'], 'D': ['AA'], 'C': ['a'], 'E': ['B'], 'F': ['b'], 'G': ['A'], 'H': ['S'], 'I': ['BA'], 'J': [''], 'K': ['D']}
        self.assertEqual(self.P5, expected_result)


if __name__ == 'main':
    unittest.main()