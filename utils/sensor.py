import sys
import random

from utils.constants import DB_SENSOR_BUS, DB_SENSOR_ADDRESS

def get_db_level():
    if sys.platform == "win32":
        # return a random value for testing purposes
        random.seed()  # Initialize random number generator
        data = random.randint(35, 85)  # Simulate a decibel
    else :
        # Read the decibel level from the sensor
        DB_SENSOR_BUS.write_byte(DB_SENSOR_ADDRESS, 0x0A)
        data = DB_SENSOR_BUS.read_byte(DB_SENSOR_ADDRESS)

    return data

