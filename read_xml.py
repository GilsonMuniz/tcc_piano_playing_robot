import xml.etree.ElementTree as ET
from openpyxl import Workbook

def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    music_commands = []
    extract_notes(root, music_commands)
    return music_commands

def extract_notes(root, music_commands):
    for element in root.iter():
        if element.tag == 'note':
            note = element
            step_element = note.find('.//pitch//step')
            alter_element = note.find('.//pitch//alter')
            octave_element = note.find('.//pitch//octave')
            duration_element = note.find('.//duration')
            rest_element = note.find('.//rest')
            chord_element = note.find('.//chord')

            # Rest
            if rest_element is not None:
                command = 'REST'
                duration = int(duration_element.text)
                note_data = {'command': command, 'duration': duration}
            else:  # Note
                command = 'NOTE'
                step = step_element.text
                octave = octave_element.text
                duration = int(duration_element.text)
                alter = int(alter_element.text) if alter_element is not None else 0
                if alter == 1:
                    step += '#'
                elif alter == -1:
                    step += 'b'
                chord = True if chord_element is not None else False
                note_data = {'command': command, 'step': step + octave, 'chord': chord, 'duration': duration}

            music_commands.append(note_data)

        elif element.tag == 'backup':
            backup = element
            command = 'BACKUP'
            duration_element = backup.find('.//duration')
            duration = int(duration_element.text)
            backup_data = {'command': command, 'duration': duration}
            music_commands.append(backup_data)

print('Music Name: ', end='')
file_name = input()

xml_file = f'musicxmls/{file_name}.musicxml'
music_commands = parse_xml(xml_file)

# Create an Excel workbook and select the active sheet
workbook = Workbook()
sheet = workbook.active
sheet_list = []

# Write the header row
header_row = ['Sample',
        'C1', 'C#1', 'Db1', 'D1', 'D#1', 'Eb1', 'E1', 'Fb1', 'E#1', 'F1', 'F#1', 'Gb1', 'G1', 'G#1', 'Ab1', 'A1', 'A#1', 'Bb1', 'B1', 'Cb1', 'B#1',
        'C2', 'C#2', 'Db2', 'D2', 'D#2', 'Eb2', 'E2', 'Fb2', 'E#2', 'F2', 'F#2', 'Gb2', 'G2', 'G#2', 'Ab2', 'A2', 'A#2', 'Bb2', 'B2', 'Cb2', 'B#2',
        'C3', 'C#3', 'Db3', 'D3', 'D#3', 'Eb3', 'E3', 'Fb3', 'E#3', 'F3', 'F#3', 'Gb3', 'G3', 'G#3', 'Ab3', 'A3', 'A#3', 'Bb3', 'B3', 'Cb3', 'B#3',
        'C4', 'C#4', 'Db4', 'D4', 'D#4', 'Eb4', 'E4', 'Fb4', 'E#4', 'F4', 'F#4', 'Gb4', 'G4', 'G#4', 'Ab4', 'A4', 'A#4', 'Bb4', 'B4', 'Cb4', 'B#4',
        'C5', 'C#5', 'Db5', 'D5', 'D#5', 'Eb5', 'E5', 'Fb5', 'E#5', 'F5', 'F#5', 'Gb5', 'G5', 'G#5', 'Ab5', 'A5', 'A#5', 'Bb5', 'B5', 'Cb5', 'B#5',
        'C6', 'C#6', 'Db6', 'D6', 'D#6', 'Eb6', 'E6', 'Fb6', 'E#6', 'F6', 'F#6', 'Gb6', 'G6', 'G#6', 'Ab6', 'A6', 'A#6', 'Bb6', 'B6', 'Cb6', 'B#6',
        'Rest']
sheet_list.append(header_row)

def fill_cells(sample, symbol, duration):
    global table_samples
    global sheet_list
    for sample_i in range(sample, sample + duration):
        if sample_i not in table_samples:
            default_row = [sample_i,
                '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                '']
            table_samples.append(sample_i)
            sheet_list.append(default_row) # sample still doesn't exists
        sheet_list[sample_i][header_row.index(symbol)] = True

table_samples = []
sample = 1
for command in music_commands:
    if command['command'] == 'NOTE':
        if command['chord']: sample -= command['duration']
        fill_cells(sample, command['step'], command['duration'])
        sample += command['duration']
    elif command['command'] == 'REST':
        fill_cells(sample, 'Rest', command['duration'])
        sample += command['duration']
    elif command['command'] == 'BACKUP': sample -= command['duration']

for row in sheet_list: sheet.append(row)

# Save the workbook
output_file = f'{file_name}.xlsx'
workbook.save(f'excel_scores/{output_file}')