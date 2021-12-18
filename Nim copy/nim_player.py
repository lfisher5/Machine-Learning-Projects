#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Author: Lauren Fisher
Class: C323
Date: 10/21/2021
Desc: Nim Player class with methods enabling valid moves to be found and and played 
'''

import copy
import random

class NimPlayer:
    def __init__(self):
        self.first_player = False;
        self.second_player = False;
        self.third_player = False;
        self.end_game_reached = False;
    
    
    def findMove(self, state, possible_moves):
        """
        checks to see if specific board states are present if end game has been reached and if not tries to find a move 
        where there are an even number of groups of 1's, 2's, and 4's or if not at least try to 
        preserve an even number of tallies

        Parameters
        ----------
        state: list of number of tallies left in each row
        possible_moves: list of possible moves to make from given move

        Returns
        -------
        move: list containing row to take from and number of tallies to take

        """
        resulting_state = []
        optimal_move_found = False
        num_tallies = sum(state)
        new_move = [0,0,0,0,0]
        for i in range(len(possible_moves)):
            resulting_state = copy.deepcopy(state)
            resulting_state[possible_moves[i][0]] -= possible_moves[i][1]
            if(sum(resulting_state) == 1 or sum(resulting_state) == 2):
                new_move[possible_moves[i][0]] -= possible_moves[i][1]
                return new_move
            ones = 0
            zeros = 0
            for k in range(len(state)):
                if(state[k] == 1):
                    ones += 1
                if(state[k] == 0):
                    zeros += 1
            groups = [0,0,0]
            for j in range(len(state)):
                if(resulting_state[j] / 4 >= 1):
                    groups[2] += 1
                    resulting_state[j] -= 4
                if(resulting_state[j] / 2 >= 1):
                    groups[1] += 1
                    resulting_state[j] -= 2
                if(resulting_state[j] / 1 >= 1):
                    groups[0] += 1
                    resulting_state[j] -= 1
            if(num_tallies > 7):
                if(sum(resulting_state) > 7): 
                    new_move[possible_moves[i][0]] -= possible_moves[i][1]
                    return new_move
                else:
                    self.end_game_reached = True;
            if(self.end_game_reached):
                max_value = max(state)
                min_value = min([value for value in state if value!=0])
                max_index = state.index(max_value)
                min_index = state.index(min_value)

                if(max_value > 3):
                    new_move[max_index] -= 1
                    return new_move
                for o in range(len(state)):
                    if(zeros == 4):
                        if(num_tallies == 3 and state[o] > 1):
                            new_move[o] -= 2
                            return new_move 
                    if(zeros == 3 and num_tallies > 4):
                        max_value = max(state)
                        max_index = state.index(max_value)
                        if(state[max_index] > 2):
                            new_move[max_index] -= 3
                            return new_move
                        new_move[max_index] -= 2
                        return new_move
                    if(zeros > 1 and num_tallies < 4):
                        if(state[o] > 0):
                            new_move[o] -= 1
                            return new_move
                    if(zeros > 1):
                        max_value = max(state)
                        max_index = state.index(max_value)
                        # if(state[max_index] > 2):
                        #     new_move[max_index] -= 3
                        #     return new_move
                        if(state[max_index] > 1):
                            new_move[max_index] -= 2
                            return new_move 
                        new_move[max_index] -= 1
                        return new_move 

            if(groups[0] % 2 == 0 and groups[1] % 2 == 0 and groups[2] % 2 == 0):
                optimal_move_found = True
                new_move[possible_moves[i][0]] -= possible_moves[i][1]
                return new_move


        for l in range(len(state)):
            if(num_tallies % 2 == 0 and state[l] > 1):
                new_move[l] -= 1
                return new_move
        for l in range(len(state)):
            if(num_tallies % 2 != 0 and state[l] > 0):
                new_move[l] -= 1
                return new_move
        for l in range(len(state)):
            if(state[l] > 0):
                new_move[l] -= 1
                return new_move
                    
  
    def getMoves(self, state):
        """
        creates list valid nim moves which can be made from current state

        Parameters
        ----------
        state: list of number of tallies left in each row

        Returns
        -------
        moves: list of possible moves that can be made for given state

        """
        moves = []
        for row_index in range(len(state)):
            for amount in range(1, min(state[row_index] + 1, 4)):
                moves.append((row_index, amount))
        return moves

    def getPrevStates(self, state, history):
        """
        

        Parameters
        ----------
        state: list of number of tallies left in each row

        Returns
        -------
        moves: list of possible moves that can be made for given state

        """
        if(len(history) == 0):
            self.first_player = True
        elif(len(history) == 1):
            self.second_player = True
        elif(len(history) == 2):
            self.third_player = True




    

    

    def play(self, state, history):
        """
        gets possible moves and from them, choose valid move based on created algorithm and returns updated state

        Parameters
        ----------
        state: list of number of tallies left in each row

        Returns
        -------
        new_state: updated list of number of tallies left in each row

        """
        possible_moves = self.getMoves(state)
        self.getPrevStates(state, history)
        move_chosen = self.findMove(state, possible_moves)

        move = [0,0,0,0,0]    
        if(self.second_player or self.third_player):
            rand_move = possible_moves[random.randint(0, len(possible_moves)-1)]
            move[rand_move[0]] -= rand_move[1]
            print(move)
            return move

        print(move_chosen)
        return move_chosen
           
    


# In[ ]:




