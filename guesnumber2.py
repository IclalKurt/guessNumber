import random
number = random.randrange(1,20)

right = 5

while right > 0 :
    guess = int(input('please guess number :'))
    right -= 1

    if number == guess :
        print(f'congratulations, corretct guess! Your score {(right + 1)*20}')
        break

    elif number > guess :
        print('you need guess a big number, try again.')  

    else :
        print('you need guess a small number, try again.')
        
    if right == 0 :
        print('sorry, your right is over...')    