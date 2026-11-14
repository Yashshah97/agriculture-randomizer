"""
Module: agriculture_randomizer.utils
=====================================

Helper functions for Monte Carlo engine operations.

This module provides utility functions for the Agriculture Monte Carlo Engine.
"""

import math
from typing import Callable, List

def calculate_mean(data: List[float]) -> float:
    """
    Calculate the mean of a list of numbers.

    Args:
        data (List[float]): A list of numbers.

    Returns:
        float: The mean of the input data.
    """
    return sum(data) / len(data)


def calculate_confidence_interval(data: List[float], confidence_level: float = 0.95) -> tuple:
    """
    Calculate a confidence interval for the population mean.

    Args:
        data (List[float]): A list of numbers.
        confidence_level (float, optional): The desired confidence level. Defaults to 0.95.

    Returns:
        tuple: A tuple containing the lower and upper bounds of the confidence interval.
    """
    n = len(data)
    mean = calculate_mean(data)
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in data) / (n - 1))
    margin_of_error = math.sqrt(n) * std_dev * math.sqrt(1 / n)
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error

    return lower_bound, upper_bound


def generate_random_data(data: List[float], num_samples: int) -> List[List[float]]:
    """
    Generate random samples from the input data.

    Args:
        data (List[float]): A list of numbers.
        num_samples (int): The number of random samples to generate.

    Returns:
        List[List[float]]: A list of lists, where each sublist contains a random sample.
    """
    return [sorted([random() for _ in range(len(data))]) for _ in range(num_samples)]


def run_monte_carlo_experiment(func: Callable[[List[float]], float], data: List[float], num_samples: int) -> tuple:
    """
    Run a Monte Carlo experiment using the input function and data.

    Args:
        func (Callable[[List[float]], float]): A function that takes in a list of numbers and returns a float.
        data (List[float]): A list of numbers.
        num_samples (int): The number of random samples to generate.

    Returns:
        tuple: A tuple containing the mean and standard deviation of the results.
    """
    results = [func(random_data) for random_data in generate_random_data(data, num_samples)]
    return calculate_mean(results), math.sqrt(sum((x - calculate_mean(results)) ** 2 for x in results) / (num_samples - 1))
