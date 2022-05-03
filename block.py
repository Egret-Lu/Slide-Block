import numpy as np
from fun import *
class Block():
    def __init__(self,state,last_block):
        self.__state=state #state of the bloc, an n*n array represent the position of each block
        self.__kind=state.shape[0] #3*3--3, 4*4--4
        self.__goal=Goal(state) 
        self.__last_block=last_block
        i=0
        block=self
        while block.get_last_block():
            i+=1
            block=block.get_last_block()
        past_step=i
        self.__h_score=M_distance(state,Goal(state))
        self.__g_score=past_step #here use past step as g score
        self.__score=M_distance(state,Goal(state))+past_step
        if last_block is None:
            self.__last_move=move_detect(state,None)
        else:
            self.__last_move=move_detect(state,last_block.get_state())
        #M_distance(state,Goal(state))
        #Score of initial state
    def get_state(self):
        return self.__state
    def get_kind(self):
        return self.__kind
    def get_goal(self):
        return self.__goal
    def get_score(self):
        return self.__score
    def get_h_score(self):
        return self.__h_score
    def get_g_score(self):
        return self.__g_score
    def get_last_block(self):
        return self.__last_block
    def get_last_move(self):
        return self.__last_move
    def set_step(self):
        i=0
        block=self
        while block.get_last_block():
            i+=1
            block=block.get_last_block()
        self.__past_step=i
    
        
    