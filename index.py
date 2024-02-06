import requests
import json
import time
import re
from bs4 import BeautifulSoup

BASE_URL = "https://www.mitrais.com/case-studies/"


def get_page_content(url=BASE_URL):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    proxy = {
        "http": "http://117.54.114.103:80"
    }

    page = requests.get(url, proxies=proxy)

    # soup = BeautifulSoup(
    #     page.content, 'html.parser')

    # return soup


def get_case_studies_url_per_page(page_content):

    pattern = re.compile(r'https://www\.mitrais\.com/case-studies/[^/]+/')

    matching_urls = set([url['href'] for url in page_content.find_all(
        'a', href=pattern) if 'page/' not in url['href']])

    return matching_urls


def get_articles_content(case_studies):
    articles_content_list = []

    page_content = get_page_content(case_studies)

    f = open('index.html', 'w')
    f.write(page_content.prettify())
    f.close()
    print("Written HTML")
    # return
    # article_title = page_content.find("h1", class_="bold")
    # main_content = page_content.find("article", class_="main-article")

    # single_article_dict = {
    #     "title": article_title.text,
    #     "content": str(main_content.text.replace('\n', ' ').strip())
    # }

    # articles_content_list.append(single_article_dict)

    # return articles_content_list


def save_to_file(data):
    f = open('index.json', 'w')
    f.write(json.dumps(data, ensure_ascii=False))
    f.close()
    print("Written JSON")


urls = [
    # "https://www.mitrais.com/case-studies/partnering-for-success-foodmes-path-to-reliable-solutions",
    "https://www.mitrais.com/case-studies/navigating-advanced-solutions-through-strong-partnership",
    # "https://www.mitrais.com/case-studies/challenges-and-solutions-of-collaborative-agile-development-cac-olive-project",
    # "https://www.mitrais.com/case-studies/technologyone-simplifying-business-with-innovative-enterprise-solutions",
    # "https://www.mitrais.com/case-studies/delivering-true-workforce-scale-ioof",
    # "https://www.mitrais.com/case-studies/improving-processes-and-keeping-one-eye-on-emerging-technologies-buz-software",
    # "https://www.mitrais.com/case-studies/augmenting-the-altrad-services-software-development-team-in-australia",
    # "https://www.mitrais.com/case-studies/developing-invaluable-products-for-forward-thinking-customers-groupmap",
    # "https://www.mitrais.com/case-studies/bluestone-studios-shaping-the-future-of-3d-engineering-solutions",
    # "https://www.mitrais.com/case-studies/modoras-transforming-financial-planning-with-innovation"
]

for url in urls:
    time.sleep(5)
    initial_page_content = get_page_content(url)
    filename = url[37:]
    f = open(f"{filename}.html", 'w')
    f.write(initial_page_content.prettify())
    f.close()
    print(f"{filename}.html written!")

# case_studies = get_case_studies_url_per_page(initial_page_content)
# get_articles_content(
#     "https://www.mitrais.com/case-studies/bluestone-studios-shaping-the-future-of-3d-engineering-solutions/")
# save_to_file(articles_content)

# Scraping single article
# article_title = soup.find("h1", class_="bold")
# main_content = soup.find("article", class_="main-article")

# article_dict = {
#     "title": article_title.text,
#     "content": str(main_content.text.replace('\n', ' ').strip())
# }

# f = open('index.html', 'w')
# f.write(main_content.prettify())
# f.close()
# print("Written HTML")

# f = open('index.json', 'w')
# f.write(json.dumps(article_dict, ensure_ascii=False))
# f.close()
# print("Written JSON")
