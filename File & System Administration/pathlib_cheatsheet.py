from pathlib import Path

print("========== 📘 Pathlib Cheatsheet ==========")

# ==========================================
# หมวดที่ 1: การสร้างและเชื่อมต่อ Path
# ==========================================
print("\n--- 1. การจัดการ Path ---")
# สร้าง Path และต่อเลโก้เข้าด้วยกันด้วยเครื่องหมาย / (จัดการ \ หรือ / ให้โดยอัตโนมัติ)
work_dir = Path('Project_alpha')
file_final = work_dir / 'data' / 'summary.csv'
print(f"ที่อยู่ไฟล์ที่ได้: {file_final}")


# ==========================================
# หมวดที่ 2: การสร้างโฟลเดอร์และไฟล์
# ==========================================
print("\n--- 2. การสร้างโฟลเดอร์และไฟล์ ---")
smart_dir = Path('Smart_Folder')

# สร้างโฟลเดอร์ (exist_ok=True ช่วยป้องกัน Error ถ้ามีโฟลเดอร์นี้อยู่แล้ว)
smart_dir.mkdir(exist_ok=True)  

# สร้างไฟล์เปล่า (เหมือนคำสั่ง touch ใน Linux/Mac)
smart_file = smart_dir / 'readme.txt'
smart_file.touch()
print(f"✅ สร้างโฟลเดอร์ '{smart_dir.name}' และไฟล์ '{smart_file.name}' สำเร็จ!")


# ==========================================
# หมวดที่ 3: การเขียน อ่าน และค้นหาไฟล์
# ==========================================
print("\n--- 3. การเขียน อ่าน และค้นหาไฟล์ ---")
# 1. การเขียนไฟล์
smart_file.write_text("Hello, Smart Folder!", encoding="utf-8")

# 2. การอ่านไฟล์
content = smart_file.read_text(encoding="utf-8")
print(f"เนื้อหาที่อ่านได้: {content}")

# 3. การค้นหาไฟล์ (Globbing)
print("\nรายชื่อไฟล์ .txt ที่พบในโฟลเดอร์:")
for file in smart_dir.glob("*.txt"):
    print(f"- {file.name}")


# ==========================================
# หมวดที่ 4: การย้ายไฟล์ (Move / Replace)
# ==========================================
print("\n--- 4. การย้ายไฟล์ ---")
source_dir = Path("Smart_Folder")
archive_dir = Path("Archive_TXT")

# สร้างโฟลเดอร์ปลายทางรอไว้
archive_dir.mkdir(exist_ok=True)

# ตรวจสอบว่าโฟลเดอร์ต้นทางมีอยู่จริงหรือไม่ ป้องกันระบบพัง
if source_dir.exists() and source_dir.is_dir():
    print(f"เริ่มต้นการย้ายไฟล์จาก {source_dir.name} ไปยัง {archive_dir.name}...")
    
    # ค้นหาเฉพาะไฟล์ .txt และวนลูปย้ายไฟล์
    for file in source_dir.glob("*.txt"):
        target_path = archive_dir / file.name
        
        # ย้ายไฟล์ (เหมือนการตัด-วาง Cut & Paste)
        file.replace(target_path)
        print(f"✅ ย้ายสำเร็จ: {file.name} -> {archive_dir.name}")
        
else:
    print(f"❌ ไม่พบโฟลเดอร์ต้นทาง: {source_dir.name}")

print("\n========== 🎉 เสร็จสิ้นการทำงาน ==========")