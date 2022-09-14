import random

def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback!='c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high H or too low L or Correct C? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay !! the computer guessed it correctly')

comp_guess(20)