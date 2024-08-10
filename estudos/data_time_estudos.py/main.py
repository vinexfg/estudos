from datatimeES import Loan


print('Welcome to fathers loan')
print()
print('select one of the options below')

while True:
    options = input('[1]simular emprestimo [2]add customer to bank [3]exit')
    if options == '1':
        value_loan = float(input('Value: '))
        Loan.loan_time(value_loan)