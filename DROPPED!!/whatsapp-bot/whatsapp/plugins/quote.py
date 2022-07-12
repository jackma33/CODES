from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def get_quote():
    #1643
    import json

    with open('whatsapp/data/quotes.json') as f:
      data = json.load(f)
    
    from random import randint
    value = randint(0, 1644)

    return (data[value]['text'], data[value]['author'])


def quote(driver, message):
    action = ActionChains(driver)

    tb = driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    )

    q, a = get_quote()
    tb.send_keys(f"{str(q)}")
    action.key_down(Keys.LEFT_SHIFT).key_down(Keys.ENTER).key_up(Keys.LEFT_SHIFT).perform()
    action.key_down(Keys.LEFT_SHIFT).key_down(Keys.ENTER).key_up(Keys.LEFT_SHIFT).perform()
    tb.send_keys(f"~ {str(a)}")

    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
    sleep(1.5)
    
    return None
