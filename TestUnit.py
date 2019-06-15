import unittest
import CustomFunctions as cufu
import pandas as pd
from datetime import datetime as dt

class TestTimeMethods(unittest.TestCase):
	def test_time_stamp_to_date(self):
        self.assertEqual(cufu.time_stamp_to_date("2014-01-01 05:22:01"), dt(2014, 1, 1, 5, 22, 1))
        self.assertEqual(cufu.time_stamp_to_date("2015-10-17 07:34:11"), dt(2015, 10, 17, 7, 34, 11))
        self.assertRaises(ValueError, cufu.time_stamp_to_date, "2015-10-sfdf17 07:34:11")
    def test_time_stamp_to_week(self):
        self.assertEqual(cufu.time_stamp_to_week("2014-01-01 05:22:01"), "2014 Week: 1")
        self.assertEqual(cufu.time_stamp_to_week("2015-10-17 07:34:11"), "2015 Week: 42")
        self.assertRaises(ValueError, cufu.time_stamp_to_week, "2015-10-sfdf17 07:34:11")
    def test_get_min(self):
        d = {'col1': [1, 2, 3, 4 ,5], 'col2': [7, -1, 8, -5, 6]}
        df = pd.DataFrame(data=d)
        self.assertEqual(cufu.get_min(df["col1"], 0), 1)
        self.assertEqual(cufu.get_min(df["col2"], 0), 6)
        self.assertEqual(cufu.get_min(df["col2"], -10), -5)
if __name__ == '__main__':
    unittest.main()