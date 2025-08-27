from pico_i2c_lcd import I2cLcd
from machine import I2C, Pin
import utime as time

# I2C LCD setup (GPIO27 = SCL, GPIO26 = SDA)
i2c = I2C(id=1, scl=Pin(27), sda=Pin(26), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)  # Change to 0x3F if needed

# IR Sensor and Buzzer setup
ir_sensor = Pin(10, Pin.IN)
buzzer = Pin(18, Pin.OUT)

lcd.clear()
lcd.putstr("IR Sensor Ready")
time.sleep(2)
lcd.clear()

# Main loop
while True:
    if ir_sensor.value() == 0:  # Adjust logic if needed for your sensor
        lcd.clear()
        lcd.putstr("Object Detected")
        buzzer.high()
        time.sleep(0.2)
        buzzer.low()
        time.sleep(0.2)
    else:
        lcd.clear()
        buzzer.low()
    time.sleep(0.1)
