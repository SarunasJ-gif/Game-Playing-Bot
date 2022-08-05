from time import time

from selenium import webdriver
from selenium.webdriver.common.by import By

web_driver_path = "C:\Development/chromedriver.exe"
driver = webdriver.Chrome(web_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

timeout = time() + (5 * 60)
start = time() + 5
while True:
    cookie.click()
    if time() > start:
        store = driver.find_elements(By.CSS_SELECTOR, "#store div b")
        buy_cursors_prices = [price.text for price in store]
        buy_cursors_prices.remove('')
        names = [name.split("-")[0].strip() for name in buy_cursors_prices]
        prices = [int(price.split("-")[1].strip().replace(",", "")) for price in buy_cursors_prices]
        money = driver.find_element(By.ID, "money")
        money_in_account = int(money.text.strip().replace(",", ""))
        print(prices)
        print(money_in_account)
        button_to_click = max([price for price in prices if price <= money_in_account])
        index_of_name = prices.index(button_to_click)
        button_id = f"buy{names[index_of_name]}"
        button = driver.find_element(By.ID, button_id)
        button.click()
        start = time() + 5
    if time() > timeout:
        cookies = driver.find_element(By.ID, "cps")
        cookies_per_second = cookies.text
        print(cookies_per_second)
        driver.quit()
        break
