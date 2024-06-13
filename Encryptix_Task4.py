import random
print("Please Turn your Caps Lock On!!!")

user_choice = input(" R = Rock \n P = Paper \n S = Scissor \nEnter your choice: ")
print("User Chooses: "+ user_choice)
computer_choice = random.choice(['R', 'P', 'S'])
print("Computer chooses: " + computer_choice)

if (user_choice == computer_choice) :
    print("It's a Tie!!")
elif (user_choice == 'R') and (computer_choice == 'S') or (user_choice=='S') and (computer_choice=='P') or (user_choice=='P') and (computer_choice=='R'):
    print("User Wins. Hooray!!")

else:
    print("Computer Wins!")