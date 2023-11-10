def rock_paper_scissors():
    while True:
        player1 = input("Player 1, make your move (rock, paper, scissors): ").lower()
        player2 = input("Player 2, make your move (rock, paper, scissors): ").lower()

        if player1 == player2:
            print("It's a tie!")
        elif (player1 == "rock" and player2 == "scissors") \
                or (player1 == "scissors" and player2 == "paper") \
                or (player1 == "paper" and player2 == "rock"):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

rock_paper_scissors()