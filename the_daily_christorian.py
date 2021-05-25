#!/usr/bin/python3
from bs4 import BeautifulSoup

article_of_the_week_link = None
article_of_the_week_title = None
coping_counters = []
this_day = None
quote = None

with open("/tmp/cwcki_source/cwcki") as source:
    soup = BeautifulSoup(source)

    article_of_the_week = soup.body.find("a", string="More...")
    article_of_the_week_title = article_of_the_week["title"]
    article_of_the_week_link = "https://sonichu.com" + article_of_the_week["href"]
    for counter in soup.body.find_all("div", style="font-size:2em"):
        coping_counters.append(counter.get_text().replace(",",""))
    this_day = soup.body.find("div", style="float:left;margin-right:0.9em")
    # print(soup.body.find("table", id="mp-right").find("td",)

print(article_of_the_week_link)
print(article_of_the_week_title)
for coping_counter in coping_counters:
    print(coping_counter)
