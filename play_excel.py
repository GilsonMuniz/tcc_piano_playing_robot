import RPi.GPIO as PIN
from time import sleep
from variables import *

PIN.cleanup()
PIN.setmode(PIN.BOARD)

for pin in NOTES_PINS.values(): PIN.setup(pin, PIN.OUT)

for row in range(2, music_size + 1):
    print(f'{row}:', end=' ')
    for cell in worksheet[row][2:]:
        if notes_columns[cell.column_letter] in NOTES_PINS:
            pin = NOTES_PINS[notes_columns[cell.column_letter]]
            PIN.output(pin, PRESSED if cell.value else NOT_PRESSED)
            if cell.value: print(notes_columns[cell.column_letter], end=' ')
    sleep(SAMPLE_TIME)
    print()

workbook.close()
PIN.cleanup()