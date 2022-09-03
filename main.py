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


main()
