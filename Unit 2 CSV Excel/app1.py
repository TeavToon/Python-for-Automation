import csv

# # ข้อมูลพนักงานจำลอง
# data = [
#     ["ชื่อ", "แผนก", "เงินเดือน"],
#     ["สมชาย", "IT", "30000"],
#     ["สมหญิง", "HR", "25000"],
#     ["สมศักดิ์", "IT", "35000"]
# ]

# # สร้างไฟล์แบบ 'w' (write - เขียน)
# with open('staff_data.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# print("สร้างสมุดบัญชี staff_data.csv สำเร็จ!")

# 'r' ย่อมาจาก read (โหมดอ่านอย่างเดียว)
# encoding='utf-8' เพื่อให้มันอ่านภาษาไทยได้ไม่เพี้ยน
# with open('ชื่อไฟล์.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file) # สวมแว่นตาอ่านตาราง
#     for row in reader:        # ไล่อ่านทีละบรรทัด
#         print(row)

# อ่านไฟล์ .csv
with open('staff_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)