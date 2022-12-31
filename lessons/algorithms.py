from collections import deque


def index_of_max(numbers):
    index = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[index]:
            index = i

    return index


def aver(sent):
    for sym in ['!', '?', ';', '.', '"', "'"]:
        sent = sent.replace(sym, '')

    words = sent.split()
    total = 0
    for word in words:
        total = total + len(word)

    if len(words) != 0:
        result = total / len(words)
    else:
        result = 0
    return result


def the_stack():
    my_stack = []
    my_stack.append('Out')
    my_stack.append('First')
    my_stack.append('In')
    my_stack.append('Last')

    print(my_stack)  # ['Out', 'First', 'In', 'Last']

    print(my_stack.pop())  # Last
    print(my_stack.pop())  # In
    print(my_stack.pop())  # First
    print(my_stack.pop())  # Out


def deque_stack():
    my_stack = deque()

    my_stack.append('k')
    my_stack.append('c')
    my_stack.append('a')
    my_stack.append('t')
    my_stack.append('s')

    print(my_stack.pop())  # 's'
    print(my_stack.pop())  # 't'
    print(my_stack.pop())  # 'a'
    print(my_stack.pop())  # 'c'
    print(my_stack.pop())  # 'k'


def stack_flip():
    n = int(input())
    my_stack = deque()
    for _ in range(n):
        my_stack.append(input())
    for _ in range(len(my_stack)):
        print(my_stack.pop())


def book_stack():
    actions = int(input())
    book_pile = deque()
    read_books = deque()
    for _ in range(actions):
        user_input = input()
        user_command = user_input.split(" ", 1)
        if user_command[0] == 'BUY':
            book_pile.append(user_command[1])
        elif user_command[0] == 'READ':
            read_books.append(book_pile.pop())

    for book in read_books:
        print(book)


def candy_stack():
    number_of_actions = int(input())
    list_of_actions = []
    candy_bag = deque(['Daim'])
    for _ in range(number_of_actions):
        user_input = input()
        list_of_actions.append(user_input)
    for action in list_of_actions:
        user_command = action.split(" ", 1)
        if user_command[0] == 'TAKE':
            if len(candy_bag) > 0:
                print(candy_bag.pop())
            else:
                print('We are out of candies :(')
        elif user_command[0] == 'PUT':
            candy_bag.append(user_command[1])


def deck():
    my_deque = deque()
    my_deque.append('Middle')
    my_deque.append('Right')
    my_deque.appendleft('Left')
    print(my_deque)
    # deque(['Left', 'Middle', 'Right'])
    print(my_deque.pop())
    # Right
    print(my_deque)
    # deque(['Left', 'Middle'])
    print(my_deque.popleft())
    # Left
    print(my_deque)
    # deque(['Middle'])


def deck_as_queue():
    my_queue = deque()
    my_queue.appendleft('First')
    my_queue.appendleft('In')
    my_queue.appendleft('First')
    my_queue.appendleft('Out')
    print(my_queue)
    # Deque(['Out', 'First', 'In', 'First'])
    print(my_queue.pop())
    # First
    print(my_queue.pop())
    # In
    print(my_queue.pop())
    # First
    print(my_queue.pop())
    # Out


if __name__ == '__main__':
    # number_list = [1, 3, 5, 6, 7, 10, 2, 4, 6]
    # print(index_of_max(number_list))
    # sentence = input()
    # print(aver(sentence))
    # deque_stack()
    # stack_flip()
    # book_stack()
    candy_stack()
