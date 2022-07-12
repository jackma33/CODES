from instagrapi import Client
from config import USERNAME, PASSWORD

cl = Client()
cl.login(USERNAME, PASSWORD)

media = cl.photo_upload(
    "image.png",
    "caption"
)

try:
    with open('upload_details.txt') as f:
        f.write(str(media.dict())+'\n')
except: print(media.dict())
