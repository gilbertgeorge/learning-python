import requests
from bs4 import BeautifulSoup


def make_request(url):
    invalid_message = 'Invalid movie page!'
    res = requests.get(url)
    if res:
        soup = BeautifulSoup(res.content, 'html.parser')
        title = soup.find('h1')
        description = soup.find('span', {'data-testid': 'plot-l'})
        if title and description:
            result = dict({'title': title.text, 'description': description.text})
            print(f'{result}')
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
