from pathlib import Path

# --- Configuration & Setup ---
smart_dir = Path("Smart_Folder")
smart_dir.mkdir(exist_ok=True)  # สร้างโฟลเดอร์ถ้ายังไม่มี เพื่อป้องกัน Error
smart_file = smart_dir / "readme.txt"

# --- File Operations ---
# 1. การเขียนไฟล์
smart_file.write_text("Hello, Smart Folder!", encoding="utf-8")

# 2. การอ่านไฟล์
content = smart_file.read_text(encoding="utf-8")
print(f"เนื้อหาในไฟล์: {content}")

# --- การค้นหาไฟล์ (Globbing) ---
print("\nรายชื่อไฟล์ .txt ที่พบ:")
# ใช้ .glob("*.txt") เพื่อค้นหาไฟล์ที่ลงท้ายด้วย .txt ทั้งหมดในโฟลเดอร์
for file in smart_dir.glob("*.txt"):
    print(f"- {file.name}")