# Devloper: Tsankesara

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
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
print("Max No of Proxies:" + str(maxNum))


i = 0


while accNo > i:
    k =random.randint(0, maxNum-1)
    print(k)
    PROXY = proxies[k].get_address()
    first_name = (random.choice(open("Fnames.txt").read().split()))
    last_name =  (random.choice(open("Lnames.txt").read().split()))
    full_name = (first_name + ' ' + last_name)
    username = (first_name + '.' + last_name + '.' + str(random.randint(1, 100)) + str(random.randint(1, 1000)))
    password = (open("password.txt").readline())
    email = (username + '@' + 'kitmain.com')
    print("Connecting to Proxy:" + PROXY)
    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,

        "proxyType":"MANUAL",
    }
    
    #browser.get('https://www.expressvpn.com/what-is-my-ip')
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.instagram.com/accounts/emailsignup/')
    print("Instagram Webpage Opened")
    sleep(3)

    email_in = browser.find_element_by_name("emailOrPhone")
    email_in.send_keys(email)
    sleep(4)

    print("Your randomize Email:" + email)

    full_name_in = browser.find_element_by_name("fullName")
    full_name_in.send_keys(full_name)
    sleep(5)
    print("Your randomize Full Name is:" + full_name)
    username_in = browser.find_element_by_name("username")
    username_in.send_keys(username)
    print("Your randomize Username is:" + username)
    sleep(4)

    password_in = browser.find_element_by_name("password")
    password_in.send_keys(password)
    print("Password Entred")
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
    print("Years Entred")
    sleep(1)
    month_in.select_by_index(month_index)
    print("Month Entred")
    sleep(1)
    day_in.select_by_index(day_index)
    print("Date Entred")
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
