import requests
from bs4 import BeautifulSoup
import re
import psycopg2
from psycopg2 import Error
from selenium import webdriver
import time


#-------------------------------------------------requests & beautifulsoup----------------------------------------------------
# temp = list(range(1, 155))
# pages = []
# for i in temp:
#     pages.append(str(i))
# count = 1
# for j in pages:
#     res = requests.get('https://myzarfilm.red/page/%s/' %(j))
#     print(res, count)
#     count += 1

#     soup = BeautifulSoup(res.text, 'html.parser')

#     movies_title = soup.find_all('h2', attrs={'class': 'sitePost__headerTitle'})
#     rate = soup.find_all('div', attrs={'class': 'rate_num'})

#     movies_title2 = []
#     for item in movies_title:
#         item = re.sub(r'دانلود', '', item.text)
#         item = re.sub(r'^  ', '', item)
#         movies_title2.append(re.sub(r'فیلم', '', item))

#     rate2 = []
#     for item in rate:
#         item = item.find('strong')
#         rate2.append(item.text.strip())

#-------------------------------------------------------------selenium---------------------------------------------------------
driver = webdriver.Chrome(executable_path='E:\Data\Desktop\selenium\chromedriver.exe')
start = 350
end = 451
#adade bala safe shoroo e kar
temp = list(range(start, end))
pages = []
for i in temp:
    pages.append(str(i))
count = start
for j in pages:
    driver.get('https://myzarfilm.men/page/%s/' %(j))
    time.sleep(8)
    print('--', count, '--')
    count += 1

    movies_title2 =[]
    movies_title = driver.find_elements_by_class_name('title')
    del movies_title[:2]
    for item in movies_title:
        movies_title2.append(re.sub(r"دانلود فیلم|ژانر|سریال ها|فیلم ها", "", item.text).strip().lower())
    # print(movies_title2)
        #print(item.get_attribute("value"))

    rate2 =[]
    rate = driver.find_elements_by_xpath('//span[@class="rate"]')
    for item in rate:
        rate2.append(item.text.strip())
    # print(rate2)

    listh = []
    for i,j in zip(rate2, movies_title2):
        try:
            connection = psycopg2.connect(user="belabelabela",
                                          password="belabelabela",
                                          host="belabelabela",
                                          port="belabelabela",
                                          database="dbpython")

            #cursor = connection.cursor()
            #query = 'SELECT movies_title FROM movies'
            #cursor.execute(query)
            #record = cursor.fetchall()
            

            cursor2 = connection.cursor()
            query2 = "insert into movies(rate, movies_title)values('%f', '%s');" %(float(i), j)
            cursor2.execute(query2)

                
            print("sql query Executed successfully in PostgreSQL ")
            connection.commit()
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor2.close()
                connection.close()
                print("PostgreSQL connection is closed", "\n")


def delete():
    try:
            connection = psycopg2.connect(user="belabelabela",
                                          password="belabelabela",
                                          host="belabelabela",
                                          port="belabelabela",
                                          database="dbpython")
            cursor2 = connection.cursor()
            query2 = "delete from movies"
            cursor2.execute(query2)
            print("sql query Executed successfully in PostgreSQL ")
            connection.commit()
    except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
    finally:
            if connection:
                cursor2.close()
                connection.close()
                print("PostgreSQL connection is closed", "\n")


##delete()
