# 🎮 Rock-Paper-Scissors Game

## 📌 About the Project
This project is a simple **Rock-Paper-Scissors Game** developed using Python. The player competes against the computer, which randomly selects rock, paper, or scissors.

The program determines the winner based on the game rules and keeps track of the scores across multiple rounds.

## ✨ Features
- **User Input:** Choose rock, paper, or scissors.
- **Computer Selection:** The computer randomly selects its choice.
- **Winner Detection:** Determines whether the player wins, loses, or ties.
- **Score Tracking:** Maintains separate scores for the player and computer.
- **Play Again:** Allows the player to play multiple rounds.
- **Input Validation:** Handles invalid choices and asks the player to try again.
- **Final Score:** Displays both scores when the game ends.

## 🛠️ Technologies Used
- **Python 3**
- `random` module

## ⚙️ How to Run the Project

### 1. Clone the Repository
```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory
```bash
cd CODSOFT_3
```

### 3. Run the Program
```bash
python rockPaperScissor.py
```

*Note: Make sure the filename matches the name of your Python file.*

## 🎯 Game Rules
- 🪨 **Rock beats Scissors**
- ✂️ **Scissors beat Paper**
- 📄 **Paper beats Rock**
- 🤝 If both choices are the same, the round is a tie.

## 💻 Example Output
```text
===== ROCK PAPER SCISSORS GAME =====
Choose: rock, paper, or scissors

Enter your choice: rock
Your choice: rock
Computer's choice: scissors
Result: You win!

Your Score: 1
Computer Score: 0

Do you want to play again? (yes/no): no

===== FINAL SCORE =====
Your Score: 1
Computer Score: 0
Thanks for playing!
```

*Note: The computer's choice and game results may vary each time you play.*

## 📚 What I Learned
- Taking user input using `input()`.
- Using conditional statements (`if`, `elif`, and `else`).
- Generating random choices using `random.choice()`.
- Implementing loops using `while`.
- Validating user input.
- Tracking scores using variables.
- Using `break` and `continue` to control program flow.

## 🚀 Future Improvements
- Add a graphical user interface (GUI).
- Add a fixed number of rounds.
- Display the overall winner after multiple rounds.
- Allow the player to enter choices using numbers.

## 👨‍💻 Author
**Aditya**
