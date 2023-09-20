from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")


# link = driver.find_element(By.CSS_SELECTOR, value="{.className tagname}")

#always works
link = driver.find_element(By.XPATH, value='//*[@id="poExpander"]/div[1]/div/div[4]/span[2]')
print(link.text)


#close will close or active tab and quit will close the intire browser
driver.quit()

