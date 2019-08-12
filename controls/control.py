from __future__ import print_function
from chromecast_main.py import play ,pause

import bluetooth
import os
import time
import pychromecast
import GPIO as gpio 


# Variables 


device_friendly_name = ""




# Init chromecats 

def chromecats_init():

    

    chromecasts = pychromecast.get_chromecast()

    cast = next( cc for cc in chromecasts if cc.device.friendly_name == device_friendly_name)

    cast.wait()

    mc = cast.media_controller



# Continue chromecats 

def chromecats_contine():

    mc.play()

# Stop chromecats 
def chromecats_pause():
    
    mc.pause()




 
