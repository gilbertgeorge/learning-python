import math
import argparse


def get_nominal_interest(rate, periods):
    return rate / (periods * 100)


def get_number_payments(loan_principal, monthly_payment, loan_interest):
    nominal_interest = get_nominal_interest(loan_interest, 12)
    base = monthly_payment / (monthly_payment - nominal_interest * loan_principal)
    number = math.log(base, 1 + nominal_interest)
    # years = math.floor(math.ceil(number) / 12)
    # remaining_months = math.ceil(number) % 12
    months_left = math.ceil(number)
    return months_left


def print_period(months_left):
    years = math.floor(math.ceil(months_left) / 12)
    remaining_months = math.ceil(months_left) % 12
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


def get_overpayment(loan_principal, number_of_periods, payment):
    return abs(int(loan_principal - (number_of_periods * payment)))


def get_differentiated_payments(loan_principal, number_of_periods, loan_interest):
    nominal_interest = get_nominal_interest(loan_interest, 12)
    total_payment = 0
    for current_period in range(1, number_of_periods+1):
        current_payment = math.ceil((loan_principal / number_of_periods) + nominal_interest *
                                    (loan_principal - ((loan_principal * (current_period - 1)) / number_of_periods)))
        total_payment += current_payment
        print(f'Month {current_period}: payment is {current_payment}')
    overpayment = int(abs(loan_principal - total_payment))
    print(f'\nOverpayment = {overpayment}')


def loan_calculator():
    invalid_params_msg = 'Incorrect parameters'
    parser = argparse.ArgumentParser(description="This program calculates interest based on "
                                                 "type and presence of provided arguments.")
    parser.add_argument("-t", "--type", choices=['diff', 'annuity'],
                        help="Type must be one specified from list")
    parser.add_argument("--principal", default=None,
                        help="Used for calculations of both types of payment. You can get its value if you know"
                             " the interest, annuity payment, and number of months.")
    parser.add_argument("--periods", default=None,
                        help="Denotes the number of months needed to repay the loan. It's calculated based on the"
                             " interest, annuity payment, and principal.")
    parser.add_argument("--interest", default=None,
                        help="Specified without a percent sign. Note that it can accept a floating-point value. "
                             "The loan calculator can't calculate the interest, so it must always be provided.")
    parser.add_argument("--payment", default=None,
                        help="The monthly payment amount.")
    args = parser.parse_args()

    if args.type == 'annuity':
        if not args.interest:
            print(invalid_params_msg)
        if args.principal and args.payment and args.interest:
            loan_principal = float(args.principal)
            monthly_payment = int(args.payment)
            loan_interest = float(args.interest)
            if loan_principal < 0 or monthly_payment < 0 or loan_interest < 0:
                print(invalid_params_msg)
            else:
                number_of_periods = get_number_payments(loan_principal, monthly_payment, loan_interest)
                print(f'It will take {print_period(number_of_periods)} to repay this loan!')
                print(f'Overpayment = {get_overpayment(loan_principal, number_of_periods, monthly_payment)}')
        if args.principal and args.periods and args.interest:
            loan_principal = float(args.principal)
            number_of_periods = int(args.periods)
            loan_interest = float(args.interest)
            if loan_principal < 0 or number_of_periods < 0 or loan_interest < 0:
                print(invalid_params_msg)
            else:
                monthly_payment = get_monthly_payment(loan_principal, number_of_periods, loan_interest)
                print(f'Your annuity payment = {monthly_payment}!')
                print(f'Overpayment = {get_overpayment(loan_principal, number_of_periods, monthly_payment)}')
        if args.payment and args.periods and args.interest:
            annuity_amount = float(args.payment)
            number_of_periods = int(args.periods)
            loan_interest = float(args.interest)
            if annuity_amount < 0 or number_of_periods < 0 or loan_interest < 0:
                print(invalid_params_msg)
            else:
                loan_principal = get_loan_principal(annuity_amount, number_of_periods, loan_interest)
                print(f'Your loan principal = {loan_principal}!')
                print(f'Overpayment = {get_overpayment(loan_principal, number_of_periods, annuity_amount)}')
    elif args.type == 'diff':
        if args.payment:
            print(invalid_params_msg)
        elif args.principal and args.periods and args.interest:
            loan_principal = float(args.principal)
            number_of_periods = int(args.periods)
            loan_interest = float(args.interest)
            if loan_principal < 0 or number_of_periods < 0 or loan_interest < 0:
                print(invalid_params_msg)
            else:
                get_differentiated_payments(loan_principal, number_of_periods, loan_interest)
        else:
            print(invalid_params_msg)
    else:
        print(invalid_params_msg)


if __name__ == '__main__':
    loan_calculator()
