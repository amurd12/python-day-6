'''
Challange 1
write program that asks user for name 
than ADDS it to a guest_list.txt file
'''


name =  input("What is your name? ")

with open("guest_list.txt", "a") as file:
    file.write(name + "\n")









