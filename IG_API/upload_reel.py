from instagrapi import Client
from config import USERNAME, PASSWORD

cl = Client()
cl.login(USERNAME, PASSWORD)

media = cl.clip_upload(
    "video-path",
    "caption",
    "thumbnail-Path or it will generate automatically"
)

try:
    with open('upload_details.txt') as f:
        f.write(str(media.dict())+'\n')
except: print(media.dict())
