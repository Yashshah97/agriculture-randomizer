"""Smoke tests for data."""
import unittest

from agriculture_randomizer import data


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(data, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(data) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
