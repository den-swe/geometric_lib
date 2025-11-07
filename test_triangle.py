import unittest
from triangle import area
from triangle import perimeter

class TriangleTestCases(unittest.TestCase):
    """
    Тесты для функций area и perimeter из модуля triangle
    """

    def test_area_positive_int_sides(self):
        """Тест площади с целыми положительными сторонами"""
        result = area(3, 4)
        self.assertEqual(result, 6.0)

    def test_area_positive_float_sides(self):
        """Тест площади с дробными положительными сторонами"""
        result = area(2.5, 3.5)
        self.assertAlmostEqual(result, 4.375)

    def test_area_zero_base(self):
        """Тест площади с нулевым основанием"""
        with self.assertRaises(ValueError):
            area(0, 5)

    def test_area_zero_height(self):
        """Тест площади с нулевой высотой"""
        with self.assertRaises(ValueError):
            area(5, 0)

    def test_area_negative_base(self):
        """Тест площади с отрицательным основанием"""
        with self.assertRaises(ValueError):
            area(-3, 4)

    def test_area_negative_height(self):
        """Тест площади с отрицательной высотой"""
        with self.assertRaises(ValueError):
            area(3, -4)

    def test_area_string_input(self):
        """Тест площади со строковым вводом"""
        with self.assertRaises(TypeError):
            area("3", "4")

    def test_area_none_input(self):
        """Тест площади с None"""
        with self.assertRaises(TypeError):
            area(None, 5)

    def test_perimeter_positive_int_sides(self):
        """Тест периметра с целыми положительными сторонами"""
        result = perimeter(3, 4, 5)
        self.assertEqual(result, 12)

    def test_perimeter_positive_float_sides(self):
        """Тест периметра с дробными положительными сторонами"""
        result = perimeter(2.5, 3.5, 4.5)
        self.assertAlmostEqual(result, 10.5)

    def test_perimeter_zero_side(self):
        """Тест периметра с нулевой стороной"""
        with self.assertRaises(ValueError):
            perimeter(0, 4, 5)

    def test_perimeter_negative_side(self):
        """Тест периметра с отрицательной стороной"""
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_perimeter_string_input(self):
        """Тест периметра со строковым вводом"""
        with self.assertRaises(TypeError):
            perimeter("3", "4", "5")

if __name__ == '__main__':
    unittest.main()
