import random
from statistics import mean, stdev
from math import sqrt

def run_experiment(num_samples, func):
    """
    Run a Monte Carlo experiment with the given function.

    Args:
        num_samples (int): Number of samples to generate.
        func (function): Function that takes no arguments and returns a float.

    Returns:
        tuple: Tuple containing the mean and standard deviation of the results.
    """
    results = [func() for _ in range(num_samples)]
    return mean(results), stdev(results)

def confidence_interval(mean, std_dev, num_samples, confidence=0.95):
    """
    Calculate a confidence interval for the given data.

    Args:
        mean (float): Mean of the data.
        std_dev (float): Standard deviation of the data.
        num_samples (int): Number of samples used to calculate the mean and standard deviation.
        confidence (float, optional): Confidence level. Defaults to 0.95.

    Returns:
        tuple: Tuple containing the lower and upper bounds of the confidence interval.
    """
    z_score = stats.norm.ppf(1 - (1 - confidence) / 2)
    margin_of_error = z_score * std_dev / sqrt(num_samples)
    return mean - margin_of_error, mean + margin_of_error

def run_monte_carlo_experiment(func, num_samples=1000):
    """
    Run a Monte Carlo experiment with the given function and calculate a confidence interval.

    Args:
        func (function): Function that takes no arguments and returns a float.
        num_samples (int, optional): Number of samples to generate. Defaults to 1000.

    Returns:
        tuple: Tuple containing the mean, standard deviation, and confidence interval of the results.
    """
    mean, std_dev = run_experiment(num_samples, func)
    lower_bound, upper_bound = confidence_interval(mean, std_dev, num_samples)
    return mean, std_dev, (lower_bound, upper_bound)

# Example usage:
def example_func():
    return random.random() * 100

mean, std_dev, ci = run_monte_carlo_experiment(example_func)
print(f"Mean: {mean}, Standard Deviation: {std_dev}, Confidence Interval: {ci}")
