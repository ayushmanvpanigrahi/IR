import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse("New.xml")
root = tree.getroot()

# Print the expertise data
print("Expertise Data:")
for elem in root:
    for sublem in elem:
        print(sublem.text)

# Print child names and their text
print("\nChild Names and Text:")
for child in root.find('children'):
    print(f"Name: {child.attrib['name']}, Text: {child.text.strip()}")
    
    # If the child has grandchildren, print their data
    grandchildren = child.find('grandchildren')
    if grandchildren is not None:
        for data in grandchildren:
            print(f"  Grandchild Data: {data.text}")