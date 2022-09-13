import requests  # type: ignore
from bs4 import BeautifulSoup


def extract_news(parser):
    """Extract news from a given web page"""
    news_list = []

    tbl = parser.table.findAll("table")[1]
    news = tbl.findAll("tr")
    ninf = {"title": "None", "url": "None", "author": "None", "points": 0}
    for i in range(len(news)):
        n = news[i]
        if i % 3 == 0:
            ninf = {
                "title": "None",
                "url": "None",
                "author": "None",
                "points": 0,
                "comments": 0,
            }
        #elif i % 30 == 0:
        #    ninf = {}
        if n.attrs:
            if n.attrs["class"][0] == "athing":
                ninf["title"] = n.find("a", class_="titlelink").string
                link = n.find("a", class_="titlelink").get("href")
                if "http" in link:
                    ninf["url"] = link
                elif "item" in link:
                    ninf["url"] = "https://news.ycombinator.com/" + link
        else:
            if n.find("a").attrs:
                if "class" in n.find("a").attrs and n.find("a").attrs["class"][0] == "hnuser":
                    ninf["author"] = n.find("a").string
                    ninf["points"] = int(n.find("span").string.split()[0])
                    com = str(n.findAll("a")[-1].string.split()[0])
                    if com.isdigit():
                        ninf["comments"] = int(com)
                    else:
                        ninf["comments"] = 0
            else:
                break
            news_list.append(ninf)
    return news_list


def extract_next_page(parser):
    """Extract next page URL"""
    return parser.table.findAll("table")[1].findAll("tr")[-1].contents[2].find("a").get("href")


def get_news(url, n_pages=1):
    """Collect news from a given web page"""
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news


if __name__ == "__main__":
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    news_list = get_news(url, n_pages=1)
    for l in news_list:
        print(l)
    with open('my.html', 'w') as f:
        f.write(soup.prettify())
