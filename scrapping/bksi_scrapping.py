from bs4 import BeautifulSoup
import requests, csv
import constant
import re

url = constant.URL
hcmut = constant.HCMUT
def get_articles(): 
    articles = []
    request = requests.get(url).text
    soup = BeautifulSoup(request, 'html.parser')
    a_tags = soup.find_all('a')
    for tag in a_tags:
        if tag.has_attr('href'):
            if 'article' in tag['href'] :
                articles.append(tag['href'])
    return articles

def get_categories():
    categories = []
    request = requests.get(url).text
    soup = BeautifulSoup(request, 'html.parser')
    a_tags = soup.find_all('a')
    for tag in a_tags:
        if tag.has_attr('href'):
            if 'category' in tag['href'] :
                categories.append(tag['href'])
    return categories

def get_blogs(category): 
    blogs = []
    request = requests.get(hcmut + category).text
    soup = BeautifulSoup(request, 'html.parser')
    a_tags = soup.find_all('a')
    for tag in a_tags:
        if tag.has_attr('href'):
            if 'blog' in tag['href'] :
                blogs.append(tag['href'])
    return blogs



for article in get_articles():
    request = requests.get(hcmut + article).text
    soup = BeautifulSoup(request, 'html.parser')
    paragraphs = soup.find('section')
    documents = paragraphs.find('p').get_text(separator=' ', strip= True)
    words = re.sub('[., -()>@\[\]/:]+', ' ', documents)     
    file = open('D:/project/BKSI/BKSI_refurbishment/scrapping/articles/article_' + article[-2:] + '.txt', 'w', newline='', encoding='utf-8')
    file.write(documents)
    file.close()

for category in get_categories():
    for blog in get_blogs(category=category):
        request = requests.get(hcmut + blog).text
        soup = BeautifulSoup(request, 'html.parser')
        paragraphs = soup.find('section')
        documents = paragraphs.find('p').get_text(separator=' ', strip= True)
        file = open('D:/project/BKSI/BKSI_refurbishment/scrapping/blogs/' + re.split('/', blog)[-1] + '.txt', 'w', newline='', encoding='utf-8')
        file.write(documents)
        file.close()
        # words = re.split('[., -()>@\[\]/:]+', documents)     
        # file = open('blogs/' + re.split('/', blog)[-1] + '.csv', 'w', newline='', encoding='utf-8')
        # writer = csv.writer(file)
        # writer.writerow(words)
        # file.close()





from bs4 import BeautifulSoup
import requests, csv
import constant
import re

request = requests.get('https://hcmussh.edu.vn/tong-quan').text
soup = BeautifulSoup(request, 'lxml')