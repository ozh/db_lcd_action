import logging
import time

from utils.actions import take_action
from utils.lcd import show_image_from_db_level, lcd_switch_off
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
        lcd_switch_off()
        logging.critical("Ctrl^C -> Exiting application.")
