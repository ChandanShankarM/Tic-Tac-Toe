import random
# Initializing the number of places in a board
board_values=[i for i in range(0,9)]
# Initializing both players to null character
You, computer = '',''

# Making tuples pairs as corners,center and other places
moves=((1,7,3,9),(5,),(2,4,6,8))
# Initalizing all the winning Combinations
win_comb=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

table=range(1,10)

def print_board():
    x=1
    for i in board_values:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            if i != 1: end+='----------\n';
        char=' '
        if i in ('X','O'): 
            char=i
        x+=1
        print(char,end=end)
        
def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars

def can_move(brd, You, move):
    if move in table and brd[move-1] == move-1:
        return True
    return False

def can_win(brd, You, move):
    places=[]
    x=0
    for i in brd:
        if i == You: 
            places.append(x);
        x+=1
    win=True
    for vi in win_comb:
        win=True
        for h in vi:
            if brd[h] != You:
                win=False
                break
        if win == True:
            break
    return win

def make_move(brd, You, move, undo=False):
    if can_move(brd, You, move):
        brd[move-1] = You
        win=can_win(brd, You, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)

# AI goes here
def computer_move():
    move=-1
    # If I can win, others don't matter.
    for i in range(1,10):
        if make_move(board_values, computer, i, True)[1]:
            move=i
            break
    if move == -1:
        # If player can win, block him.
        for i in range(1,10):
            if make_move(board_values, You, i, True)[1]:
                move=i
                break
    if move == -1:
        # Otherwise, try to take one of desired places.
        for vi in moves:
            for mv in vi:
                if move == -1 and can_move(board_values, computer, mv):
                    move=mv
                    break
    return make_move(board_values, computer, move)

def space_exist():
    return board_values.count('X') + board_values.count('O') != 9

You, computer = select_char()
print('Player is [%s] and computer is [%s]' % (You, computer))
result='%%% DRAW ! %%%'
while space_exist():
    print_board()
    print('# Make your move ! [1-9] : ', end='')
    move = int(input())
    moved, won = make_move(board_values, You, move)
    if not moved:
        print(' >> Invalid number ! Try again !')
        continue
    if won:
        result='*** Congratulations ! You won ! ***'
        break
    elif computer_move()[1]:
        result='=== You lose ! =='
        break;

print_board()
print(result)
