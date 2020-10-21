#Dim and LED

import time
from machine import Pin, PWM

#the int variable "LED" stores the pin used by the LED at D6
LED = Pin(12, Pin.OUT)

#PWM is generated using 10 bits, so it ranges between
#0 and 1023 (2^10 = 1024)
#each PWM has frequency and duty cycle
pwm = PWM(LED)

#while True runs to infinity
while True:
    for i in range(0,1024,1):
        #set the brightness of the LED duty();
        pwm.duty(i)
        
        #wait 3 milliseconds
        time.sleep_ms(3)
    #keep the LED at the maximum brightness for 500 ms
    time.sleep_ms(500)

    for i in range(1024,0,-1):
        pwm.duty(i)
        time.sleep_ms(3)
    #keep the LED at the minimum brightness for 500 ms
    time.sleep_ms(500)

    


