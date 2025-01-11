# Interactive Tic-Tac-Toe PDF Game

## Description
This project generates an interactive Tic-Tac-Toe game as a PDF file. The game features a clean interface with clickable buttons and automatic game state management.

## Features
- Interactive 3x3 game board
- Clear "TIC TAC TOE GAME" title
- Player turn alternation (X starts first)
- Automatic win detection for:
  - 3 horizontal rows
  - 3 vertical columns
  - 2 diagonal lines
- Game status display showing:
  - Winner in green text (X WINS! or O WINS!)
  - Draw in red text (EVEN)
- Fixed RESET button for starting new games

## How to Run
1. Make sure you have Python installed
2. Run the script:
   ```bash
   python gamebuilderpdf.py
   ```
3. Open the generated `tictactoe.pdf` in Adobe Acrobat Reader

## Game Rules
1. Game starts with player X
2. Players take turns clicking empty squares
3. First to get 3 in a row wins
4. If all squares are filled with no winner, game is a draw
5. Click RESET anytime to start over

## Technical Details
The game is built using:
- Python for PDF generation
- PDF form fields for the game board
- Embedded JavaScript for game logic
- No external libraries required

## Requirements
- Python 3.x
- Adobe Acrobat Reader
- JavaScript enabled in PDF reader

## Important Notes
- Make sure JavaScript is enabled in your PDF reader
- Buttons cannot be edited once clicked
- Game state is maintained until reset

## Known Limitations
- Requires JavaScript support
- No game history tracking
- No customizable player names

## Author
Created by Abdessamad Sadoudi

## License
This project is open source and available under the MIT License.
