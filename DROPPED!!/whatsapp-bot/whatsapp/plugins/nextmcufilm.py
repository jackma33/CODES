import os, requests
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def send(driver, reply, filepath):
    browser = driver
    action = ActionChains(driver)

    attachment_box = browser.find_element_by_xpath(
        '//div[@title="Attach"]')
    attachment_box.click()
    time.sleep(1)

    image_box = browser.find_element_by_xpath(
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filepath)
    time.sleep(2)

    tb = driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]'
    )

    reply = reply.split('\n')
    for q in reply:
        tb.send_keys(f"{str(q)}")
        action.key_down(Keys.LEFT_SHIFT).key_down(Keys.ENTER).key_up(Keys.LEFT_SHIFT).perform()
        action.key_down(Keys.LEFT_SHIFT).key_down(Keys.ENTER).key_up(Keys.LEFT_SHIFT).perform()

    
    send_btn = browser.find_element_by_xpath(
        '//span[@data-icon="send"]')
    send_btn.click()
    time.sleep(2)


def nextmcufilm(driver, message):
    url = "https://whenisthenextmcufilm.com/api"
    
    r = requests.get(url)
    data = r.json()

    reply = f"""Title: {data["title"]}
Release Date: {data["release_date"]}
Remaining Days: {data["days_until"]}
Overview: {data["overview"]}"""

    image = requests.get(str(data["poster_url"]))
    with open("whatsapp/data/mcu-poster.jpg", "wb") as file:
        file.write(image.content)
    
    send(driver, reply, filepath='C:/NAABO/Codes/whatsapp-bot/whatsapp/data/mcu-poster.jpg')
