import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select(".storylink")
subtext = soup.select(".subtext")


def score_sorted(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


def custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get("href", None)
        vote = subtext[index].select(".score")
        if len(vote):
            score = int(vote[0].getText().replace(" points", ""))
            if score > 99:
                hn.append({"title": title, "link": href, "votes": score})
    return score_sorted(hn)


pprint.pprint(custom_hn(links, subtext))