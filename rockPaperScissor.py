import random

# Initialize scores
user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS GAME =====")
print("Choose: rock, paper, or scissors")

while True:
    # User input
    user = input("\nEnter your choice: ").lower()

    if user not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        continue

    # Computer selection
    computer = random.choice(["rock", "paper", "scissors"])

    # Display choices
    print("Your choice:", user)
    print("Computer's choice:", computer)

    # Game logic
    if user == computer:
        print("Result: It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        print("Result: You win!")
        user_score += 1
    else:
        print("Result: Computer wins!")
        computer_score += 1

    # Display scores
    print("\nYour Score:", user_score)
    print("Computer Score:", computer_score)

    # Play again
    play_again = input(
        "\nDo you want to play again? (yes/no): "
    ).lower()

    if play_again != "yes":
        break

print("\n===== FINAL SCORE =====")
print("Your Score:", user_score)
print("Computer Score:", computer_score)
print("Thanks for playing!")