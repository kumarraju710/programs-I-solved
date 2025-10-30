
import random
while True:
   
    guess=random.randint(1,10)

    my_guess=None
    while my_guess==None:
        my_guess=int(input('enter your guessing number:'))
        print('computer guess: ',guess,'My guess: ',my_guess)
      
       
        if my_guess==guess:
            print('You Win!!')

        elif my_guess>guess:
            print("think small") 
        elif my_guess<guess:
            
            print("think big")    
    
    play_again=input('Do You want to play again(y/n):').lower()
    if play_again=='y':
        pass
    elif play_again=='n' or 'no' or 'naah' :
        print("Bye Bye")

        break
      
        
