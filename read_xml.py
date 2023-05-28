import xml.etree.ElementTree as ET

def print_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    print(f"Root element: {root.tag}")

    print("\n--- XML Content ---")
    print_element(root)

def print_element(element, indent=""):
    print(f"{indent}<{element.tag}>")

    for child in element:
        print_element(child, indent + "  ")

    if element.text and element.text.strip():
        print(f"{indent}  {element.text.strip()}")

    print(f"{indent}</{element.tag}>")

# Usage example
xml_file = "titanic.xml"
print_xml(xml_file)
