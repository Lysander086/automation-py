from pathlib import Path

p = Path('C:\\Users\\inz\\Desktop')

for textFilePathObj in p.glob('*.txt'):
    print(textFilePathObj)  # Prints the Path object as a string.
    # Do something with the text file.
