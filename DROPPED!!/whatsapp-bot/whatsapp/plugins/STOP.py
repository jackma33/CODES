import sys
from time import sleep

def STOP(driver, message):
    driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    ).send_keys("STOPPED !!")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
    sleep(1.5)
    
    driver.close()
    sys.exit()
