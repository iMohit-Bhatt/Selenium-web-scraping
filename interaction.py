from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromeOption = webdriver.ChromeOptions()
chromeOption.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOption)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

required = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(required.text)
# required.click()

search = driver.find_element(By.XPATH, value='//*[@id="searchInput"]')
search1 = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')

search1.click()
search.send_keys('Python')
search.send_keys(Keys.ENTER)

driver.quit()
