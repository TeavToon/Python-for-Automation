import os
import shutil

# shutil.move(ที่อยู่ต้นทาง, ที่อยู่ปลายทาง)

source = "My_Sandbox/fake_tool_1.dll" # ต้นทาง (ไฟล์อยู่ที่นี่)
destination = "My_Sandbox/DLL_Files/fake_tool_1.dll" # ปลายทาง (อยากให้ไปอยู่ที่นี่)

shutil.move(source, destination)

# ไฟล์ fake_tool_1.dll จะหายไปจากโฟลเดอร์ด้านนอก แล้วเข้าไปอยู่ในโฟลเดอร์ DLL_Files แทน