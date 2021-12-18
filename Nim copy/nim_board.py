#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Author: Lauren Fisher
Class: CPSC323
Date: 10/21/2021
Desc: Nim Board class with methods to print game state and check if game is over
'''
class Nim_Board:
    def __init__(self):
        """
        initializes board for nim game with 1,3,5,7,9 NIM

        Parameters
        ----------
        none

        Returns
        -------
        none

        """
        self.state = []
        for row in range(5):
            self.state.append(2 * row + 1)
        
    def getValidMoves(self):
        """
        finds all valid moves for current game state

        Parameters
        ----------
        none

        Returns
        -------
        moves:

        """
        moves = []
        for row in range(len(self.state)):
            for num_tallies in range(1, self.state[row] + 1):
                moves.append((row, num_tallies))
        return moves
    
    def printWorld(self):
        """
        returns nicely printed board state list to be printed

        Parameters
        ----------
        none

        Returns
        -------
        none

        """
        for i in range(len(self.state)):
            print()
            print()
            print(i,end="")
            for j in range(self.state[i]):
                print(" " + "|", end=" ")
                
                
    def isEmpty(self):
        """
        checks to see if any rows are non-zero and returns true if so

        Parameters
        ----------
        none

        Returns
        -------
        isEmpty: whether or not list is empty

        """
        for row in self.state:
            if row > 0:
                return False

        return True
                      


# In[ ]:




