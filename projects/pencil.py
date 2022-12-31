def get_bot_move(pencils_left):
    target = (pencils_left - 1) % 4
    if target == 0:
        # print('unfortunate')
        target = 1
    return target


def get_valid_remove_pencils(pencils_left):
    valid_remove_pencils = [1, 2, 3]
    while True:
        pencils = input()
        try:
            int_pencils = int(pencils)
            if int_pencils in valid_remove_pencils:
                if pencils_left - int_pencils < 0:
                    print('Too many pencils were taken')
                else:
                    return int_pencils
            else:
                print("Possible values: '1', '2' or '3'")
        except ValueError:
            print("Possible values: '1', '2' or '3'")


def get_valid_starting_pencils():
    while True:
        pencils = input()
        try:
            int_pencils = int(pencils)
            if int_pencils > 0:
                return int_pencils
            else:
                print('The number of pencils should be positive')
        except ValueError:
            print('The number of pencils should be numeric')


def get_valid_player(valid_players):
    while True:
        player = input()
        if player in valid_players:
            return player
        else:
            valid_player_string = ' and '.join(f"'{w}'" for w in valid_players)
            print(f'Choose between {valid_player_string}')


def pencil():
    valid_players = ['John', 'Jack']
    print('How many pencils would you like to use:')
    number_of_pencils = get_valid_starting_pencils()
    print(f'Who will be the first ({", ".join(valid_players)}):')
    player = get_valid_player(valid_players)
    if player in valid_players:
        player_index = valid_players.index(player)
        while number_of_pencils > 0:
            print('|' * number_of_pencils)
            print(f"{valid_players[player_index]}'s turn:")
            if valid_players[player_index] == 'Jack':
                # print('bot move')
                remove_pencils = get_bot_move(number_of_pencils)
                print(remove_pencils)
            else:
                remove_pencils = get_valid_remove_pencils(number_of_pencils)
            number_of_pencils -= remove_pencils
            player_index = (player_index + 1) % 2
        print(f'{valid_players[player_index]} won!')


if __name__ == '__main__':
    pencil()
