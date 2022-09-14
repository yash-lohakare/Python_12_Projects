import random

def play():
    user = input("Enter 'r' for rock, 'p' for paper & 's' for sicsors:")
    comp = random.choice(['r','p','s'])
    if(user == comp):
        return "It's a tie! computer choice was : " + comp  
    
    if is_win(user, comp):
        return "You Won!! computer choice was: " + comp 

    return "You LOst computer choice was: " + comp 
def is_win(player, opponent): 
    if (player=='r' and opponent=='s') or (player == 'p' and opponent == 'r') or (player == 's' and opponent=='s'):
        return True

print(play())