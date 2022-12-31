def set_union():
    democrats = {'Kennedy', 'Obama'}
    republicans = {'Trump', 'Lincoln'}
    presidents = democrats.union(republicans)
    print(presidents)


def or_operator():
    democrats = {'Kennedy', 'Obama'}
    republicans = {'Trump', 'Lincoln'}
    presidents = democrats | republicans
    also_presidents = democrats.union(republicans)
    print(presidents == also_presidents)


def set_update():
    ghostbusters = {'Peter', 'Raymond', 'Egon'}
    soldiers = {'Winston'}
    secretaries = {'Janine'}
    # or update
    ghostbusters |= soldiers
    ghostbusters.update(secretaries)
    print(ghostbusters)


def set_intersection():
    light_side = {'Obi-Wan', 'Anakin'}
    dark_side = {'Palpatine', 'Anakin'}
    both_sides = light_side.intersection(dark_side)
    print(both_sides)
    print(light_side & dark_side)


def intersection_update():
    creatures = {'human', 'rabbit', 'cat'}
    pets = {'rabbit', 'cat'}
    creatures.intersection_update(pets)
    print(creatures)
    beasts = {'crocodile', 'cat'}
    creatures &= beasts
    print(creatures)


def set_difference():
    painters = {'Klimt', 'Michelangelo', 'Picasso'}
    ninja_turtles = {'Michelangelo', 'Leonardo'}
    print(painters.difference(ninja_turtles))
    print(painters - ninja_turtles)


def difference_update():
    criminals = {'Al Capone', 'Blackbeard', 'Bonnie and Clyde'}
    gangsters = {'Al Capone'}
    pirates = {'Blackbeard'}

    criminals.difference_update(gangsters)
    criminals -= pirates
    print(criminals)


def operators_vs_methods():
    santa_claus_sound = set('ho ho ho')
    pirate_sound = 'yo ho ho'
    ho_sound = santa_claus_sound.intersection(pirate_sound)
    print(ho_sound)
    # print(santa_claus_sound & pirate_sound)

    # sets are within a container
    languages = [{'c', 'c++', 'python'}, {'python', 'javascript'}, {'python', 'java'}]
    the_best = set.intersection(*languages)
    print(the_best)


def rivers_difference():
    rivers = set(input().split())
    states = set(input().split())
    print(rivers.difference(states))


def all_students():
    gryffindor = set(input().split())
    ravenclaw = set(input().split())
    slytherin = set(input().split())
    hufflepuff = set(input().split())
    print(gryffindor | ravenclaw | slytherin | hufflepuff)


def country_alike():
    eugene = set(input().split())
    rose = set(input().split())
    only_one = (eugene | rose) - (eugene & rose)
    print(only_one)


def method_testing():
    a = set("my code is brOKen")
    b = "i'm not OK with that"
    c = a.intersection(b)
    print(c)


def planet_intersection():
    set_1 = set(input().split())
    set_2 = set(input().split())
    set_3 = set(input().split())
    print(set_1 & set_2 & set_3)


if __name__ == '__main__':
    # applies to frozenset as well

    # set_union()
    # or_operator()
    # set_update()
    # set_intersection()
    # intersection_update()
    # set_difference()
    difference_update()
    operators_vs_methods()

    # rivers_difference()
    # all_students()
    # country_alike()

    # method_testing()
    planet_intersection()

