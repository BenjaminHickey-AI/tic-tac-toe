# tic-tac-toe


---

## Part 1: Initial Project Ideas

Decision rules for next move or narrative path.

Prioritization or score system for rule evaluation.

Rule conflict resolution strategy.

### 1. Project Idea 1: Movie Recommendation System
- **Description:** Recommends movies or books based on user preferences using rules instead of learned data.
- **Rule-Based Approach:**  
  - User inputs genres, mood, and past preferences.
  - Rule base like: If the user likes action AND hates romance THEN the system recommends Die Hard.

### 2. Project Idea 2: Home Automation System
- **Description:** Simulate a smart home assistant that controls devices based on user-defined rules.
- **Rule-Based Approach:**  
  - Rules like IF motion_detected AND time > 9 PM THEN turn_on_light.  
  - Virtual sensors and state simulation help with data control.

### 3. Project Idea 3: Rule-Based Game AI (tic tac toe)
- **Description:** Use rules to drive AI behavior in a simple game environment.
- **Rule-Based Approach:**  
  - Decision rules for next move based on board position.
  - For example, looking for any moves that immediately win before considering other tactical options.

### **Chosen Idea:** Rule-Based Game AI (tic tac toe)
**Justification:** I chose this project because it is seems like an interesting challenge. I also get to learn a very gamified rules-based approach.

---

## Part 2: Rules/Logic for the Chosen System

The **Rule-Based Game AI (tic tac toe)** system will follow these rules:

1. **Winning Move:**  
   - **IF** the AI has two in a row and the third is empty **THEN** place the mark to win.

2. **Block Opponent**  
   - **IF** the opponent has two in a row and the third is empty **THEN** block them.  

3. **Take Center**  
   - **IF** the center is empty **THEN** take it.

4. **Take Opposite Corner**  
   - **IF** the opponent is in a corner **THEN** take the opposite corner.

5. **Take Empty Corner**  
   - **IF** a corner is free **THEN** take it.

6. **Take Empty Side**  
   - **IF** no better move **THEN** take a side square.
---

## Part 3: Rules/Logic for the Chosen System

Sample input and output of a full match: 

Welcome to Tic-Tac-Toe! You are O, AI is X.
Who goes first? (human/ai): ai

  0   1   2
0   |   |
 \---------\
1   |   |
 \---------\
2   |   |

AI's move: (1, 1)

  0   1   2
0   |   |
 \---------\
1   | X |
 \---------\
2   |   |

Enter your move (row col): 1 1
That cell is taken. Try again.
Enter your move (row col): 0 0

  0   1   2
0 O |   |
 \---------\
1   | X |
 \---------\
2   |   |

AI's move: (2, 2)

  0   1   2
0 O |   |
 \---------\
1   | X |
 \---------\
2   |   | X

Enter your move (row col): 0 1

  0   1   2
0 O | O |
 \---------\
1   | X |
 \---------\
2   |   | X

AI's move: (0, 2)

  0   1   2
0 O | O | X
 \---------\
1   | X |
 \---------\
2   |   | X

Enter your move (row col): 1 2

  0   1   2
0 O | O | X
 \---------\
1   | X | O
 \---------\
2   |   | X

AI's move: (2, 0)

  0   1   2
0 O | O | X
 \---------\
1   | X | O
 \---------\
2 X |   | X

AI wins!

## Part 4: Reflection

### Project Overview:
This project is a rule-based AI system that plays Tic-Tac-Toe against the player. It uses a prioritized set of logical rules to decide moves, such as winning, blocking, or choosing strategic positions. The game includes user interaction, move display, error handling, and an option to choose who plays first.

### Rule-based System:
The rules are ordered by importance. The AI first checks if it can win by completing three in a row. If not, it checks if the opponent is about to win and blocks that move. These two are the most critical and directly impact the outcome. Next, it looks for strategic positions—such as taking the center, responding with opposite corners, or occupying empty corners and sides. These positional rules aim to control the board and increase the chance of a future win.

### Challenges:
- **Handling errors in user input:**  
  Parsing and handling bad user input was a challenge.
- **AI decisions:**  
  Ensuring that the AI doesn't overwrite or try to give invalid moves was an important step in making this work.
- **Ensuring all cases are covered:**  
  Making sure the AI had a valid move for every situation was a challenge that required planning beforehand, thankfully doing part 2 beforehand took care of this.
