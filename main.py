import network
import time
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("moon","123456789")
 
# Wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    print('IP: ', wlan.ifconfig()[0])