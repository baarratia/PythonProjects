import time

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    c = GPIO.input(15)
    if c is False:
        print(GPIO.input(15))
        for i in range(2):
            GPIO.output(7, True)
            time.sleep(1)
            GPIO.output(7, False)
            GPIO.output(11, True)
            time.sleep(1)
            GPIO.output(11, False)
            GPIO.output(13, True)
            time.sleep(1)
            GPIO.output(13, False)
    time.sleep(0.2)
GPIO.cleanup()
