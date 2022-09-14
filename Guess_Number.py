import random
def guess(x) :
    random_int = random.randint(1,x)
    guess = 0

    while guess!=random_int:
        guess =int (input(f"Enter a number between 1 and {x}: "))
        if(guess>random_int):
            print("Too high")
        elif(guess<random_int):
            print("Too Low")
    print(f"Yay!! you guessed the correct number and it is {guess}")
guess(15)