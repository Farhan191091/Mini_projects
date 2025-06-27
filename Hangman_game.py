import random
words = [
    "cat", "dog", "sun", "book", "tree",
    "car", "bird", "house", "milk", "ball",
    "shoe", "hat", "star", "fish", "apple",
    "cup", "pen", "chair", "water", "school"]
guess = ""
comp_choose = random.choice(words)
for i in range(len(comp_choose)):
    guess = guess + "_"
print(comp_choose)    
print(guess) 
list="" 
attempt=8
game_is_over = True
while game_is_over:

    user=input("Guess a letter : ")
    display = ""
    for i in comp_choose:
        if(user == i):
            display += i
            list += i
            
        elif i in list:
            display += i
        else :
            display += "_" 
    attempt -= 1               
    print(display)
    print(f"Remaing life : {attempt}") 

    if "_" not in display:
        print("Yes! You won!")
        game_is_over = False
        break

    elif(attempt == 0):
        print("Game is over ! you lost !")
           

