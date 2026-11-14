"""
Core Monte Carlo engine logic and data structures.

This module defines the core functionality of the Agriculture Monte Carlo Engine,
including the experiment runner and confidence interval calculations.
"""

import math
from typing import Callable, List, Tuple

class Experiment:
    """Represents a single Monte Carlo experiment."""

    def __init__(self, name: str):
        self.name = name
        self.results = []

    def run(self, func: Callable) -> None:
        """
        Run the given function multiple times and store the results.

        :param func: The function to run.
        """
        for _ in range(1000):  # Number of iterations is arbitrary
            result = func()
            self.results.append(result)

    def confidence_interval(self, alpha: float) -> Tuple[float, float]:
        """
        Calculate a confidence interval using the results.

        :param alpha: The desired confidence level (e.g. 0.05 for 95% CI).
        :return: A tuple containing the lower and upper bounds of the CI.
        """
        mean = sum(self.results) / len(self.results)
        std_dev = math.sqrt(sum((x - mean) ** 2 for x in self.results) / (len(self.results) - 1))
        z_score = math.sqrt(alpha * (1 - alpha) / len(self.results))  # Approximation
        interval = 1.96 * std_dev / math.sqrt(len(self.results))  # 95% CI approximation
        return mean - interval, mean + interval

class ExperimentRunner:
    """Runs multiple experiments and calculates confidence intervals."""

    def __init__(self):
        self.experiments: List[Experiment] = []

    def add_experiment(self, experiment: Experiment) -> None:
        """
        Add an experiment to the runner.

        :param experiment: The experiment to add.
        """
        self.experiments.append(experiment)

    def run_experiments(self) -> List[Tuple[float, float]]:
        """
        Run all experiments and return a list of confidence intervals.

        :return: A list of tuples containing the lower and upper bounds of each CI.
        """
        results = []
        for experiment in self.experiments:
            ci = experiment.confidence_interval(0.05)
            results.append(ci)
        return results
