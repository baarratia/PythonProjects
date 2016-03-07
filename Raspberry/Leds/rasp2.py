import time

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(15)
    if input_state == False:
        print('Button Pressed')
        #ROJO
        GPIO.output(7, True)
        time.sleep(1)
        GPIO.output(7, False)
        #AMARILLO
        GPIO.output(11, True)
        time.sleep(1)
        GPIO.output(11, False)
        #VERDE
        GPIO.output(13, True)
        time.sleep(1)
        GPIO.output(13, False)
        time.sleep(0.2)
