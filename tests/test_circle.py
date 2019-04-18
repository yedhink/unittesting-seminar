import unittest
from math import pi
from areas import area


class TestCircleArea(unittest.TestCase):
    def test_radii(self):
        radii = [0, 1, 0.1, 2+3j, -7, True, "Hello"]
        for radius in radii:
            result = area.circle_area(radius)
            self.assertEqual(result, pi * (radius**2), "Unexpected area")

    def on_negative_radius(self):
        self.assertRaises(ValueError, area.circle_area, -1)

    def on_other_types(self):
        self.assertRaises(TypeError, area.circle_area, True)
