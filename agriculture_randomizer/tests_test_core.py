import unittest
from math import sqrt
from statistics import mean, stdev

def monte_carlo(num_samples):
    """Run a Monte Carlo experiment with the given number of samples."""
    return sum([1 for _ in range(num_samples) if 0.5 > abs(0 - 0.25)])

class TestMonteCarlo(unittest.TestCase):

    def test_zero_samples(self):
        """Test that running zero samples returns 0."""
        self.assertEqual(monte_carlo(0), 0)

    def test_one_sample(self):
        """Test that running one sample is deterministic."""
        self.assertEqual(monte_carlo(1), 1 if 0.5 > abs(0 - 0.25) else 0)

    def test_large_samples(self):
        """Test that the result converges to the expected value as samples increase."""
        num_samples = 100000
        result = monte_carlo(num_samples)
        self.assertAlmostEqual(result / num_samples, 1, places=2)

    def test_confidence_interval(self):
        """Test that the confidence interval is correct for a large number of samples."""
        num_samples = 10000
        results = [monte_carlo(100) for _ in range(num_samples)]
        mean_result = mean(results)
        stdev_result = stdev(results)
        ci_lower = mean_result - (1.96 * stdev_result / sqrt(num_samples))
        ci_upper = mean_result + (1.96 * stdev_result / sqrt(num_samples))
        self.assertGreaterEqual(ci_lower, 0.8)
        self.assertLessEqual(ci_upper, 1.2)

if __name__ == '__main__':
    unittest.main()
