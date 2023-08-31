import RPi.GPIO as PIN
from time import sleep
from variables import *

PIN.cleanup()
PIN.setmode(PIN.BOARD)

# right hand
PIN.setup(18, PIN.OUT)
PIN.setup(22, PIN.OUT)
PIN.setup(24, PIN.OUT)
PIN.setup(26, PIN.OUT)
PIN.setup(32, PIN.OUT)
PIN.setup(36, PIN.OUT)
PIN.setup(38, PIN.OUT)
PIN.setup(40, PIN.OUT)
# left hand
PIN.setup(12, PIN.OUT) 
PIN.setup(16, PIN.OUT)
PIN.setup( 3, PIN.OUT)
PIN.setup( 5, PIN.OUT)
PIN.setup( 7, PIN.OUT)
PIN.setup(11, PIN.OUT)
PIN.setup(13, PIN.OUT)
PIN.setup(15, PIN.OUT)

for row in range(2, music_size + 1):
    print(f'{row}:', end=' ')
    for cell in worksheet[row][2:]:
        if notes_columns[cell.column_letter] in NOTES_PINS:
            PIN.output(NOTES_PINS[notes_columns[cell.column_letter]], PRESSED if cell.value else NOT_PRESSED)
            if cell.value: print(notes_columns[cell.column_letter], end=' ')
    sleep(SAMPLE_TIME)
    print()

workbook.close()
PIN.cleanup()