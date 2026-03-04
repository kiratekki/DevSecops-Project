#the script first checks if the file exists in the file path and then reads the lines once its done reading it ptints last 10 lines or else it will throw error saying the file not found in case the file path is mismatching
import os

file_check = input("Enter the file path: ")

if os.path.exists(file_check):
    with open(file_check) as f:
        lines = f.readlines()
        for line in lines[-10:]:
            print(line)
else:
    print("Error File not found")
