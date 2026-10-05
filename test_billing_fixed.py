import unittest

from billing_fixed import calc_fee, used_minutes


class TestBilling(unittest.TestCase):
    def test_used_minutes(self):
        self.assertEqual(used_minutes("10:00", "11:30"), 90)

    def test_fee_exact_unit(self):
        self.assertEqual(calc_fee("小会議室A", 60), 1200)

    # Issue #1: 30分未満の端数は切り上げる
    def test_fee_rounds_up_70_minutes(self):
        self.assertEqual(calc_fee("中会議室B", 70), 3000)

    def test_fee_rounds_up_short_use(self):
        self.assertEqual(calc_fee("小会議室A", 20), 600)

    def test_fee_boundaries(self):
        self.assertEqual(calc_fee("小会議室A", 30), 600)
        self.assertEqual(calc_fee("小会議室A", 31), 1200)

    # Issue #2: 月額会員は10%引き
    def test_member_discount(self):
        self.assertEqual(calc_fee("中会議室B", 60, "member"), 1800)

    def test_visitor_has_no_discount(self):
        self.assertEqual(calc_fee("中会議室B", 60, "visitor"), 2000)


if __name__ == "__main__":
    unittest.main()
