file_name = input("Enter the filename: ")
try:
    lines = open(file_name).readlines()
except:
    print("File not found.")
    exit()

while True:
    print(f"Number of lines: {len(lines)}")
    n = int(input("Enter a line number (0 to quit): "))
    if n == 0:
        break
    if 1 <= n <= len(lines):
        print(lines[n-1].rstrip())
    else:
        print("Invalid line number.")
