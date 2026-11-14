"""
Module for crop yield and soil sensor data handling and simulation.

This module provides classes and functions for generating random crop yields and
soil sensor readings. It also includes methods for calculating confidence intervals.
"""

import math
from typing import List, Tuple

class Crop:
    """Class representing a crop with its characteristics."""

    def __init__(self, name: str, mean_yield: float, std_dev: float):
        """
        Initialize a Crop object.

        Args:
            name (str): Name of the crop.
            mean_yield (float): Mean yield of the crop in kg/ha.
            std_dev (float): Standard deviation of the yield in kg/ha.
        """
        self.name = name
        self.mean_yield = mean_yield
        self.std_dev = std_dev

    def simulate_yield(self, num_samples: int) -> List[float]:
        """
        Simulate crop yields using a normal distribution.

        Args:
            num_samples (int): Number of samples to generate.

        Returns:
            List[float]: A list of simulated crop yields.
        """
        return [self.mean_yield + self.std_dev * math.sqrt(-2 * math.log(x)) for x in
               [math.sin(2 * math.pi * i / num_samples) for i in range(num_samples)]]

class SoilSensor:
    """Class representing a soil sensor with its characteristics."""

    def __init__(self, name: str, mean_reading: float, std_dev: float):
        """
        Initialize a SoilSensor object.

        Args:
            name (str): Name of the sensor.
            mean_reading (float): Mean reading of the sensor in units.
            std_dev (float): Standard deviation of the reading in units.
        """
        self.name = name
        self.mean_reading = mean_reading
        self.std_dev = std_dev

    def simulate_reading(self, num_samples: int) -> List[float]:
        """
        Simulate soil sensor readings using a normal distribution.

        Args:
            num_samples (int): Number of samples to generate.

        Returns:
            List[float]: A list of simulated soil sensor readings.
        """
        return [self.mean_reading + self.std_dev * math.sqrt(-2 * math.log(x)) for x in
               [math.sin(2 * math.pi * i / num_samples) for i in range(num_samples)]]

def calculate_confidence_interval(data: List[float], confidence_level: float = 0.95) -> Tuple[float, float]:
    """
    Calculate a confidence interval for the mean of a dataset.

    Args:
        data (List[float]): A list of numbers.
        confidence_level (float): The desired confidence level (default is 0.95).

    Returns:
        Tuple[float, float]: A tuple containing the lower and upper bounds of the confidence interval.
    """
    n = len(data)
    mean = sum(data) / n
    std_err = math.sqrt(sum((x - mean) ** 2 for x in data) / (n - 1))
    margin_of_error = math.sqrt(n) * std_err / math.sqrt(n - 1)
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return lower_bound, upper_bound

# Example usage:
crop = Crop("Wheat", 1000.0, 50.0)
soil_sensor = SoilSensor("pH Sensor", 6.5, 0.2)

simulated_yields = crop.simulate_yield(1000)
simulated_readings = soil_sensor.simulate_reading(1000)

lower_bound, upper_bound = calculate_confidence_interval(simulated_yields)
print(f"Confidence interval for wheat yield: ({lower_bound}, {upper_bound})")
