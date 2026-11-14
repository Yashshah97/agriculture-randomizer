import unittest
from agriculture_randomizer import models

class TestModels(unittest.TestCase):

    def test_crop(self):
        crop = models.Crop('Wheat', 10.0, 2.0)
        self.assertEqual(crop.name, 'Wheat')
        self.assertEqual(crop.yield_mean, 10.0)
        self.assertEqual(crop.yield_stddev, 2.0)

    def test_sensor_type(self):
        self.assertEqual(models.SensorType.pH.value, 1)
        self.assertEqual(models.SensorType.temperature.value, 2)
        self.assertEqual(models.SensorType.moisture.value, 3)

    def test_soil_sensor_reading(self):
        reading = models.SoilSensorReading(models.SensorType.pH, 7.0)
        self.assertEqual(reading.sensor_type, models.SensorType.pH)
        self.assertEqual(reading.value, 7.0)

    def test_farm(self):
        crop1 = models.Crop('Wheat', 10.0, 2.0)
        crop2 = models.Crop('Corn', 8.0, 3.0)
        farm = models.Farm('My Farm', [crop1, crop2], [])
        self.assertEqual(farm.name, 'My Farm')
        self.assertEqual(len(farm.crops), 2)

    def test_experiment_config(self):
        config = models.ExperimentConfig(100, 95.0)
        self.assertEqual(config.num_simulations, 100)
        self.assertEqual(config.confidence_interval_percentage, 95.0)

if __name__ == '__main__':
    unittest.main()
