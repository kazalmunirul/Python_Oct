# f = open('data.txt', 'r')
# first_line = f.readline() # Reads the first line
# print(first_line)
# second_line = f.readline() # Reads the next line
# print(second_line)
# f.close()

# f = open('data.txt', 'w')  # 'w' overwrites or creates
# f.write("This is the first line!\n")
# f.write("This is another line.\n")
# print("Data written to output.txt")
# f.close()

# # Appending to a file (using 'a')
# f = open('data.txt', 'a')
# f.write("This line will be appended.\n")
# print("Data appended to data.txt")
# f.close()

# Reading with 'with'
with open('data.txt', 'r') as f:
    content = f.read()
    print(content)


with open('data.txt', 'w') as f:
        f.write("Hello from the 'with' statement.\n")
        f.write("This file will auto-close.\n")
print("Data written to data.txt")

