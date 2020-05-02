# Devloper: Tsankesara

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep
import random

accNo = int(input("No of Accounts: "))

print("Requesting Proxies:")

req_proxy = RequestProxy()
proxies = req_proxy.get_proxy_list()
maxNum = len(proxies)
print("\n \n Max No of Proxies:" + str(maxNum) + "\n \n")


i = 0


while accNo > i:
    k =random.randint(0, maxNum-1)
    l =random.randint(0, maxNum-1)
    PROXY = proxies[k].get_address()
    PROXY_PLACE = proxies[k].country
    first_name = (random.choice(open("Fnames.txt").read().split()))
    last_name =  (random.choice(open("Lnames.txt").read().split()))
    full_name = (first_name + ' ' + last_name)
    username = (first_name + last_name + '.' + str(random.randint(1, 100)) + str(random.randint(1, 1000)))
    password = (open("password.txt").readline())
    email = (username + '@' + 'gmail.com')
    print("\n \n Connecting to Proxy: " + PROXY + "\n")
    print("IP is from: " + str(PROXY_PLACE) + "\n \n")

    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,

        "proxyType":"MANUAL",
    }
    
    #browser.get('https://www.expressvpn.com/what-is-my-ip')
    browser = webdriver.Chrome(ChromeDriverManager().install())
    try:
        browser.set_page_load_timeout(30) # wait 30 second
        browser.get('https://www.instagram.com/accounts/emailsignup/')
    except TimeoutException as ex:
        browser.close()
        continue
        
    print("\n \n Instagram Webpage Opened \n \n")
    sleep(3)
    
    try:
        email_in = browser.find_element_by_name("emailOrPhone")
    except NoSuchElementException:
        continue
    
    email_in.send_keys(email)
    sleep(4)

    print("\n \n Your randomize Email:" + email + "\n \n")

    full_name_in = browser.find_element_by_name("fullName")
    full_name_in.send_keys(full_name)
    sleep(5)
    print("\n \n Your randomize Full Name is: " + full_name + "\n \n")
    username_in = browser.find_element_by_name("username")
    username_in.send_keys(username)
    print("\n \n Your randomize Username is: " + username + "\n \n")
    sleep(4)

    password_in = browser.find_element_by_name("password")
    password_in.send_keys(password)
    print("\n \n Password Entred \n \n")
    sleep(2)

    sign_up = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button')
    sign_up.click()
    sleep(5)

    year_index = (random.randint(20, 46))
    month_index = (random.randint(1, 12))
    day_index = (random.randint(1, 27))

    year_in =  Select(browser.find_element_by_xpath('//*[@title="Year:"]'))
    month_in =  Select(browser.find_element_by_xpath('//*[@title="Month:"]'))
    day_in =  Select(browser.find_element_by_xpath('//*[@title="Day:"]'))
    year_in.select_by_index(year_index)
    print("\n Years Entred \n")
    sleep(1)
    month_in.select_by_index(month_index)
    print("\n Month Entred \n")
    sleep(1)
    day_in.select_by_index(day_index)
    print("\n Date Entred \n")
    sleep(5)
    try:
        next1 = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button')
        next1.click()
    except NoSuchElementException:
        next1 = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button') 
        next1.click()
    sleep(10)
    with open('username.txt', 'w') as f_output:
            f_output.write(username)
    browser.close()

    i = i+1
