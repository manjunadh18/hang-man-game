import random 
import hangman_stages 
words=['apple','beautiful','potato']
lives=6
first=random.choice(words)
print(first)
display=[]
for i in first:
    display += '_'
print(display)
flag=False
while not flag:
    guess=input("Guess a letter: ").lower()
    for position in range(len(first)):
        letter=first[position]
        if letter==guess:
            display[position] = guess
    print(display)
    if guess not in first:
        lives-=1
        if lives==0:
            flag=True 
            print("You lose!!")
    if '_' not in display:
        flag= True 
        print("You win! ")
    print(hangman_stages.stages[lives])
        