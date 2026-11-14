from dataclasses import dataclass
import enum
from typing import Optional

@dataclass(frozen=True)
class Crop:
    """Domain object representing a crop."""
    name: str
    yield_mean: float
    yield_stddev: float

@enum.unique
class SensorType(enum.Enum):
    """Enum representing the type of sensor used for soil measurement."""
    pH = 1
    temperature = 2
    moisture = 3

@dataclass(frozen=True)
class SoilSensorReading:
    """Domain object representing a reading from a soil sensor."""
    sensor_type: SensorType
    value: float

@dataclass(frozen=True)
class Farm:
    """Domain object representing a farm with crop and soil data."""
    name: str
    crops: list[Crop]
    soil_sensor_readings: list[SoilSensorReading]

@dataclass(frozen=True)
class ExperimentConfig:
    """Configuration for the Monte Carlo experiment."""
    num_simulations: int
    confidence_interval_percentage: float

@dataclass(frozen=True)
class ExperimentResult:
    """Result of a Monte Carlo experiment, including mean and CI."""
    crop_name: str
    yield_mean: Optional[float]
    yield_ci_lower: Optional[float]
    yield_ci_upper: Optional[float]
