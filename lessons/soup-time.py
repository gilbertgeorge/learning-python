from bs4 import BeautifulSoup
import requests


def get_soup():
    res = requests.get('https://www.newsinlevels.com/products/albino-tortoise-level-1/')
    if res:
        soup = BeautifulSoup(res.content, 'html.parser')
        # print(soup.prettify())
        title = soup.find('title')
        print(f'Title: {title}')
        p_s = soup.find_all('p')
        print(f'number of paragraphs: {len(p_s)}')
        # print(f'Head: {soup.head}')

        paragraphs = soup.find_all('p', {'style': 'text-align: center;'})
        for p in paragraphs:
            print(f'Paragraph: {p.text}' + '\n')

        a = soup.find_all('a')
        for i in a:
            print(f"href in a: {i.get('href')}")
    else:
        print(f'Failed to get page content. Code:{res.status_code}')


def get_subtitles():
    index = int(input())
    link = input()
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    subtitles = soup.find_all('h2')
    print(subtitles[index].text)


if __name__ == '__main__':
    # pip install beautifulsoup4
    # get_soup()
    get_subtitles()
