import unittest
from extent import Extent


class TestExtent(unittest.TestCase):
    def test_can_parse(self):
        '''
        Test that it can be read correctly from a bbox string from the controller
        '''

        # Arrange
        my_string = "123.123,123.123,456.456,456.456"
        # Act
        extent = Extent.parse(my_string) 
        # Assert
        self.assertEqual(extent.min_x,123.123)
        self.assertEqual(extent.min_y,123.123)
        self.assertEqual(extent.max_x,456.456)
        self.assertEqual(extent.max_y,456.456)

    def test_raises_on_short_bbox_string(self):
        # Arrange
        my_string = "123.123,123.123,456.456"
        # Act
        # Assert
        with self.assertRaises(ValueError):
            extent = Extent.parse(my_string)


    def test_raises_on_stringy_bbox_string(self):
        # Arrange
        my_string = "123.123,123.123,456.456,abc"
        # Act
        # Assert
        with self.assertRaises(ValueError):
            extent = Extent.parse(my_string)

    def calculates_correct_area(self):
        extent = Extent(0,0,10,10)
        area = extent.calculate_area()
        self.assertEqual(100,area)

    def test_determines_too_large(self):
        extent_too_big = Extent(0,0,10,11)
        self.assertTrue(extent_too_big.exceeds_area(100))

    def test_determines_size_ok(self):
        extent_too_big = Extent(0,0,10,10)
        self.assertFalse(extent_too_big.exceeds_area(100))

    def throws_on_invalid_bbox(self):
        with self.assertRaises(ValueError):
            extent = Extent(10,10,0,0)

if __name__ == '__main__':
    unittest.main()