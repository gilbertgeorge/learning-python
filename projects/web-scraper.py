import string
import requests
import os
from bs4 import BeautifulSoup


def write_results_to_file(current_page, file_name, text):
    file_name = os.path.join('../supplemental', 'scrape', 'step5', current_page, file_name)
    # file_name = os.path.join(current_page, file_name)
    file = open(file_name, 'wb')
    file.write(text)
    file.close()


def create_page_directory(current_page):
    directory_name = f'Page_{current_page}'
    directory_name = os.path.join('../supplemental', 'scrape', 'step5', directory_name)
    os.mkdir(directory_name)


def navigate_article(article_link, file_name, current_page):
    article_request = requests.get(article_link)
    if article_request:
        article_soup = BeautifulSoup(article_request.content, 'html.parser')
        article_body = article_soup.find('div', {'class': 'c-article-body'})
        if article_body is None:
            article_body = article_soup.find('div', {'class': 'Theme-Layer-BodyText--inner'})
        write_results_to_file(current_page, file_name, article_body.text.encode('utf-8'))


def article_search(response, current_page, article_type):
    saved_articles = []
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        create_page_directory(current_page)
        for article in articles:
            parent_span = article.find('span', {'data-test': 'article.type'})
            span = parent_span.find('span')
            link = article.find('a', {'data-track-action': 'view article'})
            article_link = f"https://www.nature.com{link['href']}"
            link_text = link.text.translate(str.maketrans('', '', string.punctuation))
            file_name = link_text.strip().replace(' ', '_') + '.txt'

            if span and span.text == article_type:
                navigate_article(article_link, file_name, f'Page_{current_page}')
                saved_articles.append(file_name)

        print(f'Saved {len(saved_articles)} articles on page {current_page}: {saved_articles}')
    else:
        print(f'The URL returned {response.status_code}!')


def make_request():
    page_limit = int(input())
    article_type = input()
    user_url = 'https://www.nature.com/nature/articles'
    for page_number in range(1, page_limit + 1):
        payload = {'year': '2020', 'page': page_number}
        response = requests.get(user_url, params=payload)
        article_search(response, page_number, article_type)


if __name__ == '__main__':
    make_request()
