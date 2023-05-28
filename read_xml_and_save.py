import xml.etree.ElementTree as ET

def save_xml_as_text(filename, output_filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    output = f'Root element: {root.tag}\n\n--- XML Content ---\n'
    output += element_to_string(root)

    with open(output_filename, 'w') as file:
        file.write(output)

def element_to_string(element, indent=''):
    output = f'{indent}<{element.tag}>\n'

    for child in element:
        output += element_to_string(child, indent + "  ")

    if element.text and element.text.strip():
        output += f'{indent}  {element.text.strip()}\n'

    output += f'{indent}</{element.tag}>\n'
    return output

# Usage example
xml_file = 'titanic.xml'
output_file = 'titanic.txt'
save_xml_as_text(xml_file, output_file)
