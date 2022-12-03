import csv
import sys
import re
import datetime
from fpdf import FPDF

class Payslip():
    def __init__(self):
        self.name = "Casey Payslip"

    def __str__(self):
        return f"""
        {self.name}
        Date = {self.date}
        ${self.deposit}
        """

    def get_deposit(self):
       self.deposit = int(input("Deposit: "))

    def get_deposit_date(self):
        datestr = input("Enter date of shift (YYYY-MM-DD): ")
        self.date = datetime.date.fromisoformat(datestr)
    
    def get_tax(self):
        ...


def main():
    
    payslip = Payslip()

    payslip.get_deposit()
    payslip.get_deposit_date()

    print(payslip)




if __name__ == '__main__':
    main()