import unittest
import math
from circle import area
from circle import perimeter

class CircleTestCases(unittest.TestCase):
    """
    Тесты для функций area и perimeter из модуля circle
    """

    def test_area_positive_int_radius(self):
        """Тест площади с целым положительным радиусом"""
        result = area(3)
        self.assertAlmostEqual(result, math.pi * 3 * 3)

    def test_area_positive_float_radius(self):
        """Тест площади с дробным положительным радиусом"""
        result = area(2.5)
        self.assertAlmostEqual(result, math.pi * 2.5 * 2.5)

    def test_area_zero_radius(self):
        """Тест площади с нулевым радиусом"""
        result = area(0)
        self.assertEqual(result, 0)

    def test_area_negative_radius(self):
        """Тест площади с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            area(-3)

    def test_area_string_input(self):
        """Тест площади со строковым вводом"""
        with self.assertRaises(TypeError):
            area("3")

    def test_perimeter_positive_int_radius(self):
        """Тест периметра с целым положительным радиусом"""
        result = perimeter(3)
        self.assertAlmostEqual(result, 2 * math.pi * 3)

    def test_perimeter_positive_float_radius(self):
        """Тест периметра с дробным положительным радиусом"""
        result = perimeter(2.5)
        self.assertAlmostEqual(result, 2 * math.pi * 2.5)

    def test_perimeter_zero_radius(self):
        """Тест периметра с нулевым радиусом"""
        result = perimeter(0)
        self.assertEqual(result, 0)

    def test_perimeter_negative_radius(self):
        """Тест периметра с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            perimeter(-3)

if __name__ == '__main__':
    unittest.main()
