# Ask the user for a filename.
# Use try-except to handle FileNotFoundError if the file doesn't exist, printing a user-friendly message.
# Also, include a generic except Exception as e: to catch any other potential I/O errors during file operations and print the error e.
# Use a finally block to print a message like "Attempted to read file [filename]." regardless of success or failure.


# try:
#     filename = input("Enter the filename: ")
#     with open(filename, 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found. Please check the filename and try again.")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     print(f"Attempted to read file {filename}.")    

def count_lines_in_file(filename):
 line_count = 0
 try:
    with open(filename, 'r') as file:
        for line in file:
            line_count  =  line_count +1
    print(f"The file '{filename}' has {line_count} lines.")
 except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
 except Exception as e:
    print(f"An unexpected error occurred: {e}")
 finally:
    print(f"Attempted to read file '{filename}'.")

if __name__ == "__main__":
    file_to_read = input("Enter the filename to read: ")
    count_lines_in_file(file_to_read)
