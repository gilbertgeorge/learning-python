import math


def number_of_payments(loan_principal):
    monthly_payment = int(input('Enter the monthly payment:'))
    payments = math.ceil(loan_principal / monthly_payment)
    if payments == 1:
        print(f'It will take {payments} month to repay the loan')
    else:
        print(f'It will take {payments} months to repay the loan')


def monthly_payments(loan_principal):
    months = int(input('Enter the number of months:'))
    monthly_payment = loan_principal / months
    remainder = monthly_payment % 1
    if remainder == 0:
        print(f'Your monthly payment = {int(monthly_payment)}')
    else:
        initial_payments = math.ceil(monthly_payment)
        last_payment = loan_principal - (months - 1) * initial_payments
        print(f'Your monthly payment = {initial_payments} and the last payment = {last_payment}')


def loan_calculator():
    loan_principal = int(input('Enter the loan principal:'))
    print('What do you want to calculate?')
    print('type "m" - for number of monthly payments,')
    print('type "p" - for the monthly payment:')
    calculation_type = input()
    if calculation_type == 'm':
        number_of_payments(loan_principal)
    if calculation_type == 'p':
        monthly_payments(loan_principal)


if __name__ == '__main__':
    loan_calculator()
