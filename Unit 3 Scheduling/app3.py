import os
import time

target_file = os.path.join('My_Sandbox', 'secret.txt')
while True:
    print("กำลังเฝ้าระวัง...")
    time.sleep(3)
    if os.path.exists(target_file):
        print("🚨 แจ้งเตือน! พบไฟล์ลับแล้ว! หยุดการทำงาน")
        break