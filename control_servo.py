from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels = 16)
kit.servo[0].set_pulse_width_range(1000, 2000)

option = int(input())
if option == 1:
	kit.servo[0].angle = 0
	time.sleep(2)
	kit.servo[0].angle = 180
elif option == 0:
	kit.continuous_servo[0].throttle = 1
	time.sleep(1)
	kit.continuous_servo[0].throttle = 0
	time.sleep(1)
	kit.continuous_servo[0].throttle = -1

