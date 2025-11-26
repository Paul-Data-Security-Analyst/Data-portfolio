Day 4 – Data Intake + Secure Backup System

This mini-project automates a full data-intake → backup → integrity-verification workflow.

What the script does

Creates required folders

Intake/

Backup/

Collects user input
Takes: Name, Age, Email
Saves them as:

data.txt

data2.csv

data3.json

Generates SHA-256 hashes
Calculates a hash for each file and stores it inside hash_db.json.

Creates secure backups
Copies files from Intake/ to Backup/.

Integrity verification
Re-hashes the backup files and checks if:

backup_hash == original_hash

Logs result in logs.txt

Final output
Prints:

Data Intake + Backup + Integrity Check → Completed Successfully
