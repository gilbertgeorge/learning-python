import random


def get_names(number_of_people):
    print('Enter the name of every friend (including you), each on a new line:')
    guest_list = {}
    for person_input in range(0, number_of_people):
        new_guest = input()
        guest_list.update({new_guest: 0})
    return guest_list


def get_bill_amount(guest_list):
    print('Enter the total bill value:')
    bill_total = int(input())
    split_amount = bill_total / len(guest_list)
    guest_list = {guest: round(split_amount, 2) for guest in guest_list}
    return guest_list


def get_lucky_bill_amount(guest_list, lucky_one):
    bill_total = sum(guest_list.values())
    split_amount = bill_total / (len(guest_list) - 1)
    # guest_list = {guest: round(split_amount, 2) for guest in guest_list if guest != lucky_one}
    for guest in guest_list:
        if guest == lucky_one:
            guest_list[lucky_one] = 0
        else:
            guest_list[guest] = split_amount
    return guest_list


def lucky_feature(guest_list):
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    use_feature = input()
    if use_feature == 'Yes':
        lucky_one = random.choice(list(guest_list.keys()))
        print(f'{lucky_one} is the lucky one!')
        return lucky_one
    else:
        print(f'No one is going to be lucky')
        return None


def bill_splitter():
    print('Enter the number of friends joining (including you):')
    number_of_people = int(input())
    if number_of_people < 1:
        print('No one is joining for the party')
    else:
        guest_list = get_names(number_of_people)
        guest_list = get_bill_amount(guest_list)
        lucky_one = lucky_feature(guest_list)
        if lucky_one:
            guest_list = get_lucky_bill_amount(guest_list, lucky_one)
        print(guest_list)


if __name__ == '__main__':
    bill_splitter()
