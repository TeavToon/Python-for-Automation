from pathlib import Path

# # 1. เสกข้อความธรรมดาให้กลายเป็นเลโก้ Path
# base_folder = Path("My_Sandbox")

# # 2. ต่อเลโก้เข้าด้วยกันด้วยเครื่องหมาย /
# # (บอทจะรู้เองว่า Windows ต้องใช้ \ และ Mac ต้องใช้ / เราไม่ต้องปวดหัวเลย)
# full_path = base_folder / "DLL_Files" / "test.dll"

# print(full_path) 
# # ผลลัพธ์: My_Sandbox\DLL_Files\test.dll (บน Windows)

work_dir = Path('Project_alpha')
file_final = work_dir / 'data' / 'summary.csv'
print(file_final)