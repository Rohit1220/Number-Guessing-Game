print ("Number Guessing Game")
chances = 5
while chances > 0 :
    import random
    print ('guess a number between 1 - 9')
    any = random.randint(1,9)
    print(any)
    value = int(input("Guess a number between 1 , 9"))
    print(value)
    if any == value :
        print("You Won")
        chances = 0
    else :
        print("sorry, please try again")
        chances = chances-1