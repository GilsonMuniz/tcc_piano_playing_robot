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
        octave_element = note.find('.//octave')
        duration_element = note.find('.//duration')
        rest_element = note.find('.//rest')

        if step_element is not None and octave_element is not None and duration_element is not None:
            step = step_element.text
            octave = octave_element.text
            duration = duration_element.text
            note_data = {'step': step, 'octave': octave, 'duration': duration}
            music.append(note_data)
        elif rest_element is not None and duration_element is not None:
            step = 'R' # rest
            octave = '-'
            duration = duration_element.text
            note_data = {'step': step, 'octave': octave, 'duration': duration}
            music.append(note_data)

# Usage example
xml_file = 'titanic.xml'
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
output_file = 'titanic.xlsx'
workbook.save(f'excel_scores/{output_file}')