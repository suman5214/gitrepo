import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
    if value>= min_value and value <= max_value :
        return True 
    else: 
        return False 

def game_board_full(gameBoard):
    """ (str) -> bool
    Precondition: gameBoard is a valid tic-tac-toe game board
    
    return True if and only if the gameBoard has no EMPTY tokens
    
    >>>game_board_full('XOXOOX-X-')
    False
    >>>game_board_full('XOXOOXOXO')
    True    
    """

    if EMPTY in gameBoard:
        return False 
    else:
        return True 



def get_board_size(gameBoard):
    """(str) -> int
    Precondition: gameBoard is a valid tic-tac-toe game board
        
    return the side length in integer of a valid game board
       
    >>>get_board_size('XOXOOX-X-')
    3
    >>>get_board_size('----')
    2 
    """
    return int(math.sqrt(len(gameBoard)))



def make_empty_board(size):
    """(int) -> str
    Precondition: size is interger between 1 - 9
    
    return a game board with the desire size and EMPTY token filled in all the possible spaces
        
    >>>make_empty_board(2)
    "--"
    >>>make_empty_board(4)
    "----------------"
    """
    board=''
    for i in range(size**2):
        board += EMPTY
    return board



def get_position(row_index, col_index, board_size):
    """(int, int, int) -> int
    Precondition: row_index and col_index must be >=1 and <= board_size
                  board_size must be a interger between 1-9
    
    return the str_index of the tokens in a string representation of the game board 
    
    >>>get_position(1,1,5)
    0
    >>>get_position(2,1,4)
    4
         
    """
    str_index = (row_index - 1) * board_size + col_index - 1
    return str_index

def make_move(symbol, row_index, col_index, gameBoard):
    """ (str, int, int, str) -> str
    Precondition: row_index and col_index must be >=1 and <= board_size
                  gameBoard is a valid tic-tac-toe game board
    
    return a gameBoard with the indicated symbol changed at position given by row_index and col_index             
        
    >>>print(make_move('X',2,2,"O---"))
    "O--X"
    >>>print(make_move('X',1,1,"O---"))
    "X---"
    """ 
    index = get_position(row_index, col_index, get_board_size(gameBoard))
    gameBoard = gameBoard[:index]+symbol+gameBoard[index+1:]
    return gameBoard
def extract_line(gameBoard, checkLine, lineNum):
    """(str, str, int) -> str
    Precondition: checkLine must be one the four indicators : 'down', 'across', 'down_diagonal' or 'up_diagonal'
                  gameBoard is a valid tic-tac-toe game board
                  lineNum is within range of the game board
    
    return the characters that makes up the specific line indicated by 'down' : the columm , 'across' : the row, 
    'down_diagonal' : upper-left corner to lower-right corner, 'up_diagonal' : lower-left corner to upper-right corner
    
    >>>extract_line('XXXOOO!!!',2,'down')
    'XO!'
    >>>extract_line('XXXOOO!!!',2,'across')
    'OOO'
    >>>extract_line('XXXOOO!!!',2,'down_diagonal')
    'XO!'
    >>>extract_line('XXXOOO!!!',2,'up_diagonal')
    '!OX'
    """
    result=''
    if checkLine=='down':
        row_index = 1
        for i in range(get_board_size(gameBoard)):
            result += gameBoard[get_position (row_index, lineNum, get_board_size(gameBoard))]
            row_index += 1
    elif checkLine=='across':
        col_index = 1
        for i in range(get_board_size(gameBoard)):
            result += gameBoard[get_position (lineNum,col_index , get_board_size(gameBoard))]
            col_index += 1 
    elif checkLine =='down_diagonal':
        col_index = 1
        row_index = 1
        for i in range(get_board_size(gameBoard)):
            result += gameBoard[get_position (row_index,col_index , get_board_size(gameBoard))]
            row_index += 1
            col_index += 1
    elif checkLine =='up_diagonal':
        col_index = 1
        row_index = get_board_size(gameBoard)
        for i in range(get_board_size(gameBoard)):
            result += gameBoard[get_position (row_index,col_index , get_board_size(gameBoard))]
            row_index -= 1
            col_index += 1
    return result

            
    