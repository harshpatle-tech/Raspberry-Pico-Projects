from machine import Pin, I2C
from time import sleep
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# I2C setup for LCD
i2c = I2C(1, scl=Pin(27), sda=Pin(26), freq=400000)
lcd_addr = i2c.scan()[0]
lcd = I2cLcd(i2c, lcd_addr, 2, 16)

# Keypad setup
keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]
row_pins = [Pin(pin, Pin.OUT) for pin in (2, 3, 4, 5)]
col_pins = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in (6, 7, 8)]

# LED setup
green_led = Pin(13, Pin.OUT)  # Success
red_led = Pin(18, Pin.OUT)    # Failure

# Password setup
password = ['1', '2', '3', '4']
entered = []

lcd.clear()
lcd.putstr("Enter Password:")

def read_key():
    for i, row in enumerate(row_pins):
        row.high()
        for j, col in enumerate(col_pins):
            if col.value():
                while col.value():
                    pass
                row.low()
                return keys[i][j]
        row.low()
    return None

while True:
    key = read_key()
    if key:
        lcd.clear()
        lcd.putstr("Key: " + key)
        entered.append(key)
        sleep(0.3)

        if len(entered) == len(password):
            if entered == password:
                lcd.clear()
                lcd.putstr("Access Granted")
                for _ in range(3):  # Green LED blink 3 times
                    green_led.on()
                    sleep(0.3)
                    green_led.off()
                    sleep(0.3)
            else:
                lcd.clear()
                lcd.putstr("Wrong Password")
                for _ in range(3):  # Red LED blink 3 times
                    red_led.on()
                    sleep(0.3)
                    red_led.off()
                    sleep(0.3)

            entered = []
            lcd.clear()
            lcd.putstr("Enter Password:")
