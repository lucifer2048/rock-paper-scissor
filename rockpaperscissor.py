#rock paper scissor
import random

def play():
    user = input("what is your choice? r for rock, p for paper and s for scissors\n")
    computer = random.choice(['r','s','p'])
    if user == computer:
        return 'it\'s a tie'
    if who_won(user,computer):
        return f'you won!! computer\'s choice was {computer}'
    
    return f'you lost!!!! computer\'s choice was {computer}'

def who_won(player,comp):
    # r > s,s > p, p > r
    if(player == 'r' and comp == 's') or (player == 's' and comp == 'p') or (player == 'p' and comp == 'r'):
        return True
if __name__ == "__main__":
    a = 0
    while a != 2:
        print(play())
        a = int(input("press 1 for start\npress 2 for exit\n"))
