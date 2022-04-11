'''
@Author: Sai Tarun
@Date: 2022-04-09 17: 30: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-09 17: 55: 00
@Title: Tic Tac Toe.
'''
import random

board=[i for i in range(0,9)]
player, computer = '',''

# Corners, Center and Others, respectively
moves=((1,7,3,9),(5,),(2,4,6,8))
# Winner combinations
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
# Table
tab=range(1,10)

def print_board():
    """
        Description:
            Will prints the design for the game with 9 blocks.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns nothing but prints game design with 9 blocks. 
    """
    x=1
    for i in board:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            if i != 1: end+='---------\n';
        char=' '
        if i in ('X','O'): char=i;
        x+=1
        print(char,end=end)
        
def select_char():
    """
        Description:
            Used to print random char.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns random character. 
    """
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars

def can_move(brd, player, move):
    """
        Description:
            Used to return random char.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns random character. 
    """
    if move in tab and brd[move-1] == move-1:
        return True
    return False

def can_win(brd, player, move):
    """
        Description:
            Used to return random char.
        Parameter:
            Passed parameters brd,player,move. 
        Return:
            Returns win. 
    """
    places=[]
    x=0
    for i in brd:
        if i == player: places.append(x);
        x+=1
    win=True
    for tup in winners:
        win=True
        for ix in tup:
            if brd[ix] != player:
                win=False
                break
        if win == True:
            break
    return win

def make_move(brd, player, move, undo=False):
    """
        Description:
            checks weather the movement is possible ot not.
        Parameter:
            Passed parameters brd,player,move. 
        Return:
            Returns status is true or false for brd and player. 
    """
    if can_move(brd, player, move):
        brd[move-1] = player
        win=can_win(brd, player, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)

# AI goes here
def computer_move():
    """
        Description:
            used to return required fields.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns board,count,move. 
    """
    move=-1
    # If I can win, others don't matter.
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move=i
            break
    if move == -1:
        # If player can win, block him.
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move=i
                break
    if move == -1:
        # Otherwise, try to take one of desired places.
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move=mv
                    break
    return make_move(board, computer, move)

def space_exist():
    """
        Description:
            used to count board count.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns board count. 
    """
    return board.count('X') + board.count('O') != 9
if __name__ == '__main__':
    player, computer = select_char()
    print('Player is [%s] and computer is [%s]' % (player, computer))
    result='%%% Draw ! %%%'
    while space_exist():
        print_board()
        print('# Make your move ! [1-9] : ', end='')
        move = int(input())
        moved, won = make_move(board, player, move)
        if not moved:
            print(' >> Invalid number ! Try again !')
            continue
        #
        if won:
            result='*** Congratulations ! You won ! ***'
            break
        elif computer_move()[1]:
            result='=== You lose ! =='
            break;
    print_board()
    print(result)