import requests


def google_search(query, num):
    r = requests.get('https://google.com/search',
                     params={'q': query, 'num': num})
    return r


if __name__ == '__main__':
    # r = requests.get('https://requests.readthedocs.io/en/master/')
    # print(r)
    # print(r.status_code)
    # print(r.text)
    # print(r.encoding)
    # print(r.headers)
    # print(r.headers['date'])
    search_google_for_python = google_search('python', 1)
    print(search_google_for_python.text)
    print(search_google_for_python.url)
