from lcd_api import LcdApi
from machine import I2C
from time import sleep_ms

class I2cLcd(LcdApi):
    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.num_lines = num_lines
        self.num_columns = num_columns
        self.backlight = 0x08
        self._init_lcd()

    def _write_byte(self, data):
        self.i2c.writeto(self.i2c_addr, bytes([data | self.backlight]))

    def _send(self, data, mode=0):
        high = data & 0xF0
        low = (data << 4) & 0xF0
        self._write_nibble(high | mode)
        self._write_nibble(low | mode)

    def _write_nibble(self, nibble):
        self._write_byte(nibble | 0x04)
        sleep_ms(1)
        self._write_byte(nibble & ~0x04)
        sleep_ms(1)

    def _init_lcd(self):
        sleep_ms(20)
        self._write_nibble(0x30)
        sleep_ms(5)
        self._write_nibble(0x30)
        sleep_ms(1)
        self._write_nibble(0x30)
        sleep_ms(1)
        self._write_nibble(0x20)
        sleep_ms(1)

        self._send(0x28)  # Function set: 4-bit, 2 line, 5x8 dots
        self._send(0x08)  # Display off
        self._send(0x01)  # Clear display
        sleep_ms(2)
        self._send(0x06)  # Entry mode
        self._send(0x0C)  # Display on

    def clear(self):
        self._send(0x01)
        sleep_ms(2)

    def backlight_on(self):
        self.backlight = 0x08
        self._write_byte(0)

    def backlight_off(self):
        self.backlight = 0x00
        self._write_byte(0)

    def move_to(self, col, row):
        row_offsets = [0x00, 0x40, 0x14, 0x54]
        self._send(0x80 | (col + row_offsets[row]))

    def putstr(self, string):
        for char in string:
            self._send(ord(char), 1)
