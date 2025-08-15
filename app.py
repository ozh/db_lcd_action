import time
import sys

from utils.actions import take_action
from utils.lcd import show_image_from_db_level
from utils.sensor import get_db_level

def main():
    while True:
        db_level = get_db_level()
        show_image_from_db_level(db_level)
        take_action(db_level)
        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl^C -> Exiting application.")
