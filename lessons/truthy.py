real_password = "12345"


def say_hello(name):
    default_name = 'Anonymous'
    print(f'Hello, {name or default_name}!')


def wrong_password(password):
    return (password == "" or (not password and real_password)) or password != real_password


def solve():
    print(wrong_password("12345"))
    print(wrong_password(None))


if __name__ == '__main__':
    # say_hello('Bob')
    # say_hello('')
    solve()
