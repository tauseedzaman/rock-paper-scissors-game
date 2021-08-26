# A simple Rock Paper Scissors Game 
# Auther: tauseed zaman

import random

def play():
    print("Game Rules \n\
    [*]=> Paper > Rock \n\
    [*]=> Scissors > Paper \n\
    [*]=> Rock > Scissors \
    ")
    user = input("\n\tWhat your Choice \n\n \t[r]-> rock \n \t[p]-> paper \n \t[s]-> scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        print(f"\nComputer chooses {computer}")
        print(f"You chooses {user}")  
        return "It\'s a Tie"
    if is_win(user, computer):
        return "You Win!"

    print(f"\nComputer chooses {computer}")
    print(f"You chooses {user}")  
    return "You Loost!"


def is_win(player, computer):
    if(player=='' and computer =='s') or (player =='s' and computer =='p') or (player == 'p' and computer =='r'):
        print(f"\nComputer chooses {computer}")
        print(f"You chooses {user}")    
        return True


while True:
    print(play())
    x = input("Do you want to play again [Y]/[N]: ")
    if(x == 'n' or x == "N"):
        exit()