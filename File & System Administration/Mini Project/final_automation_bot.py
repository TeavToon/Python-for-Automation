import os
import csv
import time
import shutil

print("========== 🚀 Final Project: Accounting Automation Bot ==========")

# ==========================================
# ส่วนที่ 1: เตรียมความพร้อม (Setup & Configuration)
# ==========================================
inbox_folder = 'My_Inbox'
archive_folder = 'Archive_CSV'

# 1.1 เช็คและสร้างโฟลเดอร์
print("\n--- 1. ตรวจสอบและสร้างโฟลเดอร์ ---")
list_folder = [inbox_folder, archive_folder]
for folder in list_folder:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"📁 สร้างโฟลเดอร์ '{folder}' เรียบร้อยแล้ว")
    else:
        print(f"📁 มีโฟลเดอร์ '{folder}' อยู่แล้ว")

# 1.2 สร้างไฟล์จำลอง 10 ไฟล์ไว้ใน Inbox
print("\n--- 2. สร้างข้อมูลจำลอง (Dummy Data) ---")
data = [
    ["ชื่อ", "แผนก", "เงินเดือน"],
    ["สมชาย", "IT", "30000"],
    ["สมหญิง", "HR", "25000"],
    ["สมศักดิ์", "IT", "35000"]
]

for i in range(1, 11):
    dummy_file_path = os.path.join(inbox_folder, f'staff_data_{i}.csv')

    # เช็คก่อนว่ามีไฟล์จำลองหรือยัง ถ้ายังไม่มีให้สร้าง
    if not os.path.exists(dummy_file_path):
        with open(dummy_file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"📄 สร้างสมุดบัญชีจำลอง: {dummy_file_path}")


print("\n🤖 บอทนักบัญชีพร้อมทำงาน! กำลังเฝ้าระวังโฟลเดอร์ Inbox...")
print("-" * 50)

# ==========================================
# ส่วนที่ 2: บอทเริ่มเฝ้าระวัง (Main Loop)
# ==========================================
try:
    while True:
        time.sleep(3)  # หน่วงเวลา 3 วินาที
        files = os.listdir(inbox_folder)
        
        for file_name in files:
            # กรองเฉพาะไฟล์ .csv
            if file_name.endswith('.csv'):
                source_path = os.path.join(inbox_folder, file_name)
                target_path = os.path.join(archive_folder, file_name)
                hr_total_salary = 0
                
                try:
                    # 2.1 เปิดอ่านไฟล์ CSV
                    with open(source_path, 'r', encoding='utf-8') as file:
                        reader = csv.reader(file)
                        next(reader) # ข้ามหัวตาราง
                        for row in reader:
                            if row[1] == 'HR':
                                hr_total_salary += int(row[2])
                    
                    # 2.2 รายงานผล
                    print(f"📊 ตรวจพบไฟล์: {file_name}")
                    print(f"💰 เงินเดือนรวมของพนักงาน HR คือ {hr_total_salary} บาท")

                    # 2.3 ย้ายไฟล์ไปเก็บที่ Archive
                    shutil.move(source_path, target_path)
                    print(f"✅ ย้ายไฟล์ไปที่ {archive_folder} เรียบร้อยแล้ว\n")
                    
                except Exception as e:
                    # จัดการ Error ระดับไฟล์ (ถ้าพังที่ไฟล์นี้ ไฟล์อื่นยังไปต่อได้)
                    print(f"❌ เกิดข้อผิดพลาดในการจัดการไฟล์ {file_name}: {e}\n")

# เพิ่ม Error Handling ระดับโปรแกรม (จับการกด Ctrl + C ของเรา)
except KeyboardInterrupt:
    print("\n🛑 ได้รับคำสั่งหยุดการทำงาน... บอทขอตัวไปพักผ่อนครับ!")
    print("========== 🎉 จบการทำงาน ==========")