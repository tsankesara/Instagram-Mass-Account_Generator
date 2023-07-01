from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import random
import requests
from bs4 import BeautifulSoup

def fetch_proxies():
    url = "https://sslproxies.org"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="table table-striped table-bordered")
    proxies = []
    for row in table.find_all("tr"):
        columns = row.find_all("td")
        if len(columns) >= 2:
            ip = columns[0].text
            port = columns[1].text
            proxy = ip + ":" + port
            proxies.append(proxy)
    return proxies

accNo = int(input("No of Accounts: "))

print("Requesting Proxies:")

prox = fetch_proxies()
proxies = prox[::-1]

maxNum = len(proxies)
print("\nMax No of Proxies: " + str(maxNum) + "\n")

i = 0

while accNo > i:
    k = random.randint(0, maxNum - 1)
    PROXY = proxies[k]
    PROXY_PLACE = ""

    first_name = random.choice(open("Fnames.txt").read().split())
    last_name = random.choice(open("Lnames.txt").read().split())
    full_name = first_name + ' ' + last_name
    username = first_name + last_name + '.' + str(random.randint(1, 100)) + str(random.randint(1, 1000))
    password = open("password.txt").readline()
    email = username + '@' + 'gmail.com'

    print("\nConnecting to Proxy: " + PROXY + "\n")
    print("IP is from: " + PROXY_PLACE + "\n")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    webdriver_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    try:
        browser.set_page_load_timeout(80)  # wait 30 seconds
        # Simulate pressing Ctrl+Shift+I
        browser.get('https://www.instagram.com/accounts/emailsignup/')
        
    except TimeoutException as ex:
        browser.quit()
        continue

    print("\nInstagram Webpage Opened\n")
    # Simulate pressing Ctrl+Shift+I
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.SHIFT + 'i')
    sleep(3)

    try:
        email_in = browser.find_element(By.NAME, "emailOrPhone")
    except NoSuchElementException:
        browser.quit()
        continue

    email_in.send_keys(email)
    sleep(4)

    print("\nYour randomized Email: " + email + "\n")

    full_name_in = browser.find_element(By.NAME, "fullName")
    full_name_in.send_keys(full_name)
    sleep(5)
    print("\nYour randomized Full Name: " + full_name + "\n")

    username_in = browser.find_element(By.NAME, "username")
    username_in.send_keys(username)
    print("\nYour randomized Username: " + username + "\n")
    sleep(4)

    password_in = browser.find_element(By.NAME, "password")
    password_in.send_keys(password)
    print("\nPassword Entered\n")
    sleep(2)

    sign_up = browser.find_element(By.XPATH, '//button[text()="Sign up"]')
    sign_up.click()
    sleep(30)

    year_index = random.randint(20, 46)
    month_index = random.randint(1, 12)
    day_index = random.randint(1, 27)
    
    year_in = Select(browser.find_element(By.XPATH, '//*[@title="Year:"]'))
    month_in = Select(browser.find_element(By.XPATH, '//*[@title="Month:"]'))
    day_in = Select(browser.find_element(By.XPATH, '//*[@title="Day:"]'))
    year_in.select_by_index(year_index)
    print("\nYears Entered\n")
    sleep(1)
    month_in.select_by_index(month_index)
    print("\nMonth Entered\n")
    sleep(1)
    day_in.select_by_index(day_index)
    print("\nDate Entered\n")
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

    browser.quit()

    i += 1

