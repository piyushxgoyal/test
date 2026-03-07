from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


options = ChromeOptions()
options.binary_location = r"C:\Users\KIIT\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
options.add_experimental_option("detach", True)

driver = Chrome(options=options)

driver.maximize_window()

# 1. Open Amazon and print all category names
driver.get('https://amazon.in')
sleep(3)
e = driver.find_elements(By.CSS_SELECTOR, "#nav-xshop a")
for i in e:
    print(i.text)

# 2. Print top 10 movie names from IMDB Top 250 https://www.imdb.com/chart/top/
driver.get('https://www.imdb.com/chart/top/')
sleep(3)
e = driver.find_elements(By.CSS_SELECTOR,'h3[class="ipc-title__text"]')
for i in range(10):
    print(e[i].text)

# 3.	Count all images on amazon
driver.get('https://amazon.in')
sleep(3)
e = driver.find_elements(By.TAG_NAME, 'img')
print(len(e))

## 4.	Open https://demoqa.com/select-menu Target first dropdown in that page and select first option
driver.get('https://demoqa.com/select-menu')
sleep(2)
e=driver.find_element('xpath','//input[@id="react-select-2-input"]')
e.click()
sleep(1)
driver.find_element(By.XPATH,'//div[text()="Group 1, option 1"]').click()

## 5.	Print All Links in amazon Page
driver.get('https://amazon.in')
sleep(2)
e=driver.find_elements(By.TAG_NAME,'a')
for i in e:
    print(i.get_attribute("href"))

## 6.	Print Auto Suggestions of any site
driver.get('https://www.amazon.in/')
sleep(2)
e=driver.find_element('id',"twotabsearchtextbox")
e.send_keys('samsung')
sleep(2)
a=driver.find_elements('xpath','//div[@class="s-suggestion-container"]')
sleep(2)
for i in a:
    print(i.text)


sleep(10)
driver.quit()