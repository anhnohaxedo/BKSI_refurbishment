import re
from exceptiongroup import catch
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

ussh = 'https://ussh.vnu.edu.vn'

def get_categories():
    driver = webdriver.ChromiumEdge(EdgeChromiumDriverManager().install())
    categories = []
    driver.get('https://ussh.vnu.edu.vn/vi/news')
    body = driver.find_element(By.CLASS_NAME, 'section-body')
    wrapper = body.find_elements(By.CLASS_NAME, 'wraper') #vcl viết sai chính tả

    sidebar = wrapper[1].find_element(By.CLASS_NAME, 'widget-sidebar-title-border')
    metismenu = sidebar.find_element(By.CLASS_NAME, 'metismenu')
    title_list = metismenu.find_elements(By.CSS_SELECTOR, 'li')
    for title in title_list:
        elements = title.find_elements(By.CSS_SELECTOR, '*')
        if (len(elements) == 1):
            categories.append(elements[0].get_attribute('href'))
    driver.quit()
    return categories

def get_news(categories):
    news = []
    for category in categories:
        driver = webdriver.ChromiumEdge(EdgeChromiumDriverManager().install())
        driver.get(category)
        body = driver.find_element(By.CLASS_NAME, 'section-body')
        wrapper = body.find_elements(By.CLASS_NAME, 'wraper')[1].find_element(By.CLASS_NAME, 'news_column')
        columns = wrapper.find_elements(By.CSS_SELECTOR, 'h3')
        exp = r'<a\s+(?:[^>]*?\s+)?href=(["])(.*?)\1'
        for column in columns:
            html = column.get_attribute('innerHTML')   
            news.append(ussh + re.findall(exp,html)[0][1])
        driver.quit()
    return news

def get_general_page():
    driver = webdriver.ChromiumEdge(EdgeChromiumDriverManager().install())    
    driver.get('https://hcmussh.edu.vn/tong-quan')
    main = driver.find_element(By.ID, 'app')
    section = main.find_element(By.CSS_SELECTOR, 'section')
    paragraphs = section.find_elements(By.CSS_SELECTOR, 'p')
    file = open('D:/project/BKSI/BKSI_refurbishment/scrapping/hcmussh/tong_quan' + '.txt', 'w', newline='', encoding='utf-8')
    for p in paragraphs:
        file.write(p.text)
        file.write('\n')
    file.close()
    driver.quit()

def get_article(name, link):
    driver = webdriver.ChromiumEdge(EdgeChromiumDriverManager().install())
    driver.get(link)
    body = driver.find_element(By.CLASS_NAME, 'section-body')
    wrapper = body.find_elements(By.CLASS_NAME, 'wraper')[1].find_element(By.CLASS_NAME, 'panel-body')
    header = wrapper.find_element(By.CSS_SELECTOR, 'h1')
    print(header)
    clearfix = wrapper.find_element(By.CLASS_NAME, 'clearfix')
    new_body = wrapper.find_element(By.ID, 'news-bodyhtml')
    try:
        author = wrapper.find_element(By.CSS_SELECTOR, 'p').text
    except:
        author = ''
    file = open('D:/project/BKSI/BKSI_refurbishment/scrapping/ussh/' + name + '.txt', 'w', newline='', encoding='utf-8')
    print(header.text)
    file.write(clearfix.text)
    for element in new_body.find_elements(By.CSS_SELECTOR, 'div'):
        if element.text != '':
            file.write(element.text)
    file.write(author)
    file.close()
    driver.quit()

categories = get_categories()
news = get_news(categories=categories)

for i in range(len(news)):
    get_article('new_' + str(i), news[i])
