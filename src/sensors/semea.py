from machine import I2C

SENSOR_CO = 0x01
SENSOR_O3 = 0x04
SENSOR_SO2 = 0x05
SENSOR_NO2 = 0X0B


class Semea():
    def __init__(self, i2c=None, sensor=None):
        if sensor not in [SENSOR_CO, SENSOR_O3, SENSOR_SO2, SENSOR_NO2]:
            raise ValueError('Unexpected sensor type {sensor}. Set sensor type'
                             ' to one of SENSOR_CO, SENSOR_O3, SENSOR_SO2 or'
                             ' SENSOR_NO2'.format(sensor=sensor))

        self._sensor = sensor

        if i2c is None:
            raise ValueError('An I2C object is required.')

        self._i2c = i2c

    def checksum(self, bytes, checksum):
        # @todo: sprawdzić zachowanie przy dwubajtowym wyniku
        # dokumentacja tego nie przewiduje
        return 0xff - sum(bytes) == checksum

    def read_value(self, lsb, readbytes):
        self._i2c.writeto(self._sensor, bytearray([0x00, lsb]))
        bytes = self._i2c.readfrom(self._sensor, readbytes)
        checksum = bytes.pop()

        if not self.checksum(bytes, checksum):
            raise ValueError('Checksum failed')

        return int.from_bytes(bytes, 'big')

    @property
    def temperature(self):
        # @todo: sprawdzić jak będą zwracane ujemne wartości
        # dokumentacja tego nie przewiduje
        return round(self.read_value(0x02, 3) / 100, 2)

    @property
    def humidity(self):
        return round(self.read_value(0x03, 3) / 100, 2)

    @property
    def sensor_value(self):
        return self.read_value(0x00, 5)

    @property
    def sensor_value_ppb(self):
        return self.read_value(0x01, 5)
