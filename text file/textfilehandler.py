class TextFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        """This method is used to read the content of the text file."""
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return "File not found"
        except Exception as e:
            return str(e)

    def write_file(self, content, mode='w'):
        """This method is used to write content to the text file."""
        try:
            with open(self.filename, mode) as file:
                file.write(content)
            return "File written successfully"
        except Exception as e:
            return str(e)

    def append_file(self, content):
        """This method is a convenience method for appending content to the text file."""
        return self.write_file(content, mode='a')


