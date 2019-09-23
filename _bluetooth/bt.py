import utime
import bluetooth

def test():
    bt = bluetooth.Bluetooth()
    bt.active(True)
    bt.advertise(100, 'MicroPython')
    print('----')
    tx = bluetooth.Characteristic('6E400002-B5A3-F393-E0A9-E50E24DCCA9E', bluetooth.FLAG_READ|bluetooth.FLAG_NOTIFY)
    rx = bluetooth.Characteristic('6E400003-B5A3-F393-E0A9-E50E24DCCA9E', bluetooth.FLAG_WRITE)
    s = bt.add_service('6E400001-B5A3-F393-E0A9-E50E24DCCA9E', [tx, rx])
    tx.write('foo')
