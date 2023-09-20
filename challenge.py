from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org/")

event = {

}

#event dates
dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery time")
date_list = [date.text for date in dates]
year = "2023-"
print(date_list)

#event titles
titles = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li a")
title_list = [title.text for title in titles]
print(title_list)

for i in range(len(date_list)-1):
    print(i)
    event[i] = {
        "time": f"{year}{date_list[i]}",
        "title": f"{title_list[i]}"
    }

print(event)

driver.quit()