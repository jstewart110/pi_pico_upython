from machine import Pin, I2C

# Define I2C on hardware 0 Pins 8 and 9
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
# scan for devices
print(i2c.scan())

# Write a 123 to device 76
i2c.writeto(39, b'123')

# Read from device 76
i2c.readfrom(39, 4)

# Define I2C on hardware 1 pins 6 and 7
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=100000)

# scan for devices
i2c.scan()

# Write a 123 to device 76
i2c.writeto_mem(76, 6, b'456')

# Read from device 76
i2c.readfrom_mem(76, 6, 4)