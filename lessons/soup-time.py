from bs4 import BeautifulSoup
import requests
from lxml import etree


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


def read_file(path):
    with open(path, 'r') as file:
        contents = file.read()
        soup = BeautifulSoup(contents, "xml")
    print(soup.prettify())

    tag1 = soup.find("title")
    print(tag1)  # <title year="1994">Pulp Fiction</title>
    tag2 = soup.find_all("director")
    print(tag2)  # [<director>Quentin Tarantino</director>, <director>David Lynch</director>]
    tag3 = soup.find("title", {"year": "1994"})
    print(tag3)  # <title year="1994">Pulp Fiction</title>

    print(soup.director)
    print(tag3.parent)
    tag4 = soup.find("movie")
    print(list(tag4.children))
    tag5 = soup.find("director")
    print(tag5.previous_sibling)  # \n
    print(list(tag5.previous_siblings))  # ['\n', <title year="1994">Pulp Fiction</title>, '\n']
    tag3 = soup.find("title", {"year": "1994"})
    print(tag3.next_sibling)  # \n
    print(list(tag3.next_siblings))  # ['\n', <director>Quentin Tarantino</director>, '\n']


def create_xml():
    xml_string = "<a><b>hello</b></a>"

    root = etree.fromstring(xml_string)

    print(type(root))  # <class 'lxml.etree._Element'>


def read_xml(xml_path):
    tree = etree.parse(xml_path)
    # print(type(tree))  # <class 'lxml.etree._ElementTree'>

    root = tree.getroot()
    # print(type(root))  # <class 'lxml.etree._Element'>
    etree.dump(root)
    etree.dump(root[1])


if __name__ == '__main__':
    # pip install beautifulsoup4
    # get_soup()
    # get_subtitles()
    # read_file(r'..\supplemental\xml\xml_file.xml')

    # pip install lxml
    create_xml()
    read_xml(r'..\supplemental\xml\xml_file.xml')
    requests.post('http://movies.com/users/1234/ratings', {'movie_name': 'Frozen', 'movie_rating': '10'})
