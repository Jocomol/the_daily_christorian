#!/usr/bin/python3
from bs4 import BeautifulSoup

article_of_the_week_link = None
article_of_the_week_title = None
article_of_the_week_picture = None
article_of_the_week_text = "" 
coping_counters = []
this_day = None 
this_day_text = None
this_day_link = None 
this_day_picture = None
quote = None 
quoted = None 
ongoing = [] 
dates = []

with open("/tmp/cwcki_source/cwcki") as source:
    soup = BeautifulSoup(source, features="html5lib")

    article_of_the_week = soup.body.find("a", string="More...")
    article_of_the_week_title = article_of_the_week["title"]
    article_of_the_week_link = "https://sonichu.com" + article_of_the_week["href"]
    article_of_the_week_picture = "https://sonichu.com" + soup.body.find("img", class_="thumbimage")["src"]
    article_of_the_week_text_para = soup.body.find("div", class_="thumb tright").find_next_sibling("p") 
    while article_of_the_week_text_para is not None:
        if "..." not in article_of_the_week_text_para.get_text():
            article_of_the_week_text += article_of_the_week_text_para.get_text()
        article_of_the_week_text_para = article_of_the_week_text_para.find_next_sibling("p")

    for counter in soup.body.find_all("div", style="font-size:2em"):
        coping_counters.append(counter.get_text().replace(",",""))
    
    this_day = soup.body.find("div", style="float:left;margin-right:0.9em")
    para = this_day.find_all("p")
    this_day_text = para[0].get_text()
    this_day_link = "https://sonichu.com" + para[1].find("b").find("a")["href"]
    this_day_picture = "https://sonichu.com" + this_day.find("a", class_="image")["href"]
    
    topic = soup.body.find("b", string="Ongoing").find_next_sibling("a")
    while topic is not None:
        ongoing.append(topic.get_text())
        topic = topic.find_next_sibling("a")
    
    dates_array = soup.body.find("b", string="Ongoing").parent.find_next_sibling("ul").find_all("li")
    for date in  dates_array:
        dates.append(date.get_text())
    
    text = soup.body.find("h2", string="Quote of the Now").parent.parent.find_next_sibling("tr").get_text()
    
    first = True 
    for line in text.splitlines():
        if line.strip() and len(line) > 1:
            if first:
                quote = line
                first = False 
            else:
                quoted = line 

    
print("---")
print("Article Of the Week")
print(article_of_the_week_link)
print(article_of_the_week_title)
print(article_of_the_week_picture)
print(article_of_the_week_text)
print("---")

print("This day")
print(this_day_link)
print(this_day_text)
print(this_day_picture)
print("---")

print("Ongoing")
for item in ongoing:
    print(item)
for date in dates:
    print(date)
print("---")

print("Counter")
for coping_counter in coping_counters:
   print(coping_counter)
print("---")

print("Quotes")
print(quote)
print(quoted)
print("---")
