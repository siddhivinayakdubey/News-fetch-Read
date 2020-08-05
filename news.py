import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  print(news.pubDate.text)
  
  from gtts import gTTS
import os
for news in news_list:
  tts = gTTS(text=news.title.text, lang='en')
  tts.save("news.mp3")
  os.system("mpg321 news.mp3")

