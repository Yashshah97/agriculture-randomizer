import unittest
from agriculture_randomizer import utils

class TestUtils(unittest.TestCase):
    def test_calculate_mean(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(utils.calculate_mean(data), 3)

    def test_calculate_confidence_interval(self):
        data = [1, 2, 3, 4, 5]
        lower_bound, upper_bound = utils.calculate_confidence_interval(data)
        self.assertGreater(lower_bound, 2.5)
        self.assertLess(upper_bound, 3.5)

    def test_generate_random_data(self):
        data = [1, 2, 3, 4, 5]
        num_samples = 10
        random_data = utils.generate_random_data(data, num_samples)
        self.assertEqual(len(random_data), num_samples)
        for sample in random_data:
            self.assertEqual(len(sample), len(data))

    def test_run_monte_carlo_experiment(self):
        data = [1, 2, 3, 4, 5]
        num_samples = 10
        mean, std_dev = utils.run_monte_carlo_experiment(lambda x: sum(x) / len(x), data, num_samples)
        self.assertGreater(mean, 0)
        self.assertLess(std_dev, 1)

if __name__ == '__main__':
    unittest.main()
