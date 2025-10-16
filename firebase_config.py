# firebase_config.py - Kết nối Firebase Realtime Database

import firebase_admin
from firebase_admin import credentials, db

# Đường dẫn tới file key JSON tải từ Firebase Console
cred = credentials.Certificate("firebase-key.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://<your-database>.firebaseio.com/"
})

# Ghi dữ liệu cảm biến lên Firebase
def update_status(temp, hum, motion):
    ref = db.reference("/status")
    ref.update({
        "temperature": temp,
        "humidity": hum,
        "motion": motion
    })

# Lấy lệnh điều khiển từ Firebase
def get_commands():
    ref = db.reference("/commands")
    return ref.get()
