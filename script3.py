import random
##program intro
print("rock paper scissors game vs random casino")
#play function takes two inputs: user choice and casino choice


elements = ["1","2","3","q","cheat"] #1-rock, 2-paper, 3-scissors 4-q to quit
playing = True
while playing: 
    #obtain the two datas from user and casino
    casino = random.randint(1,3)#same encoeing
    input_user = input("Choose 1 for rock, 2 for paper, or 3 for scissors: and q to quit ")
    #validity check: skip for now, priortize cheat exception handle
    if input_user not in elements:
        print("Invalid input, please try again.")
        continue
    
    
    #exceptioanl case: show casino choice 
    if input_user == "cheat":
        print("the casino has selected:", casino)
        input_user = input("Now choose 1 for rock, 2 for paper, or 3 for scissors: and q to quit ")
        if input_user == "cheat":
            print("You already fucking have")
            continue
    #game logic. topic: basic rock paper scissors   
    if input_user == "1" and casino == 1:
        print("It's a tie! Both chose rock.")
    elif input_user == "1" and casino == 2:
        print("You lose! Paper covers rock.")
    elif input_user == "1" and casino == 3:
        print("You win! Rock crushes scissors.")
    elif input_user == "2" and casino == 1:
        print("You win! Paper covers rock.")
    elif input_user == "2" and casino == 2:
        print("It's a tie! Both chose paper.") 
    elif input_user == "2" and casino == 3:
        print("You lose! Scissors cuts paper.")
    elif input_user == "3" and casino == 1:
        print("You lose! Rock crushes scissors.")
    elif input_user == "3" and casino == 2:
        print("You win! Scissors cuts paper.")
    elif input_user == "3" and casino == 3:
        print("It's a tie! Both chose scissors.")
    if input_user == "q":
        playing = False
        print("Thanks for playing!")
        break
