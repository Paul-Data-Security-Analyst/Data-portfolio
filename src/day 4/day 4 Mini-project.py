#---------------“Data Intake + Secure Backup System”------------------
# importing libraries
import csv
import os
import shutil
import json
from datetime import datetime
import hashlib

# setup folder
os.makedirs("Intake",exist_ok=True)
os.makedirs("Backup", exist_ok=True)
log_text = "logs.txt"
Hash_db = "hash_db.json"

# initialize hash_db if missing
if not os.path.exists(Hash_db):
    with open(Hash_db, "w") as f:
        json.dump({}, f, indent =4)

# User-input for .txt file
user_data = input("Enter Name, Age, Email (comma separated) :")
file_txt = "Intake/data.txt"
with open(file_txt, "w") as f:
    f.write(user_data)

# converting user_data into a .csv file
name,age,email = ([item.strip() for item in user_data.split(',')])
file_csv = "Intake/data2.csv"
with open(file_csv,"w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Age","Email"])
    writer.writerow([name,age,email])

# convert to .json file
file_json = "Intake/data3.json"
with open(file_json, "w") as f:
    json.dump({"Name":name,"Age":age,"Email":email}, f,indent = 4)

# generate hash
def generate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file :
        while chunk := file.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

# hash store in json format
files = [file_txt,file_csv,file_json]

with open(Hash_db,"r") as f:
    hash_records = json.load(f)
for file in files:
    hash_value = generate_hash(file)
    hash_records[file] = hash_value
with open(Hash_db, "w") as f:
    json.dump(hash_records, f, indent = 4)

# backup hash generation & compare for integrity
for file in files:
    dest = os.path.join("Backup",os.path.basename(file))
    shutil.copy(file,dest)

    original_hash = hash_records[file]
    backup_hash = generate_hash(dest)

    status = 'OK' if original_hash ==backup_hash else "CORRUPT"
    with open(log_text, "a") as log:
        log.write(f"{datetime.now()} | {file} --> {status}\n")
print("Data Intake + Backup + Integrity Check --> Completed Successfully")