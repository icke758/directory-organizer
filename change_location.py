import os
import shutil

base_path = r''
destination_path = r''

os.makedirs(destination_path, exist_ok=True)

client_list = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

for client_name in client_list:
    client_directory_path = os.path.join(base_path, client_name, 'WORKDIR', 'MONTHYEAR')
    
    if os.path.isdir(client_directory_path):
        for filename in os.listdir(client_directory_path):
            if filename.endswith('.pdf'):
                file_path = os.path.join(client_directory_path, filename)
                
                destination_file_path = os.path.join(destination_path, f"{client_name}.pdf")
                
                shutil.copy2(file_path, destination_file_path)
                print(f"Copied: {filename} to {destination_file_path}")
    else:
        print(f"Directory does NOT exist: {client_directory_path}")
