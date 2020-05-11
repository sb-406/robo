#io Prüfen
import time
import RPi.GPIO as GPIO
 
GPIO_PIN_IR_SENSOR = 4
GPIO_PIN_IR_SENSOR_2 = 17
GPIO_PIN_AUSGANG = 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
if __name__ == '__main__':
    GPIO.setup(GPIO_PIN_IR_SENSOR, GPIO.IN)
    #GPIO.setup(GPIO_PIN_IR_SENSOR_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(GPIO_PIN_AUSGANG, GPIO.OUT)
    start_time, end_time = 0, 0

if GPIO.input(GPIO_PIN_IR_SENSOR ) == GPIO.HIGH:
        time.sleep(0.001)

        GPIO.output(GPIO_PIN_AUSGANG, GPIO.HIGH)

