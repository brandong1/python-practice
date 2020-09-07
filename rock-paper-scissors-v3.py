print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
print("***NO CHEATING!\n\n" * 20)
player2 = input("Player 2, make your move: ")
 
if player1 == player2:
    print("Draw")
elif player1 == "rock" and player2 == "scissors":
    print("player1 wins")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins")
elif player1 == "scissors" and player2 == "paper":
    print("player1 wins")
else:
    print("player2 wins")