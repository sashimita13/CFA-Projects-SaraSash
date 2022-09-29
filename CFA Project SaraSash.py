import random """to make code in one module available in another"""

def main():          """the keyword for defining a function"""   
    """Start a periodic table guessing game."""
    print("Guess the periodic table!")
    print ("13,9,28,12,24,7,5")
    print("Guess the periodic table number")   """standard output device"""
    
    periodic_table= [  """variable numbers"""
        "13",
        "9",
        "28",
        "12",
        "24",
        "7",
        "5"
        ]

    x = random.choice(periodic_table)  """list comprehension"""
    guess = None    """no value at all"""

    while x != guess:   """used to iterate over a block of code as long as the test condition is true"""

        guess = str(input("What periodic table number am I thinking of? "))
        
        if x == guess:  """decides whether certain statements need to be executed or not"""
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break   """a loop control statement"""
        else:  """decides what to do if the condition is false"""
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()  """the beginning of any python program"""
