#!/usr/bin/env python
# coding: utf-8

# In[1]:

'''
Author: Lauren Fisher
Class: CS323
Date: 10/21/2021
Desc: Main file handling game logic of Nim game of AI playing against itself until game is over
'''

from nim_board import Nim_Board
from nim_player import NimPlayer

NUM_PLAYERS = 3;

def playGame():
    """
    handles logic for game where developed ai plays against eachother following same strategy until board is empty

    Parameters
    ----------
    none

    Returns
    -------
    none

    """
    players = []

    for _ in range(NUM_PLAYERS):
        new_player = NimPlayer()
        players.append(new_player)

    nim_board = Nim_Board()
    nim_board.printWorld()
    print()
    history = []
    
    j=0
    while not nim_board.isEmpty():
        for player in players:
            # make a move here
            print("Player: " + str(j + 1))
            new_move = player.play(nim_board.state, history)
            history.append(new_move)
            for i in range(len(nim_board.state)):
                nim_board.state[i] += new_move[i]
                
            nim_board.printWorld()
            j += 1
            print()
            if nim_board.isEmpty():
                break



def main():
    playGame()


# In[2]:


main()


# In[ ]:




