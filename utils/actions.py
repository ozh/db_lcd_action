"""
Define actions you want to perform given a specific dB level

THIS IS AN EXAMPLE FILE, YOU MUST MODIFY IT TO YOUR NEEDS
"""
import datetime
import logging
import subprocess
from datetime import timedelta, datetime


from utils.params import get_db_thresholds

ACTION_TAKEN = False
MINIMUM_ACTION_DURATION = timedelta(seconds=60)
ACTION_TIME = 0

def take_action(db_level):
    """
    Perform an action based on the dB level.

    :param db_level: The current dB level.
    """

    global ACTION_TIME
    global ACTION_TAKEN

    if ACTION_TAKEN and (datetime.now() - ACTION_TIME < MINIMUM_ACTION_DURATION):
        logging.info("Action already taken recently, skipping.")
        return

    db_thresh_low, db_thresh_medium = get_db_thresholds()

    if db_level < db_thresh_low:
        throttle_bandwith(1000000000) # restore bandwidth to 1 Gbps
        illuminate_leds("green")      # illuminate LEDs in green
        ACTION_TAKEN = False  # reset action taken flag
        return

    if db_level < db_thresh_medium:
        throttle_bandwith(512000)     # throttle bandwidth to 512 kbps
        illuminate_leds("orange")     # illuminate LEDs in orange

    else:
        throttle_bandwith(64000)      # throttle bandwidth to 64 kbps
        illuminate_leds("red")        # illuminate LEDs in red

    ACTION_TAKEN = True
    ACTION_TIME = datetime.now()  # Update the action time
    logging.info("Action initiated at %s", ACTION_TIME.strftime("%H:%M:%S"))

    return


def illuminate_leds(color):
    """
    Illuminate LEDs in a specified color.
    """
    # Placeholder for the actual command you would use to control the LEDs.
    logging.info(f"Illuminating LEDs in {color} color.")


def throttle_bandwith(rate_bps):
    """
    Throttle the network bandwidth to a specified rate.
    """
    # Placeholder for the actual command you would use to define port rate limits.
    #
    # Following code is a real example for my switch (Netgear GS728) :
    #
    # switch_ip = "192.168.1.99" # IP of my switch
    # port = 12                  # Switch port to which the PC I want to throttle is connected)
    #
    # for direction in [1, 2]:  # 1=ingress (incoming), 2=egress (outgoing)
    #     oid = f"1.3.6.1.4.1.4526.10.1.1.1.2.1.1.{port}.{direction}"
    #     cmd = ["snmpset", "-v", "2c", "-c", "public", switch_ip, oid, "i", str(rate_bps)]
    #     subprocess.run(cmd, check=True)

    rate_kbps = rate_bps / 1000
    if rate_kbps >= 1000:
        rate_bps = f"{rate_kbps / 1000:.0f} Mbps"
    else:
        rate_bps = f"{rate_kbps:.0f} kbps"
    logging.info(f"Rate now {rate_bps}")




