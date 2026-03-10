text_file = 'My_Note.txt'

with open(text_file, 'w', encoding='utf-8') as file:
    file.write("สวัสดี! นี่คือข้อความจากบอท Automation\nฉันสามารถอ่านไฟล์ txt ได้สบายมาก!")

with open(text_file, 'r', encoding='utf-8') as file:
    contant = file.read()
    print(contant)