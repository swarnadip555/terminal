import time
import random
import psutil   # install using: pip install psutil
from datetime import datetime
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_fake_data():
    """Simulate telemetry data like temperature, speed, and voltage"""
    return {
        "Temperature (°C)": round(random.uniform(25, 80), 2),
        "Speed (km/h)": round(random.uniform(0, 120), 2),
        "Battery Voltage (V)": round(random.uniform(11.5, 13.0), 2),
        "CPU Usage (%)": psutil.cpu_percent(interval=0.5),
        "Memory Usage (%)": psutil.virtual_memory().percent,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def display_telemetry(data):
    """Pretty print telemetry data"""
    print("="*60)
    print(f"🛰️  SWARNADIP'S PROJECT TELEMETRY SYSTEM")
    print("="*60)
    for key, value in data.items():
        print(f"{key:<25}: {value}")
    print("="*60)

def main():
    try:
        while True:
            clear_terminal()
            telemetry_data = generate_fake_data()
            display_telemetry(telemetry_data)
            time.sleep(2)  # Update every 2 seconds
    except KeyboardInterrupt:
        print("\nTelemetry stopped manually.")

if __name__ == "__main__":
    main()
