import json


def convert_json():
    movie_dict = {
        "movies": [
            {
                "title": "Inception",
                "director": "Christopher Nolan",
                "year": 2010
            },
            {
                "title": "The Lord of the Rings: The Fellowship of the Ring",
                "director": "Peter Jackson",
                "year": 2001
            },
            {
                "title": "Parasite",
                "director": "Bong Joon Ho",
                "year": 2019
            }
        ]
    }
    # with open("supplemental\\movies.json", "w") as json_file:
    #     json.dump(movie_dict, json_file)
    # json_str = json.dumps(movie_dict)
    json_str = json.dumps(movie_dict, indent=4)
    print(json_str)


def decode_json():
    with open("../supplemental/movies.json", "r") as json_file:
        movie_dict_from_json = json.load(json_file)

    print(movie_dict_from_json)


if __name__ == '__main__':
    # convert_json()
    decode_json()
