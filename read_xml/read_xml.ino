#include <TinyXML.h>

TinyXML xml;

void setup() {
  Serial.begin(9600);
  xml.LoadFile("titanic.xml");
  
  TiXmlElement* person = xml.FirstChildElement("person");
  const char* id = person->Attribute("id");
  Serial.println(id);
}

void loop() {
  // do nothing
}
