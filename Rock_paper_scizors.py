import random

def get_choices():
    player_choice = input("Input a choice:")
    computer_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_options)
    choices = {"player":player_choice, "computer":computer_choice}
    return choices
    
def check_win(player, computer):
    print(f"Player chose {player}, computer chose {computer}") #print("Player chose:"+player + 'computer chose:'+computer)
    if player == computer:
        return("draw")
    elif player == "rock":
        if computer == "paper":
            return("Paper covers rock. Computer wins")
        else:
            return("Rock smashes scissors. Player wins")
    elif player == "paper":
        if computer=="rock":
            return("Paper covers rock. Player wins")
        else:
            return("Scissors cut paper. Computer wins")
    elif player == "scissors":
        if computer == "rock":
            return("Rock smashes scissors. Computer wins")
        else:
            return("Scissors cut paper. Player wins")
    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
    