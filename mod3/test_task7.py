import unittest
from mod2.task7 import FinanceTracker

class TestFinanceTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = FinanceTracker()

    def test_add_expense(self):
        # Пэто добавить расход
        self.tracker.add_expense('20240101', 100)
        self.assertEqual(self.tracker.calculate_yearly_expenses(2024), 100)

    def test_calculate_yearly_expenses(self):
        # это за год
        self.tracker.add_expense('20240101', 100)
        self.tracker.add_expense('20240201', 200)
        self.assertEqual(self.tracker.calculate_yearly_expenses(2024), 300)

    def test_calculate_monthly_expenses(self):
        # это за месяц
        self.tracker.add_expense('20240101', 100)
        self.tracker.add_expense('20240115', 50)
        self.tracker.add_expense('20240130', 50)
        self.assertEqual(self.tracker.calculate_monthly_expenses(2024, 1), 200)

if __name__ == '__main__':
    unittest.main()
