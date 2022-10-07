#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import pickle
#import pandas as pd

list = ['Linkowanie\n1\nBaza mailowa\nReklama na Allegro i OLX\nWpis o temacie "Jaki botki kupić w tym sezonie"\n1\nDodaj kartę']
list = list[0].split('/n')
print(list)
"""

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Acer\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--profile-directory=Profile 1")


driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')

url = driver.command_executor._url
session_id = driver.session_id
driver = webdriver.Remote(command_executor=url, desired_capabilities={})
driver.close()
driver.session_id = session_id
driver.get("")
#def get_link():
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("https://trello.com/b/khvLOCXA/triocode")

print(session_id)
print(executor_url)

def create_driver_session(session_id, executor_url):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

    # Save the original function, so we can revert our patch
    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute

    return new_driver

driver2 = create_driver_session(session_id, executor_url)
print(driver2.current_url)

def save_cookies(driver, path):
    with open(path, 'wb') as cookiefile:
        pickle.dump(driver.get_cookies(), cookiefile)


def load_cookies(driver, path):
    with open(path, 'rb') as cookiefile:
        cookies = pickle.load(cookiefile)
        for cookie in cookies:
            driver.add_cookie(cookie)
"""


