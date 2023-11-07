from textfilehandler import TextFileHandler

# Instantiate the TextFileHandler with a filename
file_handler = TextFileHandler('example.txt')

# Read from the file
content = file_handler.read_file()
print("File content:")
print(content)

# Write to the file
write_result = file_handler.write_file("New content\n")
print(write_result)

# Append to the file
append_result = file_handler.append_file("More content\n")
print(append_result)
