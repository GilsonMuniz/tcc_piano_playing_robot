#include <iostream>
#include "tinyxml2.h"
#include "tinyxml2.cpp"

// compilar: "C:\Program Files (x86)\Falcon\MinGW\bin\g++.exe" -g C:\Users\Gilson\Documents\GitHub\tcc_piano_playing_robot\read_xml.cpp -o C:\Users\Gilson\Documents\GitHub\tcc_piano_playing_robot\read_xml.exe
// executar: C:\Users\Gilson\Documents\GitHub\tcc_piano_playing_robot\read_xml.exe


using namespace tinyxml2;
using namespace std;

int main()
{
	XMLDocument doc;
	doc.LoadFile("titanic.xml");

	// check for errors while loading the file
	if (doc.ErrorID() != 0)
	{
		cout << "Error loading file: " << doc.ErrorStr() << endl;
		return 1;
	}

	// get the root element
	XMLElement* root = doc.RootElement();

	// loop through all child elements
	for (XMLElement* elem = root->FirstChildElement(); elem != NULL; elem = elem->NextSiblingElement())
	{
		// get the element name and value
		const char* name = elem->Name();
		const char* value = elem->GetText();

		// print the element name and value
		cout << name << ": " << value << endl;
	}

	return 0;
}
