# abstraction is when i hide the complex details for something a lot more simple 

# personal info
#  a function allows us to wrap data or inofrormation into a special box or enclosure for reuse
# define a function
def personalInformation(): 
    question1 = input("how old are you?: ")
    question2 = input("where do you live?: ")
    question3 = input("what school do you go to?: ")
    print(question1 + question2 + question3)
# call the function
# personalInformation()
# personalInformation()
# personalInformation()

# make a function that guesses how old you are
def guessAge():
    q1 = int(input("What year is it now?: "))
    q2 = int(input("what year where you ?: "))
    answer = q1 - q2
    result = print(f'you are {answer} years old')

guessAge()
guessAge()
guessAge()
