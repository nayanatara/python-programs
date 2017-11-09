#!/usr/bin/python3

# do something every 10 seconds until the end of the hour
import os
import time

a=0
b=0


while a<10:
    cmd="fswebcam -F 3 --fps 20 -r 800x600 sha" + str(b) + ".jpg"
    os.system(cmd)
    time.sleep(10)
    a=a+1
b=b+1
