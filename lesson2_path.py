from pathlib import Path

smart_dir = Path('Smart_Folder')
smart_dir.mkdir(exist_ok=True)
smart_file = smart_dir / 'readme.txt'
smart_file.touch()
print('สร้างโฟลเดอร์และไฟล์ด้วย pathlib สำเร็จ!')