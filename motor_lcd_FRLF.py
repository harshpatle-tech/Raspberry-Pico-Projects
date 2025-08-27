from machine import Pin, I2C
from time import sleep
from pico_i2c_lcd import I2cLcd
import utime as time

# Define motor pins
motor1_in1 = Pin(0, Pin.OUT)
motor1_in2 = Pin(1, Pin.OUT)
motor2_in1 = Pin(2, Pin.OUT)
motor2_in2 = Pin(3, Pin.OUT)

# Setup I2C LCD
i2c = I2C(id=1, sda=Pin(26), scl=Pin(27), freq=100000)
I2C_ADDR = i2c.scan()[0]  # Auto-detect address
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.clear()
lcd.putstr("DC Motor Control")

def stop():
    motor1_in1.value(0)
    motor1_in2.value(0)
    motor2_in1.value(0)
    motor2_in2.value(0)
    lcd.clear()
    lcd.putstr("Stopped")

def forward():
    motor1_in1.value(1)
    motor1_in2.value(0)
    motor2_in1.value(1)
    motor2_in2.value(0)
    lcd.clear()
    lcd.putstr("Forward")

def reverse():
    motor1_in1.value(0)
    motor1_in2.value(1)
    motor2_in1.value(0)
    motor2_in2.value(1)
    lcd.clear()
    lcd.putstr("Reverse")

def right():
    motor1_in1.value(0)
    motor1_in2.value(1)
    motor2_in1.value(1)
    motor2_in2.value(0)
    lcd.clear()
    lcd.putstr("Right")

def left():
    motor1_in1.value(1)
    motor1_in2.value(0)
    motor2_in1.value(0)
    motor2_in2.value(1)
    lcd.clear()
    lcd.putstr("Left")

# Test all directions
while True:
    forward()
    sleep(5)
    reverse()
    sleep(5)
    left()
    sleep(5)
    right()
    sleep(5)
    stop()
    sleep(5)
