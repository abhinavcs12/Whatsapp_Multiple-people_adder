import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def Group_add(name):
    l=[]
    with open('people.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            if row[0] != "Name":
                l.append(row[0])

    option = webdriver.ChromeOptions()
    option.add_argument(r' --user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default')
    option.add_argument(' --profile-directory=Default')

    chrome_browser = webdriver.Chrome(executable_path='D:\Python Project\chromedriver',options=option)
    chrome_browser.get('https://web.whatsapp.com/')
    time.sleep(20)

    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(name))
        user.click()
        time.sleep(10)
    except:
        print("WhatsApp group doesn't exist")
        print("Please Try again")
        return
    
    menu = chrome_browser.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span')
    menu.click()
    time.sleep(3)

    add_name = chrome_browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/section/div[6]/div[2]/div[1]/div[2]')
    add_name.click()
    time.sleep(3)
    
    for i in l[:14]:
        search_name = chrome_browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[2]')
        search_name.click()
        search_name.send_keys(i)
        time.sleep(3)

        tick = chrome_browser.find_element_by_xpath("//span[@title='{}']".format(i))
        tick.click()
        time.sleep(2)

        cross = chrome_browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div/span/button/span')
        cross.click()
        time.sleep(1)

    
    ok = chrome_browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/span[2]/div/div/div/span')
    ok.click()

    add_p = chrome_browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div[2]')
    add_p.click()

    print("*"*90)
    print("success")

    return

name = input("Enter the Group Name : ")
Group_add(name)
