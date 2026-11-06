import random
# In comments write out what you think functions should be:

# show question
# get_random question
# show_answer
# quit_app

flashcards = [
    {"question" : "What keyword is used to define function", "answer" : "def"},
    {"question" : "What data type represents whole number", "answer" : "int"},
    {"question" : "what data structures are used to represent key value pairs", "answer" : "dictonary"},
]

'''
Task: tell user goodbye
Input: none
Side effect: prints message
Return: none
'''
def quit_app():
    print("====great job studying====")

'''
input: selects and retreves random element in slafhcard list
task: flashcard list
side effect: none
return: flashcard dictonary
'''
def get_random_question(cards):
    random_card = random.choice(cards)
    return random_card

'''
input: display the question
task: question card
side effect: print question 
return: none
'''
def show_question(card):
    question = card["question"]
    print("Question: ", question)

'''
input: display the answer
task: question card
side effect: print answer 
return: none
'''
def show_answer(card):
    answer = card["answer"]
    print("Answer: ", answer)

def main():
    # write code here
    while True:
        card = get_random_question(flashcards)
        show_question(card)
    
        users_choice = input("press a to see answer or q to quit? ") 
    
        if users_choice == "a":
            show_answer(card)
        elif users_choice == "q":
            quit_app()
            break
        else: 
            print("===invalid choice=== \nplease select a or q to continue")





main()



