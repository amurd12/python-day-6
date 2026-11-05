# file is now variable
# r means to read it

line_number = 0

with open("logs.txt", "r") as file:
    for each_line in file:
        line_number = line_number +1
        if "password" in each_line:
            print(each_line)
            print("The line number is ", line_number)


