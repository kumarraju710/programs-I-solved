import random
while True:

    choices=["rock","paper","scissors"]

    computer=random.choice(choices)
    
    player=None
    while player not in choices:
        player=input("rock,paper,or scissors:").lower() 
    if player==computer:
        print('computer: ',computer)
        print('player: ',player)
        print('Tie!!')
    elif player=='rock':
        if computer=='scissors':
            print('computer: ',computer)
            print('player: ',player)
            print('You Win!')
        if computer=='paper':
            print('computer: ',computer)
            print('player: ',player)
            print('computer wins!')
    elif player=='paper':
        if computer=='rock':
            print('computer: ',computer)
            print('player: ',player)
            print('You Win!')
        if computer=='scissors':
            print('computer: ',computer)
            print('player: ',player)
            print('computer wins!')        
    elif player=='scissors':
        if computer=='paper':
            print('computer: ',computer)
            print('player: ',player)
            print('You Win!')
        if computer=='rock':
            print('computer: ',computer)
            print('player: ',player)
            print('computer wins!')
                   
    play_again=input('Play again (yes/no)?: ').lower()
    if play_again!='yes':
        break                                 
