#!/usr/bin/python
import socket
import bluetooth, subprocess

nearby_devices = bluetooth.discover_devices(duration=4,lookup_names=True,
                                                      flush_cache=True, lookup_class=False)


TCP_IP = '44:44:1B:04:13:7D'
TCP_PORT = 13854
BUFFER_SIZE = 2048

name = 'Sichiray'      # Device name
addr = '44:44:1B:04:13:7D'      # Device Address
port = 13854         # RFCOMM port
passkey = "0000" # passkey of the device you want to connect

# kill any "bluetooth-agent" process that is already running
subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)

# Start a new "bluetooth-agent" process where XXXX is the passkey
status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)

# Now, connect in the same way as always with PyBlueZ
try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((addr,port))
except bluetooth.btcommon.BluetoothError as err:
    # Error handler
    pass
