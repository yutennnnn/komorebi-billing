import unittest

from billing import calc_fee, used_minutes


class TestBilling(unittest.TestCase):
    def test_used_minutes(self):
        self.assertEqual(used_minutes("10:00", "11:30"), 90)

    def test_fee_exact_unit(self):
        self.assertEqual(calc_fee("小会議室A", 60), 1200)

    def test_fee_round_up_70min(self):
        self.assertEqual(calc_fee("中会議室B", 70), 3000)

    def test_fee_round_up_20min(self):
        self.assertEqual(calc_fee("小会議室A", 20), 600)

    def test_fee_boundary_30min(self):
        self.assertEqual(calc_fee("小会議室A", 30), 600)

    def test_fee_boundary_31min(self):
        self.assertEqual(calc_fee("小会議室A", 31), 1200)


if __name__ == "__main__":
    unittest.main()
