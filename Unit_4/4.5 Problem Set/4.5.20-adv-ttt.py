#For this check-in, your goal is to write an agent that can
#play tic-tac-toe.
#
#How do you code an agent that plays tic-tac-toe? Well, you
#code an agent that plays a single move in a tic-tac-toe game.
#Then, we run a game, passing the board back and forth between
#your agent and an opponent.
#
#So, all you need to do is write a function called move. move
#should have one parameter, a list of lists. The parameter
#will always be a 3x3 list of characters. Every item in the
#3x3 list will be either a space (empty), U (Us), or T (Them).
#We're using U and T instead of X and O so that your agent
#doesn't have to worry about whether it's playing as X or O:
#you always play as U.
#
#Your move function should  always return a tuple with two
#integer representing the coordinate where you want to play, row
#then column. For example, returning (0, 0) would play in the
#top left. Returning (0, 2) would play in the top right (row 0,
#column 2). Returning (2, 0) would play in the bottom left (row
#2, column 0). Returning (2, 2) would play in the bottom right
#(row 2, column 2).
#
#Remember, you're only coding an agent to play a single move
#in a tic-tac-toe game; it's given a board and it returns a
#single move. The board it receives might be empty, it might
#be partially-played, or it might have only a single possible
#move remaining. You may assume that the game board is valid
#(e.g. no one has yet won the game).
#
#In order to pass this check-in, all you have to do is write
#an agent that can play a move in any valid board: it never
#tries to play in a spot that has already been played or to
#play a move out of range. Beyond that, it does not matter if
#your agent wins or loses, or how it selects the move to play.


#Add your move() function here!
def move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return (i, j)
    return (-1, -1)



#Below is some code that will run your agent. Specifically,
#this code has your agent play against itself, as both X and
#O. X will move first. The version of the game board fed into
#your move() function will still use U and T, but it will be
#shown in the output as X and O so that it makes sense to read.
#
#You don't really need to know how this code works, so don't
#be intimidated by it; but also, there's nothing here that you
#don't know about, so feel free to try to reason through it!
#
#However, DO NOT MODIFY THE CODE BELOW. I mean, unless you
#really want to. If you modify it, you won't be able to test
#your agent against itself, but you could modify it to try other
#stuff if you want to. If you accidentally change the code below,
#copy your move() function, reset the problem, and paste your
#move() function back in.



#Checks if anyone has won the game yet. Returns a tuple whose
#first value is a boolean representing whether the game is
#over and whose second value is a string representing the result.
def game_result(board):
    #Check horizontal winner
    #Check row 0
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        if not board[0][0] == " ":
            return True, board[0][0]
    #Check row 1
    if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        if not board[1][0] == " ":
            return True, board[1][0]
    #Check row 2
    if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        if not board[2][0] == " ":
            return True, board[2][0]
    #Check column 0
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        if not board[0][0] == " ":
            return True, board[0][0]
    #Check column 1
    if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        if not board[0][1] == " ":
            return True, board[0][1]
    #Check column 2
    if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        if not board[0][2] == " ":
            return True, board[0][2]
    #Check top-left to bottom-right diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if not board[0][0] == " ":
            return True, board[0][0]
    #Check bottom-left to top-right diagonal
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if not board[0][2] == " ":
            return True, board[0][2]
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False, "Continue"
    return True, "Draw"

#Changes a game from Xs and Os to Us and Ts depending on whose
#move it is.
def pivot_board(board, player):
    pivoted_board = [["?","?","?"],["?","?","?"],["?","?","?"]]
    if player == "X":
        replacement_dictionary = {" ": " ", "X": "U", "O": "T"}
    else:
        replacement_dictionary = {" ": " ", "X": "T", "O": "U"}
    for i in range(3):
        for j in range(3):
            pivoted_board[i][j] = replacement_dictionary[board[i][j]]
    return pivoted_board

#Print the game board to the console.
def print_board(board):
    print("{0}|{1}|{2}\n-----\n{3}|{4}|{5}\n-----\n{6}|{7}|{8}\n".format(board[0][0], board[0][1], board[0][2],
                                                                     board[1][0], board[1][1], board[1][2],
                                                                     board[2][0], board[2][1], board[2][2]))


#Main game-running engine.
def test_game():
    game_board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    current_player = "X"
    game_done = False

    while not game_done:
        print(current_player + "'s turn...")

        #Gets next move based on the current board, pivoting it
        #to show the player's own moves as U and the opponent's
        #as T.
        result = move(pivot_board(game_board, current_player))

        #Checks if result is a tuple with two items, and prints
        #INVALID MOVE if not. Quits the game if the move is not
        #valid.
        try:
            row, column = result
        except:
            print("INVALID MOVE:", result)
            break

        #Checks if the move is legal, e.g. consists of two integers
        #in range and is not a move on top of an existing move.
        #Prints INVALID MOVE if not. Quits the game if the move
        #is not valid.
        try:
            if not game_board[row][column] == " ":
                print("INVALID MOVE:", row, column)
                break

            #Updates the game board if the move appeared valid.
            game_board[row][column] = current_player
        except:
            print("INVALID MOVE:", row, column)
            break

        #Changes the current player.
        current_player = "O" if current_player == "X" else "X"

        #Prints the current board.
        print_board(game_board)

        #Checks if the game has a winner or is a draw.
        game_done, winner = game_result(game_board)

    #Prints the final result if the game finished completely
    #(no invalid moves).
    if game_done:
        if winner == "Draw":
            print("It's a draw!")
        else:
            print(winner, "wins!")

if __name__ == '__main__':
    test_game()