import os
import sys

sys.stderr = open(os.devnull, "w")

try:
    import psutil
finally:
    sys.stderr = sys.__stderr__


def main():
    print(psutil.sensors_temperatures())


main()
