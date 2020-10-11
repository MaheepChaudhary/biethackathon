from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

def scrapper(company):
    driver = webdriver.Firefox(options=options)
    driver.get('https://www.wsj.com/')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/header/div[2]/button/span').click()
    driver.find_element_by_xpath('//*[@id="searchInput"]').send_keys(company)
    driver.find_element_by_xpath('//*[@id="searchInput"]').send_keys(Keys.ENTER)
    #driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/header/div[2]/div/form/input[2]').click()
    time.sleep(3)
    present_link = driver.current_url
    text = driver.find_element_by_xpath('//*[@id="search-results"]/div/div').text
    print(text)
    return text