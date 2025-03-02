import os

print("Current Directory:", os.getcwd())  # Shows where the script is running from
filename = input("Enter filename: ").strip()  # Remove any accidental spaces

if not os.path.exists(filename):
    print("File not found.")
else:
    print("File exists.")