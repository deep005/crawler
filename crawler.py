from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
from selenium.webdriver.common.keys import Keys
link = ''
driver = webdriver.PhantomJS()
driver.get(link)
time.sleep(3)
#Block for infinite_scroll
no_of_pagedowns = 240
while no_of_pagedowns:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(.75)
    no_of_pagedowns-=1
#block for retreiving the details
hotelNames = driver.find_elements_by_class_name('hote_nameinfo')
reg = driver.find_elements_by_class_name('hotel_location')
actPrice = driver.find_elements_by_css_selector('.actual_price.ng-binding')
starRating = driver.find_elements_by_tag_name('starrating')
print (len(hotelNames))
print (len(actPrice))
info = []
for i in range(0,len(hotelNames)):
        infor = {}
        elem = starRating[i].find_elements_by_css_selector(".glyphicon-star.active-star.ng-scope")
        if(len(elem)< 3):
            continue
        infor['name'] = hotelNames[i].text
        infor['region'] = reg[i].text
        infor['price'] = actPrice[i].text
        infor['rating'] = str(len(elem))
        info.append(infor)
#parsing the data to the csv
keys = info[0].keys()
with open('mmt_pune.csv', 'w') as csvfile:
            dict_writer = csv.DictWriter(csvfile, keys)
            dict_writer.writeheader()
            dict_writer.writerows(info)
driver.close()

