# CSV Files
___

Interacting with CSV (Comma-Separated Values) files in Python is a common task. Python provides a built-in module called `csv` that makes it easy to read from and write to CSV files. Here's a basic guide on how to interact with CSV files in Python:
### 1. Reading CSV Files:
In this example, ***example.csv*** is the name of your CSV file. The `csv.reader` object allows you to iterate over the rows in the CSV file.

```py
import csv

# Open the CSV file for reading
with open('example.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        print(row)
```


### 2. Writing to CSV Files:
In this example, output.csv is the name of the CSV file you want to create. The `csv.writer` object allows you to write rows to the CSV file.
```py
import csv

# Data to be written to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Alice', 30, 'London'],
    ['Bob', 22, 'Paris']
]

# Open the CSV file for writing
with open('output.csv', 'w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)

    # Write the data to the CSV file
    csv_writer.writerows(data)
```

### 3. Reading CSV Files with Headers:
If your CSV file has headers, you can use the `csv.DictReader` class to read the file into a list of dictionaries:
```py
import csv

# Open the CSV file for reading
with open('example.csv', 'r') as file:
    # Create a CSV DictReader object
    csv_reader = csv.DictReader(file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        print(row['Name'], row['Age'], row['City'])

```

### 4. Writing to CSV Files with Headers:
```py
import csv

# Data to be written to the CSV file
data = [
    {'Name': 'John', 'Age': 25, 'City': 'New York'},
    {'Name': 'Alice', 'Age': 30, 'City': 'London'},
    {'Name': 'Bob', 'Age': 22, 'City': 'Paris'}
]

# Open the CSV file for writing
with open('output.csv', 'w', newline='') as file:
    # Specify the field names (headers)
    fieldnames = ['Name', 'Age', 'City']

    # Create a CSV DictWriter object
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header to the CSV file
    csv_writer.writeheader()

    # Write the data to the CSV file
    csv_writer.writerows(data)
```
> :bulb: **Tip:** for mor information visit [CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)