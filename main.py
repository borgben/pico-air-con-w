from machine import Pin, ADC
import time 

led = Pin(16, Pin.OUT)
led.value(1)
time.sleep(2)
# We set Pin26 to read the analog input from the IR reciever 
ir_rec = Pin(22, Pin.IN, Pin.PULL_UP)

current_value = ir_rec.value()
start_value = time.ticks_us()
while True: 
    next_value = ir_rec.value()
    if next_value != current_value:
        print(str(time.ticks_diff(time.ticks_us(),start_value))+","+str(current_value))
        start_value = time.ticks_us()
        current_value = next_value