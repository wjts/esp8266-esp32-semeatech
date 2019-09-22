from machine import Pin, I2C
from sensors import semea

# esp32
# i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)

# esp8266
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)

sensors = dict([(0x76, 'bme280'), (0x0B, 'semea'), (0x23, 'bh1750')])

for address in i2c.scan():
    # sensors.append(address)
    print('Detected sensor at 0x{:02X}: {}'.format(address, sensors[address]))

semea = semea.Semea(i2c=i2c, sensor=semea.SENSOR_O3)

print(f'Sensor value: {semea.sensor_value}ug/m3')
print(f'Sensor value: {semea.sensor_value_ppb}ppb')
print(f'Temperature: {semea.temperature}°C')
print(f'Humidity: {semea.humidity}%')
