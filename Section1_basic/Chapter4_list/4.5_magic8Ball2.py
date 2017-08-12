#coding = utf-8
##上一个magic 8 ball 在：Chapter3--3.2
import random
messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

#print(len(messages))
print( messages[random.randint(0, len(messages)-1)])