# Mock libraries for Windows to avoid dependency on hardware

class SMBus:
    def __init__(self, bus_number):
        self.bus_number = bus_number
        self.registers = {}

    def SMBus(self, *args, **kwargs):
        pass

class SPIdev:
    def __init__(self, spi=1,spi_freq=40000000,rst = 27,dc = 25,bl = 18,bl_freq=1000,i2c=None,i2c_freq=100000):
        self.spi = spi
        self.spi_freq = spi_freq
        self.rst = rst
        self.dc = dc
        self.bl = bl
        self.bl_freq = bl_freq
        self.i2c = i2c
        self.i2c_freq = i2c_freq

    def SpiDev(self, *args, **kwargs):
        pass

class DigitalOutputDevice:
    def __init__(self, pin, active_high=True, initial_value=False):
        self.pin = pin
        self.active_high = active_high
        self.value = initial_value

    def on(self):
        self.value = True

    def off(self):
        self.value = False

class PWMOutputDevice:
    def __init__(self, pin, frequency=1000):
        self.pin = pin
        self.frequency = frequency
        self.value = 0
