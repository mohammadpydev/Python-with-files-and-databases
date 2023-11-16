import csv

class CSVHandler:
    def __init__(self, file_name, fieldnames=None):
        self.file_name = file_name
        self.fieldnames = fieldnames

    def read_csv(self):
        data = []
        with open(self.file_name, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        return data

    def read_csv_dict(self):
        data = []
        with open(self.file_name, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data

    def write_csv(self, data):
        with open(self.file_name, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)

    def write_csv_dict(self, data):
        with open(self.file_name, 'w', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(data)

# Example usage:
csv_handler = CSVHandler('example.csv', fieldnames=['Name', 'Age', 'City'])

# Writing data to CSV
data_to_write = [['John', 25, 'New York'], ['Alice', 30, 'London'], ['Bob', 22, 'Paris']]
csv_handler.write_csv(data_to_write)

# Reading data from CSV
read_data = csv_handler.read_csv()
print("Data read from CSV:")
print(read_data)

# Writing data to CSV with headers
data_to_write_dict = [
    {'Name': 'John', 'Age': 25, 'City': 'New York'},
    {'Name': 'Alice', 'Age': 30, 'City': 'London'},
    {'Name': 'Bob', 'Age': 22, 'City': 'Paris'}
]
csv_handler.write_csv_dict(data_to_write_dict)

# Reading data from CSV with headers
read_data_dict = csv_handler.read_csv_dict()
print("\nData read from CSV with headers:")
print(read_data_dict)
