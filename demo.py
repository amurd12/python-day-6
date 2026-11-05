# Escape Charecters 
# \n creates a new line
# \t for tab indent

# Absolute vs Relative Paths
# .. is Relative to where you are rather than Absolute start from Home like users and so on 

# Modules and Libraies
# import random
# random_int = random.randint(1,10)
# ex. to pick random from list you can name the function = random.choice(name of list)
# import math
# answer = math.sqrt(64)

# File I/O
# Reading, Writing (this overwrites), Append (this adds)
#changing "w" to "a" to append
#adding \n adds a new line each tme you run it
with open("demo.txt", "a") as file:
    file.write("File I/O is funnnnnn\n")


