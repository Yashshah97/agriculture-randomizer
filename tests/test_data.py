import unittest
from agriculture_randomizer import data

class TestData(unittest.TestCase):

    def test_crop_simulation(self):
        crop = data.Crop('Test Crop', 1000, 50)
        yields = crop.simulate_yield(10)
        self.assertEqual(len(yields), 10)

    def test_soil_sensor_simulation(self):
        sensor = data.SoilSensor('Test Sensor', 500, 20)
        readings = sensor.simulate_reading(10)
        self.assertEqual(len(readings), 10)

    def test_calculate_confidence_interval(self):
        data_list = [1.0, 2.0, 3.0, 4.0, 5.0]
        lower_bound, upper_bound = data.calculate_confidence_interval(data_list)
        self.assertGreater(lower_bound, -float('inf'))
        self.assertLess(upper_bound, float('inf'))

if __name__ == '__main__':
    unittest.main()
