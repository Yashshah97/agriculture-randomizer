import unittest
from agriculture_randomizer import core

class TestCoreModule(unittest.TestCase):

    def test_experiment_run(self):
        experiment = core.Experiment("Test Experiment")
        def func():
            return 42
        experiment.run(func)
        self.assertGreater(len(experiment.results), 0)

    def test_confidence_interval(self):
        experiment = core.Experiment("Test Experiment")
        def func():
            return 42
        for _ in range(1000):
            result = func()
            experiment.results.append(result)
        ci = experiment.confidence_interval(0.05)
        self.assertIsInstance(ci, tuple)

    def test_experiment_runner(self):
        runner = core.ExperimentRunner()
        experiment1 = core.Experiment("Experiment 1")
        experiment2 = core.Experiment("Experiment 2")
        runner.add_experiment(experiment1)
        runner.add_experiment(experiment2)
        ci_list = runner.run_experiments()
        self.assertEqual(len(ci_list), len(runner.experiments))

if __name__ == "__main__":
    unittest.main()
