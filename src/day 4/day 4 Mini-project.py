#--------------- Data Intake + Secure Backup System ------------------

import csv
import os
import shutil
import json
from datetime import datetime
import hashlib

# ------------------ Folder Setup ------------------
os.makedirs("Intake", exist_ok=True)
os.makedirs("Backup", exist_ok=True)

log_text = "logs.txt"
Hash_db = "hash_db.json"

# initialize hash_db if missing
if not os.path.exists(Hash_db):
    with open(Hash_db, "w") as f:
        json.dump({}, f, indent=4)

# ------------------ Validation Functions ------------------
def valid_name(name):
    return name.replace(" ", "").isalpha()

def valid_age(age):
    return age.isdigit() and 1 <= int(age) <= 120

def valid_email(email):
    return (
        "@" in email and
        "." in email and
        " " not in email and
        email.count("@") == 1
    )

# ------------------ User Input Loop ------------------
while True:
    raw_data = input("Enter 'Name','Age','Email' (comma separated : ")
    parts = ([items.strip() for items in raw_data.split(",")])
    if len(parts)!=3:
        print("❌ Input must contain exactly 3 fields: Name, Age, Email. Try again.")
        continue
    name,age,email = parts
    if not name or not age or not email:  #empty data input condition
        print("❌ Name, Age or Email cannot be empty. Try again.")
        continue
    name = name.title()  #clean formatting

    # Validate name
    if not valid_name(name):
        print("❌ Invalid name. Only letters & spaces allowed.")
        continue

    # Validate age
    if not valid_age(age):
        print("❌ Age must be a number between 1–120.")
        continue
    age = int(age)
    # Validate email
    if not valid_email(email):
        print("❌ Invalid email format. Try again.")
        continue
    print("✔ Input validated successfully.")
    break

# ------------------ File Creation ------------------
file_txt = "Intake/data.txt"
with open(file_txt, "w") as f:
    f.write(f"{name}, {age}, {email}")

file_csv = "Intake/data2.csv"
with open(file_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Email"])
    writer.writerow([name, age, email])

file_json = "Intake/data3.json"
with open(file_json, "w") as f:
    json.dump({"Name": name, "Age": age, "Email": email}, f, indent=4)

# ------------------ Hash Generator ------------------
def generate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

# ------------------ Hash Storage ------------------
files = [file_txt, file_csv, file_json]

with open(Hash_db, "r") as f:
    hash_records = json.load(f)

for file in files:
    hash_records[file] = generate_hash(file)

with open(Hash_db, "w") as f:
    json.dump(hash_records, f, indent=4)

# ------------------ Backup + Integrity Check ------------------
for file in files:
    dest = os.path.join("Backup", os.path.basename(file))
    shutil.copy(file, dest)

    original_hash = hash_records[file]
    backup_hash = generate_hash(dest)

    status = "OK" if original_hash == backup_hash else "CORRUPT"

    with open(log_text, "a") as log:
        log.write(f"{datetime.now()} | {file} --> {status}\n")

print("Data Intake + Backup + Integrity Check --> Completed Successfully")
