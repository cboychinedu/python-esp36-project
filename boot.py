import micropython
import network

import esp
esp.osdebug(None)

try:
    import usocket as socket
except:
    import socket 
import gc
gc.collect()
ssid = "Nedu"
password = "generatedpass4321"
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print("Connection successful")
print(station.ifconfig())

##
