from machine import Pin, I2C

# esp32
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)

# esp8266
# i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)

sensors = dict([(0x76, 'bme280'), (0x0B, 'semea'), (0x23, 'bh1750')])

for address in i2c.scan():
    print('Detected sensor at 0x{:02X}: {}'.format(address, sensors[address]))
else:
    print('No sensors detected')
