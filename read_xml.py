import xml.etree.ElementTree as ET
from openpyxl import Workbook

def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    music = []
    extract_notes(root, music)
    return music

def extract_notes(element, music):
    for note in element.iter('note'):
        step_element = note.find('.//step')
        alter_element = note.find('.//alter')
        octave_element = note.find('.//octave')
        duration_element = note.find('.//duration')
        rest_element = note.find('.//rest')

        if step_element is not None and octave_element is not None and duration_element is not None:
            step = step_element.text
            octave = int(octave_element.text)
            duration = int(duration_element.text)
            alter = int(alter_element.text)
            if alter == 1: step += '#'
            if alter == -1: step += 'b'
            note_data = {'step': step, 'octave': octave, 'duration': duration}
            music.append(note_data)
        elif rest_element is not None and duration_element is not None:
            step = 'R' # rest
            octave = '-'
            duration = int(duration_element.text)
            note_data = {'step': step, 'octave': octave, 'duration': duration}
            music.append(note_data)

# Usage example
print('Music Name:', end='')
file_name = input()

xml_file = f'{file_name}.xml'
music_list = parse_xml(xml_file)

# Create an Excel workbook and select the active sheet
workbook = Workbook()
sheet = workbook.active

# Write the header row
header_row = ['Step', 'Octave', 'Duration']
sheet.append(header_row)

# Write the music data rows
for note in music_list:
    row = [note['step'], note['octave'], note['duration']]
    sheet.append(row)

# Save the workbook
output_file = f'{file_name}.xlsx'
workbook.save(f'excel_scores/{output_file}')