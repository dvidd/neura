"""
Example on how to use the Multizone (Audio Group) Controller
"""

import logging
import sys
import time

import pychromecast
from pychromecast.controllers.multizone import MultizoneController
from pychromecast.socket_client import CONNECTION_STATUS_CONNECTED

# Change to the name of your Chromecast

chromecasts = pychromecast.get_chromecasts()

print(chromecasts)

# Printing the self friendly divice s

# cast = next(cc for cc in chromecasts if cc.device.friendly_name == CAST_NAME)

