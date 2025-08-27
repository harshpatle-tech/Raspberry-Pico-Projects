from pico_i2c_lcd import I2cLcd
from machine import I2C, Pin
import utime as time

# LCD I2C setup (GPIO27 = SCL, GPIO26 = SDA)
i2c = I2C(id=1, scl=Pin(27), sda=Pin(26), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Relay setup on GP10
relay = Pin(10, Pin.OUT)

lcd.clear()
lcd.putstr("Relay Control\nStarting...")
time.sleep(2)
lcd.clear()

while True:
    # Turn ON Relay
    relay.low()
    lcd.clear()
    lcd.putstr("LED ON via Relay")
    print("LED ON")
    time.sleep(2)
    
    # Turn OFF Relay
    relay.high()
    lcd.clear()
    lcd.putstr("LED OFF via Relay")
    print("LED OFF")
    time.sleep(2)
