#coding = utf-8

'''
#定义一个随机数函数，能够产生1到20的随机数
import random
def ranNum():
    num = random.randint(1,20)
    print(num)
#ranNum()

print('I am thinking a number between 1 and 20. ')
#myNum = input('Take a guess.')
cNum = ranNum()
for guessTimes in range(1,7):
    myNum = input('Take a guess.')
    if myNum < cNum:
        print('Your guess is too low.')
    elif myNum > cNum:
        print('Your guess is too high.')
    else:
        break
if myNum == cNum:
    print('Good job! You guessed my number in '+ guessTimes + 'guesses! It\'s '+ myNum )
else:
    print('Nope. The number I was thinking of was '+ cNum)
'''
#This is a guess the number game.
import random
secretNumber = random.randint(1,20)
print('I am thinking a number between 1 and 20. ')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
#    guess = int(input('Take a guess.'))  #不建议使用这种方法。会导致界面不好看。
    print('Take a guess. ')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        #
        print('You have no chances.')
        break
if guess == secretNumber:
    print('Good job! You guessed my number in '+ str(guessesTaken) + 'guesses! It\'s '+ str(guess) )
else:
    print('Nope. The number I was thinking of was '+ str(secretNumber))
