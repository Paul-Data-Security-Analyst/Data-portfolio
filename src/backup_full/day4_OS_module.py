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
import shutil
import os
backup ="backup"
shutil.copy("day 4/sample1.txt","backup/")
# renaming 'filename' while copying into backup
shutil.copy("day 4/sample3.json","backup/sample_3_backup.json")
# copying an entire folder to backup
shutil.copytree("day 4/","backup_full/")