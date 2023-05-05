from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchWindowException
from time import sleep


def main():
    cookie_clicker_url = "https://orteil.dashnet.org/cookieclicker/"
    chromedriver_path = "/Users/karlmarx/Documents/development/chromedriver"

    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.get(url=cookie_clicker_url)
    sleep(5)

    driver.find_element(By.CSS_SELECTOR, "button p.fc-button-label").click()
    english_lang = driver.find_element(By.ID, "langSelect-EN")
    english_lang.click()
    sleep(5)

    try:
        its_on = True
        while its_on:
            highest = 0
            button = []
            cookie_button = driver.find_element(By.ID, "bigCookie")
            cookie_button.click()
            try:
                total_cookies = int(driver.find_element(By.ID, "cookies").text.split()[0])
            except ValueError:
                total_cookies = int(driver.find_element(By.ID, "cookies").text.replace(",", "").split()[0])
            products = driver.find_elements(By.CLASS_NAME, "product")
            try:
                prices = [price.find_element(By.CLASS_NAME, "price").text.replace(",","") for price in products]
            except AttributeError:
                pass
            else:
                try:
                    for price in prices:
                        if int(price) > highest and int(price) < total_cookies:
                            highest = int(price)
                            button.append(str(price))
                except ValueError:
                     pass
                try:
                    products[prices.index(button[-1])].click()
                except IndexError:
                    pass
                except ElementClickInterceptedException:
                    pass
    except NoSuchWindowException:
        pass

if __name__ == "__main__":
    main()
