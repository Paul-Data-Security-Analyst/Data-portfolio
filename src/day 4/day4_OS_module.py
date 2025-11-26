# # Importing OS module and displaying the files inside a folder
# import os
# folder = "test_folder"
# files = os.listdir(folder)
# print("The files are: ",files)
#
# # joining FUNCTION for "Folder"+"Filename"
# import os
# folder = "test_folder"
# files = os.listdir(folder)
#
# for file in files:
#     full_path = os.path.join(folder,file)
#     print(full_path)
#
# # Checking if a folder exists
# import os
# folder = "test_folder"
#
# if os.path.exists(folder):
#     print("Folder Exists!")
# else:
#     print("OOps!! Folder Not found")
#
# # If not folder found automatically create one
#
# import os
# if not os.path.exists(folder):
#     os.makedirs(folder)
#     print("New Folder Created!")
# else:
#     print("Folder Already Exists!")
#
# Test code
# import os
#
# folder = "day 4"
# files = os.listdir(folder)
#
# for f in files:
#     path_file =os.path.join(folder,f)
#     print(path_file)
#
# if os.path.exists(folder):
#     print("Folder already exits")
# else:
#     os.makedirs(folder)
#     print("New folder created")
#  Copy files from a folder using 'Shutil' tool
# import shutil
# import os
# backup ="backup"
# shutil.copy("day 4/sample1.txt","backup/")
# # renaming 'filename' while copying into backup
# shutil.copy("day 4/sample3.json","backup/sample3.json")
# # copying an entire folder to 'backup'
# shutil.copytree("day 4","new")
# # moving a file to 'backup'
# importing os and shutil
# import os
# import shutil
# creating source and backup variables
# src = "day 4"
# bck = "day 4 backup"
# # shutil.move("backup/sample2.csv","day 4")
# # creating backup folder if it doesn't exist
# if not os.path.exists(bck):
#     os.makedirs(bck)
#     print("Backup folder created")
# # listing all files in source folder
# files = os.listdir(src)
# # looping through each files in source folder and printing their respective filenames
# for f in files:
#         # creating source_path var & copying it into backup_path var using 'shutil'
#         source_path = os.path.join(src,f)
#         backup_path = os.path.join(bck,f)
#         shutil.copy(source_path,backup_path)
#         print(f"file copied from source_folder: {f}")
#         print("The backup path : ",backup_path)
# Function for generating a 'HASH file'
# import os
# import hashlib  #importing hash library
# def generate_hash(file_path):      #defining the hash generating function
#     if not os.path.exists(file_path):
#         print(f'[ERROR] File does not exists:{file_path}')
#         return  None
#     sha256 = hashlib.sha256()
#     try:                                #try block to generate and add chunks of data into hash object
#         with open(file_path,"rb") as f:
#             while chunk := f.read(4096): # chunks fed into sha256 object
#                 sha256.update(chunk)        #updating
#         return sha256.hexdigest()           #.hexdigest() modifies the binary 256-bit binary data into human-readable string
#     except FileNotFoundError:
#         return "File Not Found"
#     except Exception as e:                 # 'e' catches any error and throws the exact error message as a String
#         return f"Unexpected Error Found {file_path} {e}"
# # testing user input for file integrity
# src ="day 4/sample1.txt"
# bck = "backup/sample1.txt"
# h1 = generate_hash(src) # h1 - file from src folder
# h2 = generate_hash(bck)  # h2 - file from backup folder
# print("source_path",h1)
# print("backup_path",h2)
# if h1 == h2:
#     print("\nFile integrity is perfect")
# else:
#     print("\nFile corrupted!")

# Basic 'BACKUP' + 'INTEGRITY'
# importing necessary modules & libraries

import os
import shutil
import hashlib
import json
from csv import excel

# declaring Directories
SRC_DIR = "src"
BACKUP_DIR = "bck"
HASH_DB = "hash_db.json"

# ensuring if directories exist using a function
def ensure_directory():
    os.makedirs(SRC_DIR,exist_ok=True)
    os.makedirs(BACKUP_DIR,exist_ok=True)
# generate a hash function
def generate_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath,"rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except:
        return None
#  loading HASH_DB
def load_hash_db():
    if not os.path.exists(HASH_DB):
        return {}
    with open(HASH_DB, "r") as f:
        return json.load(f)
# save HASH_DB
def save_hash_db(db):
    with open(HASH_DB,"w") as f:
        json.dump(db,f, indent=2)

# MAIN FUNCTION
def backup_verify():
    ensure_directory()
    db = load_hash_db()
# listing src files
    src_files = os.listdir(SRC_DIR)
    for file in src_files:
        source_path = os.path.join(SRC_DIR,file)
        if os.path.isdir(source_path):
            continue
# generating Current Hash
        current_hash = generate_hash(source_path)
        if current_hash is None:
            print(f"Skipping unreadable file : {file}")
#  generating the previous hash
        previous_hash = db.get(file)

        if previous_hash is None:
            print(f"New File Detected : {file}")
        elif previous_hash != current_hash:
            print(f"Change Detected : {file}")
        else:
            print(f"No change detected : {file}")
            continue
# generating backup path & hash
        backup_path = os.path.join(BACKUP_DIR,file)
        shutil.copy2(source_path,backup_path)

        backup_hash = generate_hash(backup_path)

        if backup_hash == current_hash:
            print(f"No change Detected Integrity checked : OK :{file}")
            db[file] = current_hash
        else:
            print(f"Change Detected : No Integrity!!! {file}")

    save_hash_db(db)
    print("Backup Process Completed Successfully!!!")

backup_verify()







