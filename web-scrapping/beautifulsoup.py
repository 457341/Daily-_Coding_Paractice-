from bs4 import BeautifulSoup
import requests
import pandas as pd
url = requests.get('https://www.coreyms.com').text
soup = BeautifulSoup(url,'html.parser')
print(soup.prettify()) # prettifies the html content
headlines, contents, authors, post_times, video_links  = ([] for i in range(5))
for article in soup.find_all('article'):
    # print(article.h2.a.text)
    headlines.append(article.h2.a.text) #headlines
    contents.append(article.select_one('.entry-content').p.text)#contents
    authors.append(article.select_one('.entry-author-name').text)#author
    post_times.append(article.time.text)#posting time
    try:
        youtube_link = article.find('iframe')['src']
        video_id = youtube_link.split('/')[4].split('?')[0] 
        video_links.append('https://www.youtube.com/watch?v'+video_id)
    except TypeError:
        video_links.append('Not available')

articles = pd.DataFrame({"Headline":headlines,"Content":contents,"Author":authors,"Posted Time":post_times,"Youtube Link":video_links})
# print(articles)
articles.to_csv('corey_articles.csv')
print(articles.head(1))    # to check if articles are saved