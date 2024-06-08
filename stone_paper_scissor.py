import random
print("Let's play the Stone,Paper and Scissor!")

while 1:  
    items = ["stone","paper","scissor"]
    my_choice = input("Enter 'stone','paper' and 'scissor': ").lower()
   
    while my_choice not in items:
            my_choice = input("Invalid guess.Please Enter 'stone','paper' and 'scissor': ").lower()
            break
    
    computer_choice = random.choice(items)
    print(f"your choice is '{my_choice}' and computer choice is '{computer_choice}'")
    
    if my_choice == computer_choice:
        print("it's draw")

    elif (my_choice == 'stone' and computer_choice == 'scissor')or \
        (my_choice == 'paper' and computer_choice == 'rock') or \
        (my_choice == 'scissor' and computer_choice == 'paper'):
        print("You win!")
        
    else:
        print("Computer Win!")

    next_game = input("Let's play the game again! [y/n]: ")
    if next_game == 'n':
         break 


