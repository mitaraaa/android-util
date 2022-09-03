import re
import os
import sys

sys.stderr = open(os.devnull, "w")

try:
    import psutil
finally:
    sys.stderr = sys.__stderr__


def main():
    print(
        re.findall(r"\w+=([^,)]+)", str(psutil.sensors_temperatures()["battery"][0]))[1]
    )
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    print(percent + "% | " + plugged)


main()
