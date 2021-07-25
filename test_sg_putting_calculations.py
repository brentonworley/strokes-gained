import unittest
import strokes_gained_calculations as sgc

class SimpleStrokesGainedTestCase(unittest.TestCase):
    """Tests for the simple numerical calc of SG putting"""

    def test_single_simple_strokes_gained(self):
        strokes_gained = sgc.calculate_strokes_gained(1.78, 1)
        self.assertEqual(strokes_gained, 0.78)

class StrokesGainedTestCase(unittest.TestCase):
    """Tests for the full SG Putting method"""

    def setUp(self):
        """Create some Strokes Gained input data for use in test methods"""
        self.sg_putting_test_ref_data = [
        {"distance": 2, "putts": 1.01}, {"distance": 3, "putts": 1.04}, {"distance": 4, "putts": 1.13}, {"distance": 5, "putts": 1.23}, {"distance": 6, "putts": 1.34}, {"distance": 7, "putts": 1.42}, {"distance": 8, "putts": 1.5}, {"distance": 9, "putts": 1.56}, {"distance": 10, "putts": 1.61}, {"distance": 15, "putts": 1.78}, {"distance": 20, "putts": 1.87}, {"distance": 30, "putts": 1.98}, {"distance": 40, "putts": 2.06}, {"distance": 50, "putts": 2.14}, {"distance": 60, "putts": 2.21}
        ]

        self.sg_putting_test_input_data = [
            {'distance': 1, 'putts': 1},
            {'distance': 5, 'putts': 1},
            {'distance': 27, 'putts': 1},
            {'distance': 10, 'putts': 2}
        ]

    def test_min_putt_distance(self):
        """Does the function handle a distance less than the min ref value"""
        strokes_gained = sgc.calculate_strokes_gained_putting(
            self.sg_putting_test_ref_data, self.sg_putting_test_input_data[0]
        )
        self.assertEqual(strokes_gained, 0.01)

    def test_exact_distance_match(self):
        """Does a simple exact match of distance return the expected value"""
        strokes_gained = sgc.calculate_strokes_gained_putting(
            self.sg_putting_test_ref_data, self.sg_putting_test_input_data[1]
        )
        self.assertEqual(strokes_gained, 0.23)

    def test_distance_in_between(self):
        """Does the calc work for a distance between reference numbers"""
        strokes_gained = sgc.calculate_strokes_gained_putting(
            self.sg_putting_test_ref_data, self.sg_putting_test_input_data[2]
        )
        #self.assertEqual(strokes_gained, 0.95)
        self.assertEqual(strokes_gained, 0.90)      

if __name__ == '__main__':
    unittest.main()
