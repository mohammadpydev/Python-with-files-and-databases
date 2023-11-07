# Working with JSON
---
JSON (JavaScript Object Notation) is a lightweight data interchange format that is commonly used to represent data in a structured way. Here's an example of how to read from and write to JSON files, as well as how to work with JSON data strings.

### 1. Working with JSON Files:
Let's start with reading from and writing to JSON files.
 - #### Reading from a JSON File:
   Assume you have a JSON file called "data.json" with the following content:

   ```py
   {
    "name": "John",
    "age": 30,
    "city": "New York"
   }
   ```
   You can read this JSON file in Python:

   ```py
   import json

     # Reading from a JSON file
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)

     # Now, 'data' is a Python dictionary containing  the JSON data
    print(data)
   ```
 - #### Writing to a JSON File:
   Now, if you want to write data to a JSON file, you can do the following:
   
   ```py
   import json

    # Data to be written to the JSON file
    data = {
        "name": "Alice",
        "age": 25,
        "city": "Los Angeles"
    }

    # Writing to a JSON file
    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
   ```
   In this code, the json.dump() function writes the Python dictionary data to a JSON file, and the indent parameter is used for pretty-printing.

### 2. Working with JSON Data Strings:
You can also work with JSON data strings directly in Python. 
  - #### Parsing JSON Data from a String:
    You can parse this JSON data string into a Python dictionary:

    ```py
    import json

    json_data_string = '{"name": "Alice", "age": 25, "city": "Los Angeles"}'

    data = json.loads(json_data_string)

    # Now, 'data' is a Python dictionary
    print(data)
    ```  
  - #### Creating a JSON Data String from a Dictionary:
    Conversely, you can create a JSON data string from a Python dictionary like this:

    ```py
    import json

    data = {
        "name": "Alice",
        "age": 25,
        "city": "Los Angeles"
    }

    json_data_string = json.dumps(data)

    # Now, 'json_data_string' is a JSON-formatted string
    print(json_data_string)
    ```

These examples demonstrate how to work with JSON files and JSON data strings in Python. JSON is a versatile format for data interchange, and Python's json module makes it easy to work with JSON data.