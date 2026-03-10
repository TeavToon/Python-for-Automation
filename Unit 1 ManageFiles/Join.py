import os

folder = "My_Sandbox"
file = "test.dll"

# เหมือนเราบอก Python ว่า "ช่วยรวมชื่อโฟลเดอร์กับชื่อไฟล์ให้หน่อย"
path = os.path.join(folder, file)

# ผลลัพธ์ (บน Windows): "My_Sandbox\test.dll"
# ผลลัพธ์ (บน Mac): "My_Sandbox/test.dll"

# .join() คือ การสร้าง "แผนที่" หรือ "ที่อยู่" เตรียมเอาไว้เฉยๆ