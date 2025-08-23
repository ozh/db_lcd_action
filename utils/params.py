import logging
import os
import sys
from dotenv import load_dotenv

if sys.platform != "win32":
    import smbus
else:
    # Mock smbus and spidev for Windows testing to avoid importing hardware-specific libraries
    from utils.mock_classes import SMBus as smbus

from lib import LCD_1inch28

load_dotenv()

# Sound sensor
DB_SENSOR_BUS = smbus.SMBus(1)  # Open I2C1
DB_SENSOR_ADDRESS = 0x48  # Decibel meter I2C address

# Decibel thresholds
DB_THRESH_LOW_DAY = int(os.getenv("DB_THRESH_LOW_DAY"))
DB_THRESH_LOW_NIGHT = int(os.getenv("DB_THRESH_LOW_NIGHT"))
DB_THRESH_MEDIUM_DAY = int(os.getenv("DB_THRESH_MEDIUM_DAY"))
DB_THRESH_MEDIUM_NIGHT = int(os.getenv("DB_THRESH_MEDIUM_NIGHT"))

# Time ranges for day and night
DAY_START = os.getenv("DAY_START")
DAY_END = os.getenv("DAY_END")

# Debug mode - default false
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() in ("true", "1", "yes")

# Initialize the LCD screen
LCD_SCREEN = LCD_1inch28.LCD_1inch28()
LCD_SCREEN.Init()
LCD_SCREEN.bl_DutyCycle(100)

# Configure logging : loggind.INFO for debug mode, logging.CRITICAL otherwise
logging.basicConfig(
    level=logging.INFO if DEBUG_MODE else logging.CRITICAL,
    format='%(levelname)s: %(asctime)s - %(message)s',
    datefmt='%H:%M:%S',
)


def is_daytime() -> bool:
    """
    Check if the current time is within the defined day period.
    :return: True if current time is within day period, False otherwise.
    """
    from datetime import datetime
    now = datetime.now().strftime("%H:%M")
    return DAY_START <= now <= DAY_END


def get_db_thresholds():
    """
    Get the decibel thresholds based on the time of day.
    :return: Tuple of low and medium decibel thresholds.
    """
    if is_daytime():
        db_thresh_low = DB_THRESH_LOW_DAY
        db_thresh_medium = DB_THRESH_MEDIUM_DAY
    else:
        db_thresh_low = DB_THRESH_LOW_NIGHT
        db_thresh_medium = DB_THRESH_MEDIUM_NIGHT
    return db_thresh_low, db_thresh_medium
