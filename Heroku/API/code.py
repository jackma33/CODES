from threading import Thread
import requests
import datetime
from time import sleep


auth = ''
app_name = 'app1'

#detect the running app
HEADERS = {
            "Accept": "application/vnd.heroku+json; version=3",
            "Authorization": f'Bearer {auth}'
        }

url = f"https://api.heroku.com/apps/{app_name}/dynos/worker.1"

result = requests.get(url, headers=HEADERS)
print(result)


if str(result) in ['<Response [200]>','<Response [201]>','<Response [202]>','<Response [206]>']:
    running_app = 'app1'
    sleeping_time ='150000'
    sleeping_app = 'app2'
else:
    running_app = 'app2'
    sleeping_app = 'app1'
    sleeping_time = '010000'




def changeDyno():
	#turn on sleeping app
        payload = {'quantity': 1}
        url = "https://api.heroku.com/apps/" + sleeping_app + "/formation/worker"
        result = requests.patch(url, headers=HEADERS, data=payload)

	#turn off running app
        payload = {'quantity': 0}
        url = "https://api.heroku.com/apps/" + running_app + "/formation/worker"
        result = requests.patch(url, headers=HEADERS, data=payload)


def scheduler():
        while True:
            time = datetime.datetime.now().strftime('%d%H%M')
            if time == sleeping_time:
                changeDyno()
                print('done')
            sleep(1)

Thread(target=scheduler, args=()).start()

#here goes your code
print(running_app)
while True:
    sleep(10)
    print(datetime.datetime.now())