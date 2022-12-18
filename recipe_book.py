import argparse

# # python .\recipe_book.py --salt --ingredient_1=1
# parser.add_argument("-i1", "--ingredient_1")  # optional argument
# # parser.add_argument("ingredient_1")           # positional argument
#
# # python .\recipe_book.py 1 --salt
# parser.add_argument("--salt", action="store_true")
#
# # python .\recipe_book.py --pepper 'True'
# parser.add_argument("--pepper", default=False)
#
# # python .\recipe_book.py --ingredient_2='carrot'
# # python .\recipe_book.py -i2='onion'
# parser.add_argument("-i2", "--ingredient_2",
#                     choices=["pasta", "rice", "potato", "onion",
#                              "garlic", "carrot", "soy_sauce", "tomato_sauce"],
#                     help="You need to choose only one ingredient from the list.")

# print(f'parser: {parser}; arguments: {parser.parse_args()}')
#
# args = parser.parse_args()
# print(f'ingredient_2: {args.ingredient_2}')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This program prints recipes "
                                                 "consisting of the ingredients you provide.")

    parser.add_argument("-i1", "--ingredient_1", choices=["pasta", "rice", "potato",
                                                          "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                        help="You need to choose only one ingredient from the list.")
    parser.add_argument("-i2", "--ingredient_2", choices=["pasta", "rice", "potato",
                                                          "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                        help="You need to choose only one ingredient from the list.")
    parser.add_argument("-i3", "--ingredient_3", choices=["pasta", "rice", "potato",
                                                          "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                        help="You need to choose only one ingredient from the list.")
    parser.add_argument("-i4", "--ingredient_4", choices=["pasta", "rice", "potato",
                                                          "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                        help="You need to choose only one ingredient from the list.")
    parser.add_argument("-i5", "--ingredient_5", choices=["pasta", "rice", "potato",
                                                          "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                        help="You need to choose only one ingredient from the list.")

    parser.add_argument("--salt", action="store_true",
                        help="Specify if you'd like to use salt in your recipe.")
    parser.add_argument("--pepper", default="False",
                        help="Change to 'True' if you'd like to use pepper in your recipe.")

    args = parser.parse_args()

    ingredients = [args.ingredient_1, args.ingredient_2, args.ingredient_3,
                   args.ingredient_4, args.ingredient_5]
    if args.salt:
        ingredients.append("salt")
    if args.pepper == "True":
        ingredients.append("pepper")

    # python .\recipe_book.py -i1 rice -i2 onion -i3 garlic -i4 carrot -i5 tomato_sauce --salt
    print(f"The ingredients you provided are: {ingredients}")

