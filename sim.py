import serial
import time
import random

def simulate_serial_data(port, baudrate=9600, interval=1):
    try:
        ser = serial.Serial(port, baudrate)
        print(f"Simulating data on {port}. Press Ctrl+C to stop.")
        while True:
            rate_act = random.randint(2, 8)
            data = f"7,100,{rate_act}\n".encode('utf-8')
            ser.write(data)
            print(f"Sent: {data.decode('utf-8').strip()}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Stopped.")
        ser.close()

simulate_serial_data('COM11')  # Replace 'COMx' with your COM port
