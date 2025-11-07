import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCases(unittest.TestCase):
    """
    Тесты для функций area и perimeter из модуля rectangle
    """

    def test_area_positive_int_sides(self):
        """Тест площади с целыми положительными сторонами"""
        result = area(3, 4)
        self.assertEqual(result, 12)

    def test_area_positive_float_sides(self):
        """Тест площади с дробными положительными сторонами"""
        result = area(2.5, 3.5)
        self.assertAlmostEqual(result, 8.75)

    def test_area_zero_side(self):
        """Тест площади с нулевой стороной"""
        with self.assertRaises(ValueError):
            area(0, 5)

    def test_area_negative_sides(self):
        """Тест площади с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            area(-3, 4)

    def test_area_string_input(self):
        """Тест площади со строковым вводом"""
        with self.assertRaises(TypeError):
            area("3", "4")

    def test_perimeter_positive_int_sides(self):
        """Тест периметра с целыми положительными сторонами"""
        result = perimeter(3, 4)
        self.assertEqual(result, 14)

    def test_perimeter_positive_float_sides(self):
        """Тест периметра с дробными положительными сторонами"""
        result = perimeter(2.5, 3.5)
        self.assertAlmostEqual(result, 12.0)

    def test_perimeter_zero_side(self):
        """Тест периметра с нулевой стороной"""
        with self.assertRaises(ValueError):
            perimeter(0, 5)

    def test_perimeter_negative_sides(self):
        """Тест периметра с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            perimeter(-3, 4)

if __name__ == '__main__':
    unittest.main()
