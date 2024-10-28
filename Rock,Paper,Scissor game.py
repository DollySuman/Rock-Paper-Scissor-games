import random

reply = ["Rock","Paper","Scissor"]
computer = random.choice(reply)
user = input("Enter your choice: ")
if(computer == user):
    print(f"The computer chose {computer}")
    print("Hey it's a draw")
else:
    if(computer == "Rock" and user == "Paper"):
        print(f"The computer chose {computer}")
        print(f"Hey {user} wins")
        
    elif(computer == "Rock" and user == "Scissor"):
        print(f"The computer chose {computer}")
        print(f"Hey {computer} wins")


        
    elif(computer == "Paper" and user == "Rock"):
        print(f"The computer chose {computer}")
        print(f"Hey {computer} wins")

    elif(computer == "Paper" and user == "Scissor"):
        print(f"The computer chose {computer}")
        print(f"Hey {user} wins")

    elif(computer == "Scissor" and user == "Paper"):
        print(f"The computer chose {computer}")
        print(f"Hey {computer} wins")

    elif(computer == "Scissor" and user == "Rock"):
        print(f"The computer chose {computer}")
        print(f"Hey {user} wins")

    else:
        print("Invalid choice")
        