p1 = input ("Welcome to Rock, Paper, Scissors!!! For 1 player, type 1.  For Multiplayer, type 2.")
if p1 == ("1"):
    p1 = input ("Please Choose rock, paper, or scissors:")
    import random
    p2 = random.choice(["rock","paper","scissors"])
    if p1 == "rock":
        if p2 == "rock":
            print("draw")
        elif p2 == "scissors":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    elif p1 == "paper":
        if p2 == "paper":
            print("Draw")
        elif p2 == "rock":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    elif p1 == "scissors":
        if p2 == "scissors":
            print("Draw")
        elif p2 == "paper":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
elif p1 == ("2"):
    p1 = input ("Player 1, Please Choose rock, paper, or scissors:")
    p2 = input ("Player 2, Please Choose rock, paper, or scissors:")
    if p1 == "rock":
        if p2 == "rock":
            print("draw")
        elif p2 == "scissors":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    elif p1 == "paper":
        if p2 == "paper":
            print("Draw")
        elif p2 == "rock":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    elif p1 == "scissors":
        if p2 == "scissors":
            print("Draw")
        elif p2 == "paper":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

else:
    print("only numbers 1 or 2 please")