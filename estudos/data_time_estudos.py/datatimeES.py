from datetime import datetime
from dateutil.relativedelta import relativedelta
from dataclasses import dataclass

@dataclass
class Loan:
    amount: float
    interest_rate: float
    term_years: int
    
    
    def loan_time(self):
        total_amount = self.amount * (1 + self.interest_rate * self.term_years)
        return total_amount
    


