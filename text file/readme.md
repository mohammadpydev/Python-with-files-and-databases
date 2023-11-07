# Text File Handling
ext files are a common way to store and manipulate textual data in Python. You can perform tasks like reading from a text file, writing to a text file, and appending data to an existing text file. Here are some examples to get you started:

### 1. Reading from a Text File:
You can use the `open()` function to open a text file and read its contents. Here's an example of how to read from a text file:
```py
# Open a text file in 'read' mode ('r')
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)
```
In this example, `sample.txt` is the name of the text file you want to read. The with statement is used to ensure that the file is properly closed after you've finished reading its contents.

If you want to read the lines of a text file into a list where each line is an element in the list, you can do that by using a for loop. Here's an example:
```py
# Open a text file in 'read' mode ('r')
with open('sample.txt', 'r') as file:
lines = file.readlines()

# Now, 'lines' is a list where each element is a line from the file
for line in lines:
print(line, end='')
```
In this code, the `file.readlines()` method reads all the lines from the text file 'sample.txt' and stores them in the lines list. Each element in the list represents a line from the file.

You can then loop through the lines list to process each line, print them, or perform any other operations you need.
### 2. Writing to a Text File:
To write data to a text file, you can use the `write` mode ('w') with the open() function. If the file doesn't exist, it will be created; if it does exist, its previous content will be overwritten:
```py
# Open a text file in 'write' mode ('w')
with open('output.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a sample text file.")
```
This code will create or overwrite the file `output.txt` with the specified content.
### 3. Appending to a Text File:
To add content to an existing text file without overwriting its previous content, you can use the `append` mode ('a'):
```py
# Open a text file in 'append' mode ('a')
with open('output.txt', 'a') as file:
    file.write("\nAppending more data.")
```
This code appends the new content to the end of the 'output.txt' file.

### 4.Binary File:
Reading and writing binary files in Python is similar to working with text files, but you should open the files in binary mode `rb` for reading and 'wb' for writing. Here's how you can read from a binary file and write to a binary file:

- Reading from a Binary File:

  ```py
  # Open a binary file in 'read' mode ('rb')
    with open("downloaded_image.jpg", 'rb') as file:
        binary_data = file.read()
  ```
- Writing to a Binary File:
  ```py
  # Open a binary file in 'write' mode ('wb')
    with open("downloaded_image.jpg", "wb") as file:
        file.write(binary_data)
  ```
You may ask yourself why I convert the image to a binary file and vice versa. Sometimes we may have to convert the image to binary data in order to send it in some way.  

