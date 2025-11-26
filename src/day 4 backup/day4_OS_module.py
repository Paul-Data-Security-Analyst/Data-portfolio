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
# shutil.copy("day 4/sample3.json","backup/sample_3_backup.json")
# # copying an entire folder to 'backup'
# shutil.copytree("day 4","new")
# # moving a file to 'backup'
# importing os and shutil
import os
import shutil
# creating source and backup variables
src = "day 4"
bck = "day 4 backup"
# shutil.move("backup/sample2.csv","day 4")
# creating backup folder if it doesn't exist
if not os.path.exists(bck):
    os.makedirs(bck)
    print("Backup folder created")
# listing all files in source folder
files = os.listdir(src)
# looping through each files in source folder and printing their respective filenames
for f in files:
        # creating source_path var & copying it into backup_path var using 'shutil'
        source_path = os.path.join(src,f)
        backup_path = os.path.join(bck,f)
        shutil.copy(source_path,backup_path)
        print(f"file copied from source_folder: {f}")
        print("The backup path : ",backup_path)



