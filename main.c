#include <windows.h>
#include <stdio.h>

typedef struct
{
    ULONGLONG idleTime;
    ULONGLONG kernelTime;
    ULONGLONG userTime;
} CpuTimes;

ULONGLONG FileTimeToULL(FILETIME ft)
{
    return (((ULONGLONG)ft.dwHighDateTime) << 32) | ft.dwLowDateTime;
}

void GetCpuTimes(CpuTimes *times)
{
    FILETIME idleTime, kernelTime, userTime;
    if (GetSystemTimes(&idleTime, &kernelTime, &userTime))
    {
        times->idleTime = FileTimeToULL(idleTime);
        times->kernelTime = FileTimeToULL(kernelTime);
        times->userTime = FileTimeToULL(userTime);
    }
    else
    {
        fprintf(stderr, "Failed to get system times.\n");
    }
}

double CalculateCpuLoad(CpuTimes *prev, CpuTimes *curr)
{
    ULONGLONG idleDiff = curr->idleTime - prev->idleTime;
    ULONGLONG totalDiff = (curr->kernelTime - prev->kernelTime) + (curr->userTime - prev->userTime);

    if (totalDiff == 0)
    {
        return 0.0; 
    }

    return (1.0 - ((double)idleDiff / totalDiff)) * 100.0;
}

HANDLE openSerialPort(const char *portName)
{
    HANDLE hSerial = CreateFile(portName,
                                GENERIC_READ | GENERIC_WRITE,
                                0,
                                NULL,
                                OPEN_EXISTING,
                                0,
                                NULL);

    if (hSerial == INVALID_HANDLE_VALUE)
    {
        printf("Error opening serial port %s.\n", portName);
        return INVALID_HANDLE_VALUE;
    }

    DCB dcbSerialParams = {0};
    dcbSerialParams.DCBlength = sizeof(dcbSerialParams);

    if (!GetCommState(hSerial, &dcbSerialParams))
    {
        printf("Error getting serial port state.\n");
        CloseHandle(hSerial);
        return INVALID_HANDLE_VALUE;
    }

    dcbSerialParams.BaudRate = CBR_9600;
    dcbSerialParams.ByteSize = 8;
    dcbSerialParams.StopBits = ONESTOPBIT;
    dcbSerialParams.Parity = NOPARITY;

    if (!SetCommState(hSerial, &dcbSerialParams))
    {
        printf("Error setting serial port parameters.\n");
        CloseHandle(hSerial);
        return INVALID_HANDLE_VALUE;
    }

    COMMTIMEOUTS timeouts = {0};
    timeouts.ReadIntervalTimeout = 50;
    timeouts.ReadTotalTimeoutConstant = 50;
    timeouts.ReadTotalTimeoutMultiplier = 10;
    timeouts.WriteTotalTimeoutConstant = 50;
    timeouts.WriteTotalTimeoutMultiplier = 10;

    if (!SetCommTimeouts(hSerial, &timeouts))
    {
        printf("Error setting serial port timeouts.\n");
        CloseHandle(hSerial);
        return INVALID_HANDLE_VALUE;
    }

    return hSerial;
}

void writeSerialPort(HANDLE hSerial, const char *data)
{
    DWORD bytesWritten;
    if (!WriteFile(hSerial, data, strlen(data), &bytesWritten, NULL))
    {
        printf("Error writing to serial port.\n");
    }
    else
    {
        printf("Sent %d bytes: %s\n", bytesWritten, data);
    }
}

void readSerialPort(HANDLE hSerial)
{
    char buffer[128];
    DWORD bytesRead;
    if (ReadFile(hSerial, buffer, sizeof(buffer) - 1, &bytesRead, NULL))
    {
        buffer[bytesRead] = '\0'; // Null-terminate the string
        printf("Received %d bytes: %s\n", bytesRead, buffer);
    }
    else
    {
        printf("Error reading from serial port.\n");
    }
}

int main()
{
    CpuTimes prev, curr;
    const char *portName = "COM8"; // Replace with your port

    // Open the serial port
    HANDLE hSerial = openSerialPort(portName);
    if (hSerial == INVALID_HANDLE_VALUE)
    {
        return 1;
    }

    // Initial CPU times
    GetCpuTimes(&prev);

    while (1)
    {
        Sleep(1000);

        // Get current CPU times
        GetCpuTimes(&curr);

        // Calculate and display CPU load
        double cpuLoad = CalculateCpuLoad(&prev, &curr);
        printf("CPU Load: %.2f%%\n", cpuLoad);

        if (cpuLoad >= 0 && cpuLoad <= 30)
        {
            writeSerialPort(hSerial, "C");
        }
        else if (cpuLoad > 30 && cpuLoad <= 60)
        {
            writeSerialPort(hSerial, "B");
        }
        else if (cpuLoad > 60 && cpuLoad <= 100)
        {
            writeSerialPort(hSerial, "A");
        }
        

        // Read response from Arduino
        readSerialPort(hSerial);

        // Update previous times
        prev = curr;
    }

    // Cleanup
    CloseHandle(hSerial);
    return 0;
}
