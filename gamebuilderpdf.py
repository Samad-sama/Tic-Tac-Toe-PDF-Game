PDF_FILE_TEMPLATE = """
%PDF-1.6

% Root
1 0 obj
<<
  /AcroForm <<
    /Fields [ ###FIELD_LIST### ]
  >>
  /Pages <<
    /Count 1
    /Kids [
      16 0 R
    ]
    /Type /Pages
  >>
  /OpenAction 17 0 R
  /Type /Catalog
>>
endobj

%% Annots Page 1
21 0 obj
[
  ###FIELD_LIST###
]
endobj

###FIELDS###

%% Page 1
16 0 obj
<<
  /Annots 21 0 R
  /Contents << >>
  /CropBox [
    0.0
    0.0
    612.0
    792.0
  ]
  /MediaBox [
    0.0
    0.0
    612.0
    792.0
  ]
  /Parent 7 0 R
  /Resources <<
  >>
  /Rotate 0
  /Type /Page
>>
endobj

17 0 obj
<<
  /JS 42 0 R
  /S /JavaScript
>>
endobj

42 0 obj
<< >>
stream
var currentPlayer = 'X';
var gameBoard = [['','',''],['','',''],['','','']];
var gameOver = false;

function updateButton(btn, symbol) {
    try {
        btn.value = symbol;
        btn.textSize = 30;
        btn.textColor = color.black;
        btn.fillColor = ["RGB", 0.9, 0.9, 0.9];
        btn.readonly = true;
    } catch(e) {
        app.alert("Error updating button: " + e);
    }
}

function makeMove(row, col) {
    try {
        if (gameOver) {
            app.alert("Game is over! Click Reset to play again.");
            return;
        }

        var btn = this.getField(`btn_${row}_${col}`);
        if (btn.value !== "") {
            return;
        }

        // Update the game board and button
        gameBoard[row][col] = currentPlayer;
        updateButton(btn, currentPlayer);

        // Check for win
        if (checkWin(currentPlayer)) {
            this.getField('status').value = currentPlayer + " WINS!";
            this.getField('status').textColor = color.green;
            gameOver = true;
            return;
        }

        // Check for draw
        if (isDraw()) {
            this.getField('status').value = "EVEN";
            this.getField('status').textColor = color.red;
            gameOver = true;
            return;
        }

        // Switch players
        currentPlayer = (currentPlayer === 'X') ? 'O' : 'X';
        this.getField('status').value = "Current Player: " + currentPlayer;

    } catch(e) {
        app.alert("Error in makeMove: " + e);
    }
}

function checkWin(player) {
    // Rows
    for (var i = 0; i < 3; i++) {
        if (gameBoard[i][0] === player && 
            gameBoard[i][1] === player && 
            gameBoard[i][2] === player) return true;
    }
    
    // Columns
    for (var i = 0; i < 3; i++) {
        if (gameBoard[0][i] === player && 
            gameBoard[1][i] === player && 
            gameBoard[2][i] === player) return true;
    }
    
    // Diagonals
    if (gameBoard[0][0] === player && 
        gameBoard[1][1] === player && 
        gameBoard[2][2] === player) return true;
        
    if (gameBoard[0][2] === player && 
        gameBoard[1][1] === player && 
        gameBoard[2][0] === player) return true;
    
    return false;
}

function isDraw() {
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            if (gameBoard[i][j] === '') return false;
        }
    }
    return true;
}

function resetGame() {
    try {
        currentPlayer = 'X';
        gameBoard = [['','',''],['','',''],['','','']];
        gameOver = false;

        // Reset all buttons
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 3; j++) {
                var btn = this.getField(`btn_${i}_${j}`);
                btn.value = '';
                btn.readonly = false;
                btn.fillColor = ["RGB", 0.9, 0.9, 0.9];
            }
        }

        // Reset status
        var status = this.getField('status');
        status.value = "Current Player: X";
        status.textColor = color.black;
    } catch(e) {
        app.alert("Error in resetGame: " + e);
    }
}

// Initialize the game
try {
    resetGame();
} catch(e) {
    app.alert("Error initializing game: " + e);
}

app.execMenuItem("FitPage");
endstream
endobj

trailer
<<
  /Root 1 0 R
>>

%%EOF
"""

