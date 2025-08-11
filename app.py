import time
import sys

from utils.lcd import show_image_from_db_level
from utils.sensor import get_db_level

def main():
    try:
        while True:
            data = get_db_level()
            show_image_from_db_level(data)
            time.sleep(1)

    except IOError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl^C -> Exiting application.")
