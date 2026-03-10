import os
import shutil

# --- [ 1. CONFIGURATION & SETUP ] ---
# กำหนดชื่อโฟลเดอร์หลักและโฟลเดอร์เป้าหมาย
sandbox_folder = "My_Sandbox"
target_folder  = os.path.join(sandbox_folder, "DLL_Files")

# สร้างโฟลเดอร์ Sandbox ถ้ายังไม่มี
if not os.path.exists(sandbox_folder):
    os.mkdir(sandbox_folder)
    print(f"Directory '{sandbox_folder}' created.")

# สร้างไฟล์จำลอง (Fake Files) สำหรับทดสอบ
for i in range(1, 6):
    # สร้างทั้งไฟล์ .dll และ .txt ผสมกัน
    open(os.path.join(sandbox_folder, f"fake_tool_{i}.dll"), "w").close()
    open(os.path.join(sandbox_folder, f"document_{i}.txt"), "w").close()

print("--- Setup Complete: Sandbox and fake files are ready! ---\n")


# --- [ 2. PROCESSING: MOVE DLL FILES ] ---
# ตรวจสอบและสร้างโฟลเดอร์ปลายทางสำหรับเก็บ DLL
if not os.path.exists(target_folder):
    os.mkdir(target_folder)
    print(f"Created target folder: {target_folder}")

# ดึงรายชื่อไฟล์จาก Sandbox
file_list = os.listdir(sandbox_folder)

print("Starting to move files...")
for name in file_list:
    # กรองเฉพาะไฟล์ .dll
    if name.endswith(".dll"):
        source_path = os.path.join(sandbox_folder, name)
        destination = os.path.join(target_folder, name)
        
        # ดำเนินการย้ายไฟล์
        shutil.move(source_path, destination)
        print(f"[SUCCESS] Moved: {name} -> {target_folder}")


# --- [ 3. SUMMARY ] ---
print("\n--- All tasks completed successfully! ---")