TITLE_OBJ = """
###IDX### obj
<<
    /F 4
    /FT /Tx
    /MK <<
        /BG [1 1 1]
    >>
    /Q 1
    /P 16 0 R
    /Rect [
        ###RECT###
    ]
    /Subtype /Widget
    /T (title)
    /V (TIC TAC TOE GAME)
    /Type /Annot
    /Ff 1
>>
endobj
"""

BUTTON_OBJ = """
###IDX### obj
<<
    /A <<
        /JS (###SCRIPT###)
        /S /JavaScript
    >>
    /F 4
    /FT /Tx
    /MK <<
        /BG [0.9 0.9 0.9]
    >>
    /Q 1
    /P 16 0 R
    /Rect [
        ###RECT###
    ]
    /Subtype /Widget
    /T (###NAME###)
    /Type /Annot
    /Ff 0
>>
endobj
"""

STATUS_OBJ = """
###IDX### obj
<<
    /F 4
    /FT /Tx
    /MK <<
        /BG [1 1 1]
    >>
    /Q 1
    /P 16 0 R
    /Rect [
        ###RECT###
    ]
    /Subtype /Widget
    /T (status)
    /Type /Annot
    /Ff 1
>>
endobj
"""

# Configuration
BUTTON_SIZE = 80
GRID_OFF_X = 200
GRID_OFF_Y = 500

fields_text = ""
field_indexes = []
obj_idx_ctr = 50

def add_field(field):
    global fields_text, field_indexes, obj_idx_ctr
    fields_text += field
    field_indexes.append(obj_idx_ctr)
    obj_idx_ctr += 1

def create_tictactoe_pdf():
    # Add title
    title = TITLE_OBJ
    title = title.replace("###IDX###", f"{obj_idx_ctr} 0")
    title = title.replace("###RECT###", f"{GRID_OFF_X} {GRID_OFF_Y + 100} {GRID_OFF_X + BUTTON_SIZE * 3} {GRID_OFF_Y + 150}")
    add_field(title)

    # Create game board buttons
    for row in range(3):
        for col in range(3):
            button = BUTTON_OBJ
            button = button.replace("###IDX###", f"{obj_idx_ctr} 0")
            button = button.replace("###NAME###", f"btn_{row}_{col}")
            button = button.replace("###SCRIPT###", f"makeMove({row}, {col});")
            x = GRID_OFF_X + col * BUTTON_SIZE
            y = GRID_OFF_Y - row * BUTTON_SIZE
            button = button.replace("###RECT###", f"{x} {y} {x + BUTTON_SIZE} {y + BUTTON_SIZE}")
            add_field(button)

    # Add status field
    status = STATUS_OBJ
    status = status.replace("###IDX###", f"{obj_idx_ctr} 0")
    status = status.replace("###RECT###", f"{GRID_OFF_X} {GRID_OFF_Y - 250} {GRID_OFF_X + BUTTON_SIZE * 3} {GRID_OFF_Y - 220}")
    add_field(status)

    # Add reset button
    reset = """
###IDX### obj
<<
    /A <<
        /JS (resetGame())
        /S /JavaScript
    >>
    /F 4
    /FT /Btn
    /MK <<
        /BG [0.8 0.8 0.8]
        /CA (RESET)
    >>
    /P 16 0 R
    /Rect [
        ###RECT###
    ]
    /Subtype /Widget
    /T (reset)
    /Type /Annot
    /Ff 65536
>>
endobj
"""
    reset = reset.replace("###IDX###", f"{obj_idx_ctr} 0")
    reset = reset.replace("###RECT###", f"{GRID_OFF_X + BUTTON_SIZE} {GRID_OFF_Y - 300} {GRID_OFF_X + BUTTON_SIZE * 2} {GRID_OFF_Y - 270}")
    add_field(reset)

    # Generate final PDF
    filled_pdf = PDF_FILE_TEMPLATE.replace("###FIELDS###", fields_text)
    filled_pdf = filled_pdf.replace("###FIELD_LIST###", " ".join([f"{i} 0 R" for i in field_indexes]))

    with open("tictactoe.pdf", "w") as pdffile:
        pdffile.write(filled_pdf)

if __name__ == "__main__":
    create_tictactoe_pdf()
