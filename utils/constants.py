import logging
import sys

if sys.platform != "win32":
    import smbus
else:
    # Mock smbus and spidev for Windows testing to avoid importing hardware-specific libraries
    from utils.mock_classes import SMBus as smbus

from lib import LCD_1inch28

# App parameters

DB_SENSOR_BUS = smbus.SMBus(1)  # Open I2C1
DB_SENSOR_ADDRESS = 0x48  # Decibel meter I2C address

# Decibel thresholds
DB_THRESH_LOW = 50  # considered low up to this decibel level
DB_THRESH_MEDIUM = 60  # considered medium up to this decibel level - high above this decibel level

# Initialize the LCD screen
LCD_SCREEN = LCD_1inch28.LCD_1inch28()
LCD_SCREEN.Init()
LCD_SCREEN.bl_DutyCycle(100)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(asctime)s - %(message)s',
    datefmt='%H:%M:%S',
)
