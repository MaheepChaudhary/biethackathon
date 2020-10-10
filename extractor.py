from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://www.wsj.com/')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/header/div[2]/button/span').click()
driver.find_element_by_xpath('//*[@id="searchInput"]').send_keys('Tesla')
driver.find_element_by_xpath('//*[@id="searchInput"]').send_keys(Keys.ENTER)
#driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/header/div[2]/div/form/input[2]').click()
time.sleep(10)
present_link = driver.current_url
print(present_link)
print(driver.find_element_by_xpath('//*[@id="search-results"]/div/div').text)
