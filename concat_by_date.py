import os
import shutil
from datetime import datetime

filedirectory1 = r''
filedirectory2 = r''
emails_directory = r''

os.makedirs(emails_directory, exist_ok=True)

files_directory1 = [f for f in os.listdir(filedirectory1) if os.path.isfile(os.path.join(filedirectory1, f))]
files_directory2 = [f for f in os.listdir(filedirectory2) if os.path.isfile(os.path.join(filedirectory2, f))]

def get_last_modified_time(file_path):
    return os.path.getmtime(file_path)

def get_hour_minute(file_path):
    mod_time = get_last_modified_time(file_path)
    dt = datetime.fromtimestamp(mod_time)
    return (dt.hour, dt.minute)

file_times1 = {}
for filename in files_directory1:
    file_path = os.path.join(filedirectory1, filename)
    hour_minute = get_hour_minute(file_path)
    file_times1[hour_minute] = file_times1.get(hour_minute, []) + [filename]

file_times2 = {}
for filename in files_directory2:
    file_path = os.path.join(filedirectory2, filename)
    hour_minute = get_hour_minute(file_path)
    file_times2[hour_minute] = file_times2.get(hour_minute, []) + [filename]

for filename1 in files_directory1:
    file_path1 = os.path.join(filedirectory1, filename1)
    hour_minute1 = get_hour_minute(file_path1)

    if hour_minute1 in file_times2:
        folder_name = os.path.splitext(filename1)[0]
        folder_path = os.path.join(emails_directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        shutil.copy2(file_path1, folder_path)
        print(f"Copied {filename1} to {folder_path}")

        for filename2 in file_times2[hour_minute1]:
            file_path2 = os.path.join(filedirectory2, filename2)
            shutil.copy2(file_path2, folder_path)
            print(f"Copied {filename2} to {folder_path}")

    else:
        continue
