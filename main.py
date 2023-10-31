import requests
from bs4 import BeautifulSoup

def get_10_new_article(a):
    counter = 0
    answer = []
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition Yx GX)"
    }
    url = "https://habr.com/ru/articles/top/daily/"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    article_cards = soup.find_all("article", class_="tm-articles-list__item")
    for article in article_cards:
        if counter < a:
            article_name = article.find("a", class_="tm-title__link").text.strip()
            article_rate = article.find("div", class_="tm-votes-meter tm-data-icons__item").get_text()
            article_help_ulr = article.find("a", class_="tm-title__link").get("href")
            article_url = f'https://habr.com/{article_help_ulr}'
            article_time = article.find("span", class_="tm-article-reading-time__label").text.strip()

            #print(f"{article_name} | {article_rate} | {article_time} | {article_url}")
            counter += 1
            answer.append(f"Название: {article_name}. \n Всего голосов: {article_rate}.\n Примерное время на прочтение: {article_time}.\n Ссылка на статью: {article_url} \n")

    return answer
# data = get_10_new_article()
# for el in data:
#     print(el)
#