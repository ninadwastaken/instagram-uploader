from instagrapi import Client
import os
import datetime

username = "freedfera"
password = "Anjali&Ninad1"


cl = Client()
cl.login(username, password)

def instagram_upload(path:str, caption:str):

    cl.clip_upload(path, caption, thumbnail=r"cutest_dog.jpg")


# instagram_upload(r"dog.jpg", "test1")
upload_flag = True
time_to_upload = 14
day_count = 1
path = r'cutest_dog_reel.mp4'


while True:
    curr_hour = int(datetime.datetime.now().strftime('%H'))
    print(curr_hour)

    if curr_hour == time_to_upload + 1:
        upload_flag = True
    elif curr_hour == time_to_upload and upload_flag:
        instagram_upload(path, f"Day {day_count}")
        upload_flag = False
        day_count += 1
        print('uploaded')