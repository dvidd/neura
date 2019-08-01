from __future__ import print_function
import time
import pychromecast

# Your Chromecast device Friendly Name
device_friendly_name = "Andy"

chromecasts = pychromecast.get_chromecasts()

# select Chromecast device
cast = next(cc for cc in chromecasts if cc.device.friendly_name == device_friendly_name)

# wait for the device
cast.wait()
print(cast.device)
print(cast.status)

# get media controller 
mc = cast.media_controller
# set online video url
mc = cast.media_controller
# mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
mc.block_until_active()
print(mc.status)


# MediaStatus(current_time=42.458322, content_id='http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', content_type='video/mp4', duration=596.474195, stream_type='BUFFERED', idle_reason=None, media_session_id=1, playback_rate=1, player_state='PLAYING', supported_media_commands=15, volume_level=1, volume_muted=False)


#time.sleep(5)
#mc.play()