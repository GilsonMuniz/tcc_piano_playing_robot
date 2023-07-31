import openpyxl

data = ['Sample',
        'C1', 'C#1', 'Db1', 'D1', 'D#1', 'Eb1', 'E1', 'Fb1', 'F1', 'F#1', 'Gb1', 'G1', 'G#1', 'Ab1', 'A1', 'A#1', 'Bb1', 'B1', 'Cb1',
        'C2', 'C#2', 'Db2', 'D2', 'D#2', 'Eb2', 'E2', 'Fb2', 'F2', 'F#2', 'Gb2', 'G2', 'G#2', 'Ab2', 'A2', 'A#2', 'Bb2', 'B2', 'Cb2',
        'C3', 'C#3', 'Db3', 'D3', 'D#3', 'Eb3', 'E3', 'Fb3', 'F3', 'F#3', 'Gb3', 'G3', 'G#3', 'Ab3', 'A3', 'A#3', 'Bb3', 'B3', 'Cb3',
        'Rest']

# Create a new Excel workbook
wb = openpyxl.Workbook()

# Get the active sheet (first sheet) of the workbook
sheet = wb.active

# Write the header data to the sheet
for col_index, header in enumerate(data, start=1):
    sheet.cell(row=1, column=col_index, value=header)

# Save the workbook to a file
wb.save('header_data.xlsx')
