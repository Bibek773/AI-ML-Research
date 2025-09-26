
from random import randint as r # for generating random number

def main(temp, user):
    if temp == user:
        print("It's a draw")
    elif (temp == 'r' and user == 's') or (temp == 's' and user == 'p') or (temp == 'p' and user == 'r'):
        print("You lose")
    else:
        print("You win")
while(1):
    play=input("enter p to play")
    if play=='p':
        game = ['r', 'p', 's']
        temp = game[r(0, 2)]
        user = input("Enter r for rock, s for scissors, p for paper: ")
        main(temp, user)
    else:
        break