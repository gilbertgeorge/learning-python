import string
import requests
import os
from bs4 import BeautifulSoup


def write_results_to_file(file_name, text):
    file_name = os.path.join('supplemental', file_name)
    file = open(file_name, 'wb')
    file.write(text)
    file.close()


def make_request(url):
    SEARCH_TEXT = 'News'
    saved_articles = []
    res = requests.get(url)
    if res:
        soup = BeautifulSoup(res.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            parent_span = article.find('span', {'data-test': 'article.type'})
            span = parent_span.find('span')
            link = article.find('a', {'data-track-action': 'view article'})
            if span and span.text == SEARCH_TEXT:
                article_link = f"https://www.nature.com{link['href']}"
                link_text = link.text.translate(str.maketrans('', '', string.punctuation))
                file_name = link_text.strip().replace(' ', '_') + '.txt'
                saved_articles.append(file_name)
                article_request = requests.get(article_link)
                if article_request:
                    article_soup = BeautifulSoup(article_request.content, 'html.parser')
                    article_body = article_soup.find('div', {'class': 'c-article-body'})
                    write_results_to_file(file_name, article_body.text.encode('utf-8'))
        print(f'Saved articles: {saved_articles}')
    else:
        print(f'The URL returned {res.status_code}!')


def scrape():
    user_url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
    make_request(user_url)


if __name__ == '__main__':
    scrape()
