import unittest

from billing import calc_fee, used_minutes


class TestBilling(unittest.TestCase):
    def test_used_minutes(self):
        self.assertEqual(used_minutes("10:00", "11:30"), 90)

    def test_fee_exact_unit(self):
        self.assertEqual(calc_fee("小会議室A", 60), 1200)


if __name__ == "__main__":
    unittest.main()
