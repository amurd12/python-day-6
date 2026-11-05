'''
Challange 2
Create file called line_counter.py
Copy and paste sogn lyrics into lyrics.txt file
Write a prgrm that outputs the TOTAL number of lines
'''

line_number = 0
empty_line_counter = 0
section_label_counter = 0

with open("lyrics.txt", "r") as file:
    for every_line in file:
        if every_line == "\n":
            empty_line_counter = empty_line_counter + 1

        elif every_line.startswith("["):
            section_label_counter = section_label_counter + 1

        else:
            line_number = line_number + 1

    print("The total lines in the song: ", line_number)
    print("The total empty lines in song:", empty_line_counter)
    print("The total section lables in song:", section_label_counter)
        
        
        



