#! python3
import random
guess = ''
tails = 0
heads = 1
while guess not in (heads, tails):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = int(input())
toss = random.randint(0,1)  # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = int(input())
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

