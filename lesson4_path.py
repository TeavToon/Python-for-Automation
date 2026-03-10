from pathlib import Path

# --- ตั้งค่าตำแหน่งโฟลเดอร์ ---
source_dir = Path("Smart_Folder")
archive_dir = Path("Archive_TXT")

# 1. สร้างโฟลเดอร์ปลายทาง (ถ้ายังไม่มี)
archive_dir.mkdir(exist_ok=True)

# 2. ตรวจสอบว่าโฟลเดอร์ต้นทางมีอยู่จริงหรือไม่ เพื่อป้องกัน Error
if source_dir.exists() and source_dir.is_dir():
    
    print(f"--- เริ่มต้นการย้ายไฟล์จาก {source_dir} ---")
    
    # 3. ค้นหาเฉพาะไฟล์ .txt และวนลูปย้ายไฟล์
    for file in source_dir.glob("*.txt"):
        target_path = archive_dir / file.name
        
        # ย้ายไฟล์ (เหมือนการตัด-วาง หรือ Cut & Paste)
        file.replace(target_path)
        
        print(f"✅ ย้ายสำเร็จ: {file.name} -> {archive_dir}")
        
else:
    print(f"❌ ไม่พบโฟลเดอร์ต้นทาง: {source_dir}")

print("--- เสร็จสิ้นภารกิจ ---")