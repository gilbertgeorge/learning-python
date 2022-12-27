import requests


def make_request(url):
    # http://api.quotable.io/quotes/-4WQ_JwFWI (valid)
    # http://api.quotable.io/quotes/asdfgh (invalid)
    # http://api.quotable.io/authors (invalid)
    KEY_TO_SEARCH = 'content'
    invalid_message = 'Invalid quote resource!'
    r = requests.get(url)
    if r:
        json_response = r.json()
        if KEY_TO_SEARCH in json_response:
            print(json_response[KEY_TO_SEARCH])
        else:
            print(invalid_message)
    else:
        print(invalid_message)


def scrape():
    print('Input the URL:')
    user_url = input()
    make_request(user_url)


if __name__ == '__main__':
    scrape()
