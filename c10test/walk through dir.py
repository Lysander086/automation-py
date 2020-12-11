import os

# Unlike range(), the os.walk() function will return three values on each iteration through the loop:
for folderName, subfolders, filenames in os.walk('..\\'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')