
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    while True:
        input_state = GPIO.input(11)
        if input_state == False:
            print('Button Pressed')
            GPIO.output(7, True)
        else:
            GPIO.output(7, False)
except KeyboardInterrupt:
    GPIO.cleanup()

