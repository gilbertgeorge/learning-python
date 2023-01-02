def slicing_py():
    fib_nums = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    print(fib_nums[0])
    print(fib_nums[-1])
    print(fib_nums[2:5])

    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    print(planets[2:7:2])

    # sequence[:end]  # elements from start to end-1
    # sequence[start:]  # elements from start to the last element
    # sequence[:]  # the full copy of the sequence
    # sequence[::step]  # every element with a given step


def some_more_examples():
    # slicing from the start
    snakes = ['python', 'cobra', 'viper']
    print(snakes[:2])  # ['python', 'cobra']
    print(snakes[0][:2])  # py

    # slicing to the end
    powers_of_two = [1, 2, 4, 8, 16, 32, 64, 128]
    print(powers_of_two[4:])  # [16, 32, 64, 128]

    # slicing in steps of 3
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    print(colors[::3])  # ['red', 'green', 'violet']

    # copy a list
    sheep = ['Dolly', 'Polly', 'Molly']
    cloned_sheep = sheep[:]  # ['Dolly', 'Polly', 'Molly']


def secret_message():
    string = "no clouds here to spy on pets"
    # every fifth letter, reversed
    secret = string[::5][::-1]
    print(secret)


if __name__ == '__main__':
    # slicing_py()
    # some_more_examples()
    secret_message()
