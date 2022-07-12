from time import sleep


def clear(driver, message):
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div/div").click()
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/span[4]/div/ul/div/div/li[4]").click()
    sleep(1.5)
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[2]/div/div[2]/div/div").click()
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]").click()
