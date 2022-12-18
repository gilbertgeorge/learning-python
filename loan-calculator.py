import math


def get_nominal_interest(rate, periods):
    return rate / (periods * 100)


def get_number_payments(loan_principal, monthly_payment, loan_interest):
    nominal_interest = get_nominal_interest(loan_interest, 12)
    base = monthly_payment / (monthly_payment - nominal_interest * loan_principal)
    number = math.log(base, 1 + nominal_interest)
    years = math.floor(math.ceil(number) / 12)
    remaining_months = math.ceil(number) % 12
    if remaining_months == 0 and years > 1:
        return f'{years} years'
    elif remaining_months == 0 and years == 1:
        return f'{years} year'
    elif years > 1:
        if remaining_months > 1:
            return f'{years} years and {remaining_months} months'
        elif remaining_months == 1:
            return f'{years} years and {remaining_months} month'
    elif years == 1:
        if remaining_months > 1:
            return f'{years} year and {remaining_months} months'
        elif remaining_months == 1:
            return f'{years} year and {remaining_months} month'


def get_monthly_payment(loan_principal, number_of_periods, loan_interest):
    nominal_interest = get_nominal_interest(loan_interest, 12)
    # ((i*p)*(1+i)^n) / ((1+i)^n - 1)
    result = ((nominal_interest * loan_principal) * (1 + nominal_interest)**number_of_periods) / \
             ((1 + nominal_interest)**number_of_periods - 1)
    return math.ceil(result)


def get_loan_principal(annuity_amount, number_of_periods, loan_interest):
    nominal_interest = get_nominal_interest(loan_interest, 12)
    # P = A / ((i * (1+i)**n) / ((1+i)**n) - 1))
    result = annuity_amount / ((nominal_interest * (1 + nominal_interest)**number_of_periods) /
                               ((1 + nominal_interest)**number_of_periods - 1))
    return math.floor(result)


def loan_calculator():
    print('What do you want to calculate?')
    print('type "n" for number of monthly payments,')
    print('type "a" for annuity monthly payment amount,')
    print('type "p" for loan principal:')
    loan_principal_msg = 'Enter the loan principal:'
    monthly_payment_msg = 'Enter the monthly payment:'
    loan_interest_msg = 'Enter the loan interest:'
    periods_msg = 'Enter the number of periods:'
    annuity_msg = 'Enter the annuity payment:'
    calculation_type = input()

    if calculation_type == 'n':
        loan_principal = float(input(loan_principal_msg))
        monthly_payment = int(input(monthly_payment_msg))
        loan_interest = float(input(loan_interest_msg))
        result = get_number_payments(loan_principal, monthly_payment, loan_interest)
        print(f'It will take {result} to repay this loan!')
    if calculation_type == 'a':
        loan_principal = float(input(loan_principal_msg))
        number_of_periods = int(input(periods_msg))
        loan_interest = float(input(loan_interest_msg))
        result = get_monthly_payment(loan_principal, number_of_periods, loan_interest)
        print(f'Your monthly payment = {result}!')
    if calculation_type == 'p':
        annuity_amount = float(input(annuity_msg))
        number_of_periods = int(input(periods_msg))
        loan_interest = float(input(loan_interest_msg))
        result = get_loan_principal(annuity_amount, number_of_periods, loan_interest)
        print(f'Your loan principal = {result}!')


if __name__ == '__main__':
    loan_calculator()
