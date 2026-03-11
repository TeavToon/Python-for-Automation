import os
import shutil

print("========== 📘 OS & Shutil Cheatsheet ==========")

# ==========================================
# หมวดที่ 1: การสร้างและการเชื่อมต่อที่อยู่ไฟล์ (Path)
# ==========================================
print("\n--- 1. การสร้างและเชื่อมต่อ Path ---")
folder = "My_Sandbox"
file = "test.dll"

# os.path.join() ช่วยรวมชื่อโฟลเดอร์กับไฟล์ให้ถูกต้องตามแต่ละระบบปฏิบัติการ 
# (Windows จะได้ My_Sandbox\test.dll ส่วน Mac จะได้ My_Sandbox/test.dll)
path = os.path.join(folder, file)
print(f"ที่อยู่ไฟล์ที่ได้เตรียมไว้: {path}")


# ==========================================
# หมวดที่ 2: การสร้างโฟลเดอร์และไฟล์จำลอง
# ==========================================
print("\n--- 2. การสร้างโฟลเดอร์และไฟล์จำลอง ---")
sandbox_folder = "My_Sandbox"

# 1. เช็คว่ามีโฟลเดอร์หรือยัง ถ้ายังไม่มีให้สร้าง (ป้องกัน Error)
if not os.path.exists(sandbox_folder):
    os.mkdir(sandbox_folder)
    print(f"📁 สร้างโฟลเดอร์ '{sandbox_folder}' สำเร็จ")

# 2. การสร้างไฟล์เปล่า (0 Byte) แบบเข้าใจง่าย: เปิด (w) -> ปิด
demo_path = os.path.join(sandbox_folder, "demo.dll")
f = open(demo_path, "w")
f.close() 

# 3. สร้างไฟล์จำลองหลายๆ ไฟล์รวดเดียว (เขียนแบบย่อบรรทัดเดียว)
for i in range(1, 4):
    open(os.path.join(sandbox_folder, f"fake_tool_{i}.dll"), "w").close()
    open(os.path.join(sandbox_folder, f"document_{i}.txt"), "w").close()
    
print("📄 สร้างไฟล์จำลอง .dll และ .txt อย่างละ 3 ไฟล์สำเร็จ!")


# ==========================================
# หมวดที่ 3: การกรองรายชื่อไฟล์และการย้ายไฟล์ (List, Filter, Move)
# ==========================================
print("\n--- 3. การกรองรายชื่อไฟล์และการย้ายไฟล์ ---")
target_folder = os.path.join(sandbox_folder, "DLL_Files")

# สร้างโฟลเดอร์เป้าหมายรอไว้
if not os.path.exists(target_folder):
    os.mkdir(target_folder)

# os.listdir() ดึงรายชื่อไฟล์ทั้งหมดที่อยู่ในโฟลเดอร์นั้นออกมาเป็น List
file_list = os.listdir(sandbox_folder)
print(f"พบไฟล์/โฟลเดอร์ทั้งหมด: {file_list}\n")

print("กำลังเริ่มคัดแยกและย้ายเฉพาะไฟล์ .dll...")
for name in file_list:
    # กรองเฉพาะชื่อไฟล์ที่ลงท้ายด้วย .dll
    if name.endswith(".dll"):
        source = os.path.join(sandbox_folder, name)
        destination = os.path.join(target_folder, name)
        
        # shutil.move(ต้นทาง, ปลายทาง)
        shutil.move(source, destination)
        print(f"✅ ย้ายสำเร็จ: {name} -> {target_folder}")

print("\n========== 🎉 เสร็จสิ้นภารกิจ ==========")