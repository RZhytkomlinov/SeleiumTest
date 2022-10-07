from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
username = ''
password = ''


def find_list():
    df = pd.DataFrame(columns=['Lista'])
    raw_data = driver.find_elements(By.XPATH,
                                    "/html[@class='board-theme-dark']/body[@class='feplat3731']/div[@id='trello-root']/div[@id='chrome-container']/div[@class='eDvIPXGjzBdiaB']/div[@id='surface']/main[@id='popover-boundary']/div/div[@id='content-wrapper']/div[@id='content']/div[@class='board-wrapper']/div[@class='board-main-content']/div[@class='board-canvas']/div[@id='board']/div[@class='js-list list-wrapper'][2]")
    tasks = raw_data[0].get_attribute('innerText')
    tasks = tasks.split("\n")
    df['Lista'] = tasks
    df.to_excel('lista.xlsx')


if __name__ == '__main__':
    # find_list()
    driver.get("https://trello.com/b/khvLOCXA/triocode")
    login_button = driver.find_element(By.XPATH,
                                       "/html/body[@class='feplat3731']/div[@id='trello-root']/div[@id='chrome-container']/div[@class='eDvIPXGjzBdiaB']/div[@id='surface']/main[@id='popover-boundary']/div/div[@id='content-wrapper']/div[@id='content']/div[@class='js-react-root']/div[@class='BMO756CE7DJW6Q']/div[2]/button[@class='o8V5BfhKqk3f2x Ts+YceGnvTbKoG lnOVlvCd0LhzVB JIXQq8gDYY04N6']")
    login_button.click()
    enter_username = driver.find_element(By.ID, 'user')
    WebDriverWait(driver, 10)
    enter_username.send_keys(username)
    second_page = driver.find_element(By.ID, 'login')
    second_page.click()
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.title_is('Zaloguj się, aby kontynuować - Zaloguj się przy użyciu konta Atlassian'))
    finally:
        enter_password = driver.find_element(By.NAME, 'password')
        enter_password.send_keys(password)
        final_login = driver.find_element(By.ID, 'login-submit')
        final_login.click()
        wait.until(EC.title_is('TrioCode | Trello'))
    find_list()
