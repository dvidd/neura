#! /usr/bin/env python

import sys
import time

import pychromecast




requested_volume = float(sys.argv[1]) if len(sys.argv) > 1 else None

chromecats = pychromecast.get_chromecast()

cast = next( cc for cc in chromecasts if cc.device.friendly_name == device_friendly_name)

cast.wait()



def set_volume(self, volume):
    """ Allows to set volume. Should be value between 0..1.
        Returns the new volume.
        """
    volume = min(max(0, volume), 1)
    self.logger.info("Receiver:setting volume to %.1f", volume)
    self.send_message({MESSAGE_TYPE: 'SET_VOLUME','volume': {'level': volume}})
    
    return volume
