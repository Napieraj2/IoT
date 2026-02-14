# LAB1 Runtime Instructions

## Prerequisites

- Raspberry Pi OS with Python 3.10+
- GPIO access enabled (`sudo raspi-config` → Interface Options → enable SPI/I2C as needed)
- Install sensor libraries from each module directory:
  - `pip install -r RFID/requirements.txt`
  - `pip install -r TEMP/requirements.txt`

## RANGER (HC-SR04 ultrasonic)

1. Wire TRIG to BCM 4, ECHO to BCM 17, and supply the sensor with 5 V (use a safe level shifter on the echo line).
2. From the `RANGER` directory, run `python3 ranger.py`.
3. The console refreshes every 0.1 s with the measured distance in centimetres. Press `Ctrl+C` to exit; GPIO pins auto-clean up.

## RFID (MFRC522)

1. Enable SPI on the Pi and wire the MFRC522 reader to the standard SPI pins (SDA=BCM 8, SCK=11, MOSI=10, MISO=9, RST=25, 3.3 V power).
2. Install requirements and then run from the `RFID` directory:
   - Read an existing tag: `python3 read.py`
   - Write text to a tag: `python3 write.py`
   - Exercise byte read/write loop: `python3 reading_writing.py`
3. Each script cleans up GPIO after completion; press `Ctrl+C` to break the looped demo.

## TEMP (DHT11 sensor)

1. Wire the DHT11 data pin through a 10 kΩ pull-up to 3.3 V and connect it to BCM 17.
2. Install requirements and run from the `TEMP` directory: `python3 DHT11.py`.
3. The terminal displays the last valid reading and the status of the most recent attempt, updating at 1 Hz. Interrupt with `Ctrl+C`.
