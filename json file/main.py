from JSONfilehandler import JSONFileHandler

# Instantiate the JSONFileHandler with a filename
json_handler = JSONFileHandler('data.json')

# Read from the JSON file
data = json_handler.read_json()
print("JSON data:")
print(data)

# Write to the JSON file
new_data = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
}
write_result = json_handler.write_json(new_data, indent=4)
print(write_result)
