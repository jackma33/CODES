from instagrapi import Client
from config import USERNAME, PASSWORD

cl = Client()
cl.login(USERNAME, PASSWORD)

media = cl.photo_upload_to_story(
    'C:\\Users\\Admin\\Pictures\\NAABO\\pexels-photo-1034662.jpeg',
    "good"
)

try:
    with open('upload_details.txt') as f:
        f.write(str(media.dict())+'\n')
except: print(media.dict())
