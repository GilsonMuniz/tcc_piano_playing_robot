#include <iostream>
#include "tinyxml2.h"

using namespace tinyxml2;

int main() {
  XMLDocument doc;
  doc.LoadFile("titanic.xml");

  // check for errors while loading the file
  if (doc.ErrorID() != 0) {
    std::cout << "Error loading file: " << doc.ErrorStr() << std::endl;
    return 1;
  }

  // get the root element
  XMLElement* root = doc.RootElement();

  // loop through all child elements
  for (XMLElement* elem = root->FirstChildElement(); elem != NULL; elem = elem->NextSiblingElement()) {
    // get the element name and value
    const char* name = elem->Name();
    const char* value = elem->GetText();

    // print the element name and value
    std::cout << name << ": " << value << std::endl;
  }

  return 0;
}
