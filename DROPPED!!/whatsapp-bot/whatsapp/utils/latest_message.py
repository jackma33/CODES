from time import sleep
from bs4 import BeautifulSoup
from whatsapp.plugins.clear import clear


def get_N(driver):
    with open('whatsapp/data/NAABO.html', 'w', encoding="utf-8") as f:
        f.write(driver.page_source)

    f = open('whatsapp/data/NAABO.html', 'r', encoding='UTF-8')
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    N = soup.find('div', class_="_3K4-L",
                  attrs={"role": "region"}).find_all('div', class_="_2wUmf")
    N = len(N)

    return N


def latest_message(driver):
    n = 0
    N = get_N(driver)

    try:
        message = driver.find_element_by_css_selector(
            f"#main > div._2gzeB > div > div._33LGR > div._3K4-L > div:nth-child({N}) > div > div > div._22Msk > div._2jGOb.copyable-text > div > span.i0jNr.selectable-text.copyable-text > span")
        message = message.text
        return message
    except:
        n += 1
        try:
            message = driver.find_element_by_css_selector(
            f"#main > div._2gzeB > div > div._33LGR > div._3K4-L > div:nth-child({N+n}) > div > div > div._22Msk > div._2jGOb.copyable-text > div > span.i0jNr.selectable-text.copyable-text > span")
            message = message.text
            return message
        except:
            pass
        
        if n == 10:
            clear(driver, message=None)
