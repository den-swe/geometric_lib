import unittest
from square import area
from square import perimeter

class SquareTestCases(unittest.TestCase):
    """
    Тесты для функций area и perimeter из модуля square
    """

    def test_area_positive_int_side(self):
        """Тест площади с целой положительной стороной"""
        result = area(3)
        self.assertEqual(result, 9)

    def test_area_positive_float_side(self):
        """Тест площади с дробной положительной стороной"""
        result = area(2.5)
        self.assertAlmostEqual(result, 6.25)

    def test_area_zero_side(self):
        """Тест площади с нулевой стороной"""
        with self.assertRaises(ValueError):
            area(0)

    def test_area_negative_int_side(self):
        """Тест площади с целой отрицательной стороной"""
        with self.assertRaises(ValueError):
            area(-3)

    def test_area_negative_float_side(self):
        """Тест площади с дробной отрицательной стороной"""
        with self.assertRaises(ValueError):
            area(-2.5)

    def test_area_string_input(self):
        """Тест площади со строковым вводом"""
        with self.assertRaises(TypeError):
            area("3")

    def test_area_bool_input(self):
        """Тест площади с булевым вводом"""
        with self.assertRaises(TypeError):
            area(True)

    def test_area_none_input(self):
        """Тест площади с None"""
        with self.assertRaises(TypeError):
            area(None)

    def test_perimeter_positive_int_side(self):
        """Тест периметра с целой положительной стороной"""
        result = perimeter(3)
        self.assertEqual(result, 12)

    def test_perimeter_positive_float_side(self):
        """Тест периметра с дробной положительной стороной"""
        result = perimeter(2.5)
        self.assertAlmostEqual(result, 10.0)

    def test_perimeter_zero_side(self):
        """Тест периметра с нулевой стороной"""
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_perimeter_negative_int_side(self):
        """Тест периметра с целой отрицательной стороной"""
        with self.assertRaises(ValueError):
            perimeter(-3)

    def test_perimeter_negative_float_side(self):
        """Тест периметра с дробной отрицательной стороной"""
        with self.assertRaises(ValueError):
            perimeter(-2.5)

    def test_perimeter_string_input(self):
        """Тест периметра со строковым вводом"""
        with self.assertRaises(TypeError):
            perimeter("3")

    def test_perimeter_list_input(self):
        """Тест периметра со списком"""
        with self.assertRaises(TypeError):
            perimeter([24, 56, 10])

if __name__ == '__main__':
    unittest.main()
