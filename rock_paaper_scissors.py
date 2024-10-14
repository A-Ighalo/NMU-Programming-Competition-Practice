import random

#rock paper scissors game testing my ability to use inputs,
# compare it with the computers choice to see who won
def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return "You lost"


def is_win(player, opponent):
    #return tru if player wins
    #r > s, s > p , p > r
    if ((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or
            (player == 'p' and opponent == 'r')):
        return True


print(play())
