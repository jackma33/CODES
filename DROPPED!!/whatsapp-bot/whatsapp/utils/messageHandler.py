import random
from time import sleep


def send(driver, message):
    driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    ).send_keys(f"{str(message)}")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
    sleep(1.5)


def messageHandler(driver, message):
    if message.lower().strip() in ['hi', 'hey', 'hello']:
        resp = ['Hey there, How are you??', 'Hi', 'What\'s up??']
        send(driver, random.choice(resp))
