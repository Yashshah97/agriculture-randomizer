import unittest
from agriculture_randomizer import tests_test_core

class TestTestCore(unittest.TestCase):

    def test_monte_carlo(self):
        """Test the monte_carlo function."""
        self.assertEqual(tests_test_core.monte_carlo(0), 0)
        self.assertEqual(tests_test_core.monte_carlo(1), 1 if 0.5 > abs(0 - 0.25) else 0)

    def test_MonteCarloTestCase(self):
        """Test the TestMonteCarlo class."""
        suite = unittest.TestLoader().loadTestsFromTestCase(tests_test_core.TestMonteCarlo)
        self.assertTrue(suite.countTestCases() == 4)

if __name__ == '__main__':
    unittest.main()
