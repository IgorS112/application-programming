class FinanceTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, date, amount):
        year, month, day = map(int, [date[:4], date[4:6], date[6:]])
        self.expenses.setdefault(year, {}).setdefault(month, {})
        self.expenses[year][month][day] = self.expenses[year][month].get(day, 0) + amount

    def calculate_yearly_expenses(self, year):
        return sum(sum(month.values()) for month in self.expenses.get(year, {}).values())

    def calculate_monthly_expenses(self, year, month):
        return sum(self.expenses.get(year, {}).get(month, {}).values())

tracker = FinanceTracker()


