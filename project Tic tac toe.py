#!/usr/bin/env python
# coding: utf-8

# In[1]:


#new output


# In[2]:


board=[" "]*10


# In[3]:


from IPython.display import clear_output

def display(board):
    clear_output()
    print(board[7] +'  |  '+board[8]+'  |  '+board[9])
    print('--------------')
    print(board[4] +'  |  '+board[5]+'  |  '+board[6])
    print('---------------')
    print(board[1] +'  |  '+board[2]+'  |  '+board[3])
    
    


# In[4]:


#who goes first


# In[5]:


import random
def first_player():
    outcome=random.randint(0,1)
    if outcome==1:
        return 'player_1'
    else:
        return 'player_2'


# In[ ]:


def marker():
    mark='c'
    while mark not in ['X','O']:
        mark=input("enter the desired mark sir (x,o): ").upper()
    if mark =='X':
        return ('X','O')
    else:
        return ('O','X')


# In[7]:


#marker to place position


# In[8]:


def modification_fn(board,posi,mark):
    board[posi]=mark
    


# In[9]:


#checking if places are empty or not 


# In[10]:


def space_check(board,posi):
    if board[posi]==' ':
        return True
    else:
        return False


# In[11]:


def position(board):
    posi=0
    while posi not in [1,2,3,4,5,6,7,8,9,0] or not space_check(board,posi):
        
        posi= int(input("give the position of modification: "))
        if posi not in range(10):
            print("not the range we look for  :")
    return  posi


# In[12]:


def full_board(board):
    for i in range(10):
        if board[i]==' ':
            return False
    return True


# In[13]:


#win check condition of game
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[14]:


def replay():
    reply=input("wanna play again (Y or N): ").upper()
    if reply=='Y':
        return True
    else:
        return False


# In[ ]:


print("hey there welcome to my board game")
while True:
    display(board)
    player1_mark,player2_mark=marker()
    turn=first_player()
    if turn =='player_1':
        print(turn + " he will lead the game")
    else:   
        print(turn + " he will lead the game")
    
    play_game=input("give the order to play the game in (y or n): ").lower()              
    if play_game=='y':            
        game_on =True
    else:
        game_on=False
    while game_on:
        if turn =='player_1':
            display(board)
            posi=position(board)
            modification_fn(board,posi,player1_mark)
            if win_check(board,player1_mark):
                print(turn +'is the winner')
                game_on=False
                break
            if full_board(board):
                print("game is tie")
                game_on=False
                break
            else:
                turn='player_2'
        else:
            
            if turn =='player_2':
                display(board)
                posi=position(board)
                modification_fn(board,posi,player2_mark)
                if win_check(board,player2_mark):
                    print(turn +'is the winner')
                    game_on=False
                    break
                if full_board(board):
                    print("game is tie")
                    game_on=False
                    break
                else:
                    turn='player_1'
    if not replay():
        break
                    


# In[ ]:





# In[ ]:




