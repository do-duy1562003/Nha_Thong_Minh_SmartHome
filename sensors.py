# sensors.py - Đọc cảm biến nhiệt độ, độ ẩm và chuyển động

import Adafruit_DHT
import gpiozero
import time

# Chân kết nối
DHT_PIN = 4         # GPIO4
PIR_PIN = 17        # GPIO17

pir = gpiozero.MotionSensor(PIR_PIN)

def read_dht():
    sensor = Adafruit_DHT.DHT11
    humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT_PIN)
    if humidity is None or temperature is None:
        return (0, 0)
    return (round(temperature, 1), round(humidity, 1))

def detect_motion():
    return pir.motion_detected

