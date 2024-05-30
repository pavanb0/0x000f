import usb.core
import usb.util
import time
import pyautogui

# Replace with your device's VID and PID
VENDOR_ID = 0x0810
PRODUCT_ID = 0x0001

# Find the USB device
dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

# Check if the device was found
if dev is None:
    raise ValueError('Device not found')

# Set the active configuration. With no arguments, the first configuration will be the active one
dev.set_configuration()

# Get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0, 0)]

# Match the endpoint with your device's endpoint address
ep = usb.util.find_descriptor(
    intf,
    # match the first IN endpoint
    custom_match=lambda e:
    usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_IN
)

assert ep is not None

# Read data from the endpoint continuously
try:
    while True:
        try:
            # Adjust the size of the read according to your device's requirements
            data = ep.read(size_or_buffer=64, timeout=100)
            # pyautogui.moveTo(data[1],data[2])
            print('Data read from device:',data)
        except usb.core.USBError as e:
            if e.errno == 110:  # Timeout error
                continue
            else:
                raise e
        time.sleep(0.001)  # Add a small delay to prevent CPU overuse
except KeyboardInterrupt:
    print("Stopped reading data.")

# Release the device
usb.util.dispose_resources(dev)
