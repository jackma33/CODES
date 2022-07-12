import os
import warnings
from time import sleep
from whatsapp import Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def initialize():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    options = webdriver.ChromeOptions()
    options.add_argument(Config.CHROME_PROFILE_PATH)
    # options.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path=Config.EXEC_PATH, options=options)

    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)

    target = '"NAABO"'

    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()
    sleep(1.5)

    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(Keys.SHIFT).send_keys(
        'u').key_up(Keys.CONTROL).key_up(Keys.ALT).key_up(Keys.SHIFT).perform()
    sleep(1.5)
    action.key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(Keys.SHIFT).send_keys(
        'u').key_up(Keys.CONTROL).key_up(Keys.ALT).key_up(Keys.SHIFT).perform()
    sleep(1.5)

    os.system("cls")

    return driver, ActionChains, Keys
