import requests
from threading import Thread


auth = "afaa7a7e-debe-47ef-a80c-8af390bd1a61"
app_name = "tg-bot-pyronaabo"

HEADERS = {
    "Accept": "application/vnd.heroku+json; version=3",
    "Authorization": f'Bearer {auth}'
}


def get_running():
    url = f"https://api.heroku.com/apps/{app_name}/dynos/worker.1"

    result = requests.get(url, headers=HEADERS)
    print(result)


def run():
    # turn on sleeping app
    payload = {'quantity': 1}
    url = "https://api.heroku.com/apps/" + app_name + "/formation/worker"
    result = requests.patch(url, headers=HEADERS, data=payload)
    print(result)


def stop():
    # turn off running app
    payload = {'quantity': 0}
    url = "https://api.heroku.com/apps/" + app_name + "/formation/worker"
    result = requests.patch(url, headers=HEADERS, data=payload)
    print(result)


if __name__ == '__main__':
    get_running()
