#include <libusb-1.0/libusb.h>
#include <iostream>
#include <windows.h>
#include <stdexcept>

#define VENDOR_ID  0x0810
#define PRODUCT_ID 0x0001

void moveCursor(int x, int y) {
    SetCursorPos(x, y);
}

int main() {
    libusb_device_handle* handle = nullptr;
    libusb_context* ctx = nullptr;
    int r;

    // Initialize libusb
    r = libusb_init(&ctx);
    if (r < 0) {
        std::cerr << "Failed to initialize libusb: " << libusb_error_name(r) << std::endl;
        return 1;
    }

    // Open the USB device
    handle = libusb_open_device_with_vid_pid(ctx, VENDOR_ID, PRODUCT_ID);
    if (!handle) {
        std::cerr << "Device not found" << std::endl;
        libusb_exit(ctx);
        return 1;
    }

    // Set the active configuration
    r = libusb_set_configuration(handle, 1);
    if (r < 0) {
        std::cerr << "Failed to set configuration: " << libusb_error_name(r) << std::endl;
        libusb_close(handle);
        libusb_exit(ctx);
        return 1;
    }

    // Claim the interface
    r = libusb_claim_interface(handle, 0);
    if (r < 0) {
        std::cerr << "Failed to claim interface: " << libusb_error_name(r) << std::endl;
        libusb_close(handle);
        libusb_exit(ctx);
        return 1;
    }

    unsigned char data[64];
    int actual_length;

    // Read data from the endpoint continuously
    try {
        while (true) {
            r = libusb_interrupt_transfer(handle, 0x81, data, sizeof(data), &actual_length, 100);
            if (r == LIBUSB_ERROR_TIMEOUT) {
                continue;
            } else if (r < 0) {
                throw std::runtime_error(libusb_error_name(r));
            }

            // Assuming data[1] and data[2] contain the cursor position
            std::cout << "Data read from device: " << static_cast<int>(data[1]) << ", " 
                      << static_cast<int>(data[0]) << ", " << static_cast<int>(data[2])
                      << ", Length: " << actual_length << std::endl;

            // Uncomment the next line to move the cursor
            // moveCursor(data[1], data[2]);

            Sleep(1);  // Add a small delay to prevent CPU overuse
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    // Release the interface and close the device
    libusb_release_interface(handle, 0);
    libusb_close(handle);
    libusb_exit(ctx);

    return 0;
}
