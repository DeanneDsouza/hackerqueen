#### Hang Man ####
import random
from stages import stages , logo 
import pdb 

wordlist = ["chocolate" , "paper", "house" , "ice cream"]
ans = random.choice(wordlist)
print(ans)
display= []
word = len(ans)
endgame = False
lives = 6 
for i in range(word):
    display += "_"
print (display)
while not endgame : ## meanning endgame not true 
    guess= input("Guess the letter :- ").lower()
    
    for position in range(word):
        letter = ans[position]
        if letter == guess:
            display[position]=letter
        elif letter in display :
            print("the letter you have already guess ")
    
    if guess not in ans :
            lives -= 1
            print("lives" ,lives)
            print(stages[lives])
    if lives == 0:
        print("you loose")
        endgame = True 
            
            
    print (display)
    if "_" not in display :
        endgame= True
        print("game over !")
        






    
       
        
        
    
        



    

    
    
