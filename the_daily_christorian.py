#!/usr/bin/python3
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

counter_text = ["days since Chris made up a new escapist fantasy to cope with reality", "days since the Dimensional Merge was to be completed","days since Chris joined the cult of the Idea Guys", "days since Chris last begged for money","days since Chris last up    loaded pages to the Sonichu comic", "days since Chris last applied for a job"]

data = {
    "counter" : None,
    "week": {
        "link": None,
        "title": None,
        "picture": None,
        "text": None,
    },
    "day": {
        "text": None,
        "link": None,
        "picture": None

    },
    "quote": None,
    "quoted": None,
    "dates": []

}

with open("/tmp/cwcki_source/cwcki") as source:
    soup = BeautifulSoup(source, features="html.parser")

    article_of_the_week = soup.body.find("a", string="More...")
    data["week"]["title"] = article_of_the_week["title"]
    data["week"]["link"] = "https://sonichu.com" + article_of_the_week["href"]
    try: # sonichu.com doesn't have a picture in the current Article of the Week, this is a workaround
        data["week"]["picture"] = "https://sonichu.com" + soup.body.find("img", class_="thumbimage")["src"]
    except TypeError:
       data["week"]["picture"] = "https://sonichu.com" 
    #article_of_the_week_text_para = soup.body.find("div", class_="thumb tright").find_next_sibling("p")
    article_of_the_week_text_para = soup.body.find("span", id="Article_of_the_Week").parent.parent.parent.find_next_sibling("tr").find("td").find("div").find("p")
    article_of_the_week_text = ""
    while article_of_the_week_text_para is not None:
        if "..." not in article_of_the_week_text_para.get_text():
            article_of_the_week_text += article_of_the_week_text_para.get_text()
        article_of_the_week_text_para = article_of_the_week_text_para.find_next_sibling("p")
    data["week"]["text"] = article_of_the_week_text
    this_day = soup.body.find("div", style="float:left;margin-right:0.9em")
    para = this_day.find_all("p")
    data["day"]["text"] = para[0].get_text()
    data["day"]["link"] = "https://sonichu.com" + para[1].find("b").find("a")["href"]
    data["day"]["picture"] = "https://sonichu.com" + this_day.find("a", class_="image").findChildren("img", recursive=False)[0]["src"]
    
    dates_array = soup.body.find("a", href="/cwcki/File:CWCki_News.png").parent.find_next_sibling("ul").find_all("li")
    for date in  dates_array:
        data["dates"].append(date.get_text())
    data["counter"] = soup.find("div", style="font-size:2em").getText()
    text = soup.body.find("h2", string="Quote of the Now").parent.parent.find_next_sibling("tr").get_text()
    
    first = True 
    for line in text.splitlines():
        if line.strip() and len(line) > 1:
            if first:
                data["quote"] = line
                first = False 
            else:
                data["quoted"] = line 

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template("template.html")
output = template.render(data=data)

print(output)
