#from pico_i2c_lcd import I2cLcd
#from machine import I2C
#from machine import Pin
#import utime as time

#i2c = I2C(id=1,scl=Pin(27),sda=Pin(26),freq=100000)
#lcd = I2cLcd(i2c, 0x27, 2, 16) # LCD 16x2

#lcd.putstr('Hello Harsh')

from pico_i2c_lcd import I2cLcd
from machine import I2C, Pin
import utime as time

# I2C LCD setup (GPIO27 = SCL, GPIO26 = SDA)
i2c = I2C(id=1, scl=Pin(27), sda=Pin(26), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)  # Adjust address to 0x3F if needed

# Ultrasonic sensor pins
TRIG = Pin(10, Pin.OUT)
ECHO = Pin(11, Pin.IN)

# Startup message
lcd.clear()
lcd.putstr("Hello Harsh")
time.sleep(2)
lcd.clear()

# Function to get distance in cm
def get_distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

    while ECHO.value() == 0:
        signaloff = time.ticks_us()
    while ECHO.value() == 1:
        signalon = time.ticks_us()

    time_passed = time.ticks_diff(signalon, signaloff)
    distance_cm = (time_passed * 0.0343) / 2
    return distance_cm

# Main loop
while True:
    try:
        distance = get_distance()
        lcd.clear()
        lcd.putstr("Distance:\n{:.2f} cm".format(distance))
        time.sleep(1)
    except Exception as e:
        lcd.clear()
        lcd.putstr("Error")
        time.sleep(1)
