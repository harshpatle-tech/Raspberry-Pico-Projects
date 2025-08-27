from pico_i2c_lcd import I2cLcd
from machine import I2C, Pin, ADC
import utime as time

# I2C LCD Setup
i2c = I2C(id=1, scl=Pin(27), sda=Pin(26), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# LDR Sensor on ADC2 (GP28)
ldr = ADC(Pin(28))

lcd.clear()
lcd.putstr("LDR Ready...")
time.sleep(2)
lcd.clear()

# Main loop
while True:
    ldr_value = ldr.read_u16()  # 0 to 65535 range
    light_status = "LIGHT" if ldr_value > 30000 else "DARK"
    
    lcd.clear()
    lcd.putstr("LDR Value:\n{}".format(ldr_value))
    time.sleep(1)
    
    lcd.clear()
    lcd.putstr("Status:\n{}".format(light_status))
    time.sleep(1)
