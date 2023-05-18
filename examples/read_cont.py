from u8488a import base
from time import sleep

dev = base.PowerMeter()
# List available devices
devs = dev.get_device_list()
if len(devs) > 0:
    dev.open_device(devs[0])
else:
    print("No device found!")
    exit(1)

print("Available devices:")
print(devs)

# Setting frequency to 20 GHz
dev.frequency = 1.85e9

while True:
    # Read power level every second
    print(f"Power: {dev.get_power()} dBm")
    sleep(1)
