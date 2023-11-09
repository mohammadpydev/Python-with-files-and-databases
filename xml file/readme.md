# XML files
---
Working with XML files in Python using the `lxml` library is a powerful and efficient way to parse and manipulate XML data. Here's an example of how to read from and write to an **XML file** using `lxml`:

### 1. Reading from an XML File:

Let's say you have an XML file called `data.xml` with the following content:
```xml
<root>
    <person>
        <name>John</name>
        <age>30</age>
        <city>New York</city>
    </person>
</root>
```

You can read this XML file in Python:

```py 
from lxml import etree

# Parse the XML file
tree = etree.parse('data.xml')
root = tree.getroot()

# Access and print data from the XML
name = root.find('person/name').text
age = root.find('person/age').text
city = root.find('person/city').text

print(f"Name: {name}, Age: {age}, City: {city}")
```

### 2. Writing to an XML File:

Now, if you want to create a new XML file or update an existing one, you can do the following:

```py
from lxml import etree

# Create the root element
root = etree.Element('root')

# Create a person element
person = etree.SubElement(root, 'person')

# Add sub-elements to the person element
name = etree.SubElement(person, 'name')
name.text = 'Alice'
age = etree.SubElement(person, 'age')
age.text = '25'
city = etree.SubElement(person, 'city')
city.text = 'Los Angeles'

# Create an ElementTree
tree = etree.ElementTree(root)

# Write to an XML file
tree.write('output.xml', pretty_print=True, encoding='utf-8')
```

In this code, we manually construct the XML structure by creating elements and adding sub-elements to represent the data. Then, we create an ElementTree from the root element and use the write() method to save the data to the "output.xml" file.

The pretty_print=True argument in the write() method adds indentation for a more readable XML file. The encoding argument specifies the character encoding for the XML file.

These examples demonstrate how to read from and write to XML files using the lxml library in Python. lxml is a robust and efficient library for working with XML data.

> :bulb: **Tip:** for more information about [lxml library](https://lxml.de/)