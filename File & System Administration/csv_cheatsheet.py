import csv

print("========== 📘 CSV Handling Cheatsheet ==========")

# ==========================================
# หมวดที่ 1: การสร้างและเขียนไฟล์ CSV (Write)
# ==========================================
print("\n--- 1. การสร้างและเขียนไฟล์ CSV ---")
# ข้อมูลพนักงานจำลอง
data = [
    ["ชื่อ", "แผนก", "เงินเดือน"],
    ["สมชาย", "IT", "30000"],
    ["สมหญิง", "HR", "25000"],
    ["สมศักดิ์", "IT", "35000"]
]

# 'w' ย่อมาจาก write (เขียน), newline='' ป้องกันบรรทัดว่างแทรก, encoding='utf-8' เพื่อให้อ่านภาษาไทยได้
with open('staff_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("✅ สร้างสมุดบัญชี staff_data.csv สำเร็จ!")


# ==========================================
# หมวดที่ 2: การอ่านไฟล์ CSV แบบปกติ (Read All)
# ==========================================
print("\n--- 2. การอ่านข้อมูลทั้งหมดในไฟล์ ---")
# 'r' ย่อมาจาก read (โหมดอ่านอย่างเดียว)
with open('staff_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file) # สวมแว่นตาอ่านตาราง
    for row in reader:        # ไล่อ่านทีละบรรทัด
        print(row)


# ==========================================
# หมวดที่ 3: การอ่านและกรองข้อมูล (Filter Data)
# ==========================================
print("\n--- 3. การกรองข้อมูล (เฉพาะพนักงานแผนก IT) ---")
with open('staff_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # ข้ามหัวตาราง (บรรทัดแรก) ไป 1 สเต็ป
    
    for row in reader:
        # เช็คข้อมูลคอลัมน์ที่ 2 (Index 1) ว่าตรงกับ 'IT' หรือไม่
        if row[1] == 'IT':
            print(f"พนักงาน {row[0]} ได้เงินเดือน {row[2]}")


# ==========================================
# หมวดที่ 4: การนำข้อมูลมาคำนวณ (Calculate Data)
# ==========================================
print("\n--- 4. การคำนวณยอดรวม (โจทย์: งบประมาณรวมแผนก IT) ---")
total_it_salary = 0

with open('staff_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # ข้ามหัวตาราง
    
    for row in reader:
        if row[1] == 'IT':
            # ต้องแปลง String เป็น Integer ก่อนนำมาบวกเลข
            total_it_salary += int(row[2])
    
print(f"💰 งบประมาณรวมของแผนก IT คือ {total_it_salary} บาท")

print("\n========== 🎉 เสร็จสิ้นการทำงาน ==========")