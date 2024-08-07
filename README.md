# English-Chess-with-bot-opponent-
Done building Chess pvp using pygame. There are sure to be some bugs here and there as I cannot possibly test every single move in the game but so far everything is playable as a normal chess would be. 

## Overview
This project aims to develop a Chess AI bot that can play against human opponents. The AI will be designed to understand and play chess at various levels of difficulty, providing a challenging and enjoyable experience for players of all skill levels. By leveraging advanced algorithms and machine learning techniques, the goal is to create an AI that can not only make strategic moves but also adapt its gameplay based on the opponent's moves. This project relies heavily on the library `pygame`, where the documentation can be found [here](https://pygame.readthedocs.io/en/latest/1_intro/intro.html). I have successfully coded the pvp game. However, due to unforeseen circumstances I have yet to code the AI bot part as explained in [Limitation](#limitation).

## Motivation
The motivation behind this project is to delve into the fascinating world of artificial intelligence and game theory. Chess, with its complex strategies and deep history, provides an excellent platform to explore AI development. This project will serve as a practical exercise to enhance my skills in algorithm design, machine learning, and AI, while also creating something fun and engaging. Being the first end to end project that I will be working on alone I am excited to embark on this journey.

## Limitation
Initially I wanted to code an AI bot to play against as well, along with option to choose difficulty. However, it deemed to be way too difficulty for me at my current stage. As such, I have decided to put a pause on the project for the time being and come back to code the AI bot after I have honed my proficiency in coding.

I have 3 plans for the AI part which I will touch on in the future:

1. Train an ML model that will give target feature of 'Best Next Move' by taking in every piece on the board along with their positions as the features. (simplest model)
2. Use an open_ai api key to directly ask the LLM for the best possible move in this turn. (Most likely more reliable than option 1 but cannot foresee future to lead to special outplays)
3. Build a model that is able to calculate every possible move and the outcome of those moves, meaning the model will calculate n**m different outcomes from each move to decide the best move. (most advanced)

Limitations to each option (for developer):
- Options 1 and 3 are extremely tedious and time consuming.
- Option 2 requires a paid api key to work.

---

## Steps to run:
1. Ensure you are at the correct file path -> `./English-Chess-with-bot-opponent-`
2. Create virtual environment ```python -m venv chessbot```
3. Activate virtual environment, for Windows: `chessbot\Scripts\activate`, for MacOS/Linux: `source chessbot/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run `main.py` file and game should pop up

---

## Controls:
- Use mouse to drag pieces
- Press 't' to change theme (green, brown, blue, grey)
- Press 'r' to restart game

---

## Game Snapshots

### Snapshot 1 - Start (green)
![snapshot1](snapshots/Screenshot%202024-08-07%20at%203.22.53 PM.png)

### Snapshot 2 - Start (blue)
![snapshot2](snapshots/Screenshot%202024-08-07%20at%203.26.12 PM.png)

### Snapshot 3 - En Passant (brown)
![snapshot3](snapshots/Screenshot%202024-08-07%20at%203.24.46 PM.png)

### Snapshot 4 - Only allowing valid moves when checked (grey)
![snapshot4](snapshots/Screenshot%202024-08-07%20at%203.28.06 PM.png)