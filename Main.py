#Imports
import random

#Global Variables
possible_type = [" - ", " X ", " + ", " = "]
score = 0
number = 0
#Functions
def int_checker(question):
    while True:
        try:
            user_input = int(input(question))
            return user_input
        except:
            print("Please enter a valid number!")

def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users dont enter yes / no
        if response == "yes" or response == "Yes":
            return "yes"
        elif response == "no" or response == "No":
            return "no"
        else:
            print("Please enter yes or no")


#Asks user if they want instructions
def how_to_play():

    print('''
    
**** How to play ****
To play the quiz, all you have to do is just answer 10 questions.
The questions you are going to be quized on are PLUS, MINUS and MULTIPLY. 
At the end of the questions the computer will show you how many you got right!
It will also say when you get questions right or wrong. 
If you do get a question wrong the computer will tell you what the real answer is.
The questions you have got right will get a score out of 10 and the amount of numbers you have will turn into a score.
For example, if you have got 4 questions right your score will be 4 out of 10.
You will be congradulated on how many questions you have got right.
Then the quiz will ask you if you would like to play again.
If you would not like to play again the quiz will end.

    ''')
# to make the user only enter a number

# Where the code makes the questions.
def subtract(a,b):
        global score
        subQ =  int_checker(str(a) + possible_type[0] + str(b) + possible_type[3])
        results = int(a) - int(b)
        if subQ != results:
            print("Incorrect! The answer is", results)
        else:
            score += 1
            print("Correct")
def multiply(a,b):
        global score
        multQ =  int_checker(str(a) + possible_type[1] + str(b) + possible_type[3])
        results = int(a) * int(b)
        if multQ != results:
            print("Incorrect! The answer is", results)

        else:
            score += 1
            print("Correct")
def add(a,b):
        global score
        addQ =  int_checker(str(a) + possible_type[2] + str(b) + possible_type[3])
        results = int(a) + int(b)
        if addQ != results:
            print("Incorrect! The answer is", results)

        else:
            score += 1
            print("Correct")

# Main routine
def main():
    global score
    print("Welcome to the Math Quiz!\n")
    #Asks for name
    while True:
        name = input("What's your name?\n").capitalize()
        if name == "":
            print('Please enter a name!')
        else:
            break
    print(f"Hey there {name}!")
    if yes_no("Do you want to see some instructions?\n") == "yes":
        how_to_play()
    print("You can now begin the math quiz!")
    print(f"Good luck {name} :)\n")


    questions = 0
    a = random.randint(1,12)
    b = random.randint(1,12)

    for questions in range(10):
        Qlist = (add, subtract, multiply)
        random.choice(Qlist)(random.randint(1,12), random.randint(1,12))
        questions += 1

    if questions == 10:
        print(f"You have finished {name}. \nYou are now at the end of the math quiz!")
        print(f"Your total score is {score} out of 10!")
    if score > 1 and score < 5:
        print("Try again!\nBetter luck next time.\n")
    elif score > 6 and score < 9:
        print("Well done.\nYour almost perfect!\n")
    elif score == 10:
        print("You got 10/10.\nWell Done you are the best!\n")
    elif score == 0:
        print("You really need to do better!\n")
flag = True
while flag:
    main()
    if yes_no("Would you like to play again?\n") == "yes":
        flag = True
        score = 0
    else:
        flag = False
        print("Thanks for playing, Bye!")

