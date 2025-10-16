# main.py - Chương trình chính hệ thống Smart Home Raspberry Pi

from sensors import read_dht, detect_motion
from devices import control_light, control_fan
from firebase_config import get_commands, update_status
from voice_control import listen_command
import time

print("=== HỆ THỐNG NHÀ THÔNG MINH - RASPBERRY PI 4 ===")

while True:
    # Đọc dữ liệu cảm biến
    temp, hum = read_dht()
    motion = detect_motion()

    # Cập nhật lên Firebase
    update_status(temp, hum, motion)

    # Lấy lệnh điều khiển từ Firebase
    cmd = get_commands()
    if cmd:
        control_light(cmd.get('light'))
        control_fan(cmd.get('fan'))

    # Nghe lệnh giọng nói
    listen_command()

    time.sleep(2)

