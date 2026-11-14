import unittest
from agriculture_randomizer import experiment
import random
import math
import statistics
import scipy.stats as stats

class TestExperiment(unittest.TestCase):

    def test_run_experiment(self):
        num_samples = 1000
        func = lambda: random.random() * 100
        mean, std_dev = experiment.run_experiment(num_samples, func)
        self.assertIsInstance(mean, float)
        self.assertIsInstance(std_dev, float)

    def test_confidence_interval(self):
        mean = 50.0
        std_dev = 10.0
        num_samples = 1000
        confidence = 0.95
        lower_bound, upper_bound = experiment.confidence_interval(mean, std_dev, num_samples, confidence)
        self.assertIsInstance(lower_bound, float)
        self.assertIsInstance(upper_bound, float)

    def test_run_monte_carlo_experiment(self):
        func = lambda: random.random() * 100
        mean, std_dev, ci = experiment.run_monte_carlo_experiment(func)
        self.assertIsInstance(mean, float)
        self.assertIsInstance(std_dev, float)
        self.assertIsInstance(ci, tuple)

if __name__ == '__main__':
    unittest.main()
