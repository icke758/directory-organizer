import os
import datetime

def folderName():
    now = datetime.now()
    month_number = f'{now.month:02d}' 
    return month_number


base_path = r''
FILE_TYPE = "WORKDIR"

client_list = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

for client_name in client_list:
    client_directory_path = os.path.join(base_path, client_name, FILE_TYPE, folderName())
    
    if os.path.isdir(client_directory_path):
        print(f"Directory exists: {client_directory_path}")
        for filename in os.listdir(client_directory_path):
            file_path = os.path.join(client_directory_path, filename)
            
            new_filename = f"{client_name}.pdf"
            new_file_path = os.path.join(client_directory_path, new_filename)
            
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} to {new_filename}")
    else:
        print(f"Directory does NOT exist: {client_directory_path}")