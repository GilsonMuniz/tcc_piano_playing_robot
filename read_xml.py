import xml.etree.ElementTree as ET

def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    music = []
    extract_notes(root, music)

    return music

def extract_notes(element, music):
    for note in element.iter('note'):
        step_element = note.find('.//step')
        octave_element = note.find('.//octave')
        duration_element = note.find('.//duration')

        if step_element is not None and octave_element is not None and duration_element is not None:
            step = step_element.text
            octave = octave_element.text
            duration = duration_element.text

            note_data = {'step': step, 'octave': octave, 'duration': duration}
            music.append(note_data)

# Usage example
xml_file = 'titanic.xml'
music_list = parse_xml(xml_file)
print(music_list)
