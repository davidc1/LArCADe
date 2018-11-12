from picamera import PiCamera
from time import sleep
import datetime
import sys
import os
os.system("sudo i2cset -y 1 0x70 0x00 0x5A")
os.system("sudo i2cset -y 1 0x70 0x09 0x0f")
os.system("sudo i2cset -y 1 0x70 0x02 0x32")
os.system("sudo i2cset -y 1 0x70 0x04 0x32")
os.system("sudo i2cset -y 1 0x70 0x05 0x32")
os.system("sudo i2cset -y 1 0x70 0x07 0x32")
camera = PiCamera()

camera.start_preview()

#to take pictures:
filename = datetime.datetime.now() .strftime ("%Y-%m-%d-%H.%M.%S.jpg")

#a = raw_input()
sleep(10)
#sys.exit()
camera.capture('/home/pi/Desktop/Camera/%s'%filename)

#to make a video:
#filename = datetime.datetime.now() .strftime ("%Y-%m-%d-%H.%M.%S.h264")
#camera.start_recording('/home/pi/Desktop/Camera/%s'%filename)
#sleep(100)
#camera.stop_recording()

#always:
camera.stop_preview()

os.system("sudo i2cset -y 1 0x70 0x00 0x00")
