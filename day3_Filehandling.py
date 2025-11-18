# file_read_demo.py
# with open("secure_note.txt", "w") as file:
#     file.write("I went into Interstellar. It was fun!! and thrilling")
#     file.write("\n---Now the txt file has been overwritten---\n")
#
# with open("secure_note.txt", "r") as file:
#     data = file.readline()
#     print(data)
#     data = file.readline()
#     print(data)

# .csv file Handling

# import csv
#
# employees = [["Name","Age", "Gender"],["Paul", "25", "Male"], ["Grace", "29", "Female"]]
#
# with open("employee_data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerows(employees)

# Reading a .csv file using csv.reader() method
# with open("employee_data.csv", "r") as file:
#     data = csv.reader(file)
#     for row in data:
#         print("---",row,"---")
# print()
#
# # reading a .csv file using file.read() method
# with open("employee_data.csv", "r") as file:
#     data = file.read()
#     print(data)

# JSON file Handling
#
# import json
#
# user_data = {"Name":"Madhavan","Age":"29","Gender":"Female","Name1":"Malik","Gender1":"Male","Age1":"25"}
# # .json file writing using the data
# with open("json_data.json", "w") as file:
#     json.dump(user_data, file, indent=4)
#     print("\nJSON file created successfully!!\n")
# # .json file reading using json.load(file) function
# with open("json_data.json", "r") as file:
#     data = json.load(file)
#     print("Entire Data :", data)

# Exception Handling - Error Handling
# try:
#     with open("Secure_log.txt", "r") as file:
#         data = file.read()
#         print("Data is being Read")
#         print(data)
#
# except FileNotFoundError:
#     print("⚠️ The requested File Not Found, creating a new log....")
#     open("Secure.txt", "w").close()
#     print("File created, successfully")
# except Exception as e:
#     print("Unexpected Error")
# finally:
#     print("🟢 Operation Completed successfully!!! ")

# User_defined data logger - JSON
# import json
#
# message = input("Enter your secret message: ")
#
# with open("secure_note.json", "w") as file:
#     json.dump(message,file, indent=4)
#
# with open("secure_note.json", "r") as file:
#     data = json.load(file)
#     print("Your Secret Message: ",data)
#
# # User_defined data logger - csv
# import csv
#
# message = input("Enter your secret message: ")
#
# with open("secure_note.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerows(message)
#
# with open("secure_note.csv","r") as f:
#     data = csv.reader(f)
#     for row in f:
#         print(row)












