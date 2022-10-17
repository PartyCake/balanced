import unittest
from main import calculation_by_period


class Test(unittest.TestCase):
    def test_IsInstance(self):
        self.assertIsInstance(calculation_by_period(start_date='2021-01-20', end_date='2021-12-24', filename='test'), list)

    def test_len(self):
        self.assertIs(len(calculation_by_period(start_date='2021-01-20', end_date='2021-12-24', filename='test')), 22)

    def test_types(self):
        result = calculation_by_period(start_date='2021-01-20', end_date='2021-12-24', filename='test')
        for i in result:
            self.assertIsInstance(i, float)

    def test_data(self):
        data = [4.0, 5.0, 5.333333333333333, 5.333333333333333, 6.5, 6.8, 5.333333333333333,
                4.333333333333333, 6.0, 7.5, 6.5, 2.0, 7.75, 6.0, 6.4, 7.0, 5.75, 5.0,
                5.857142857142857, 5.6, 6.166666666666667, 5.285714285714286]

        self.assertTrue(calculation_by_period(start_date='2021-01-20', end_date='2021-12-24', filename='test') == data)


if __name__ == '__main__':
    unittest.main()
