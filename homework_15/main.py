import os
import shutil


base_dir = "notes_archive"
os.makedirs(base_dir, exist_ok=True)


days = ["monday", "wednesday", "friday"]
for day in days:
    day_path = os.path.join(base_dir, day)
    os.makedirs(day_path, exist_ok=True)
    note_path = os.path.join(day_path, "note1.txt")
    with open(note_path, "w", encoding="utf-8") as file:  
        file.write(f"Бүгүнкү сабак ({day})")


wednesday_path = os.path.join(base_dir, "wednesday")
if os.path.exists(wednesday_path):
    shutil.rmtree(wednesday_path)


for root, dirs, files in os.walk(base_dir):
    print(f"Каталог: {root}")
    if dirs:
        print(f"Папкалар: {dirs}")
    if files:
        print(f"Файлдар: {files}")