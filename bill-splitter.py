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


def bill_splitter():
    print('Enter the number of friends joining (including you):')
    number_of_people = int(input())
    if number_of_people < 1:
        print('No one is joining for the party')
    else:
        guest_list = get_names(number_of_people)
        guest_list = get_bill_amount(guest_list)
        print(guest_list)


if __name__ == '__main__':
    bill_splitter()
