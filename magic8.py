import random
question = input('Ask a question: ')
num = random.randint(1, 9)
if num == 1:
    print('Yes, definitely')
elif num == 2:
    print('It is decidedly so')
elif num == 3:
    print('Whitout a doubt')
elif num == 4:
    print('Reply, try again')
elif num == 5:
    print('Ask again later')
elif num == 6:
    print('Better not tell you now')
elif num == 7:
    print('My sources say no')
elif num== 8:
    print('Outlook not so good')
else:
    print('Very doubtful')