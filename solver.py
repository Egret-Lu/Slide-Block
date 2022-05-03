from block import *
import numpy as np
import time
class Solver():
    def __init__(self,state_1,max_loop=100000):
        self.__state_1=state_1
        self.__time=time
        self.__step=0
        self.__state_path=[]
        self.__move_path=[]
        self.__is_success=0
        self.__max_loop=max_loop

        
    def get_state_1(self):
        return self.__state_1
    def get_time(self):
        return self.__time
    def get_state_path(self):
        return self.__state_path
    def get_move_path(self):
        return self.__move_path
    def get_step(self):
        return self.__step
    def get_is_success(self):
        return self.__is_success
    
    def BFS(self):
        history=[]
        start_time = time.perf_counter()
        max=self.__max_loop
        scan_list=[]
        cur_block=Block(self.__state_1,None)
        n=self.__state_1.shape[0]
        scan_list.append(cur_block)
        i=0
        flag=0
        while i<=max and scan_list!=[] and time.perf_counter()<=start_time+60:
            if i%10000==0:
                if self.__max_loop>100000:
                    print('Current nodes:'+str(i))
                else:
                    pass
                
            i+=1
            cur_block=scan_list.pop(0)
            cur_state=cur_block.get_state()
            if (cur_state==cur_block.get_goal()).all():
                #reach the
                flag=1
                end_time=time.perf_counter()
                self.__time=end_time-start_time
                block=cur_block
                self.__state_path.insert(0,cur_state)
                self.__move_path.insert(0,'')
                while block.get_last_block():
                    state=block.get_last_block().get_state()
                    move=block.get_last_move()
                    self.__state_path.insert(0,state)
                    self.__move_path.insert(1,move)
                    block=block.get_last_block()
                self.__step=len(self.__move_path)-1
                self.__is_success=1
                #print('Success')
                break
            zero_loc=np.where(cur_state==0)
            cur_x=zero_loc[0][0]
            cur_y=zero_loc[1][0]
            move_x=[1,-1,0,0]
            move_y=[0,0,1,-1]
            for x,y in zip(move_x,move_y):
                new_x=cur_x+x
                new_y=cur_y+y
                if new_x>=0 and new_x<n and new_y>=0 and new_y<n:
                    new_state=np.array(cur_state)
                    new_state[cur_x,cur_y],new_state[new_x,new_y]=new_state[new_x,new_y],new_state[cur_x,cur_y]
                    new_block=Block(new_state,cur_block)
                    if str(new_state) not in history:
                        history.append(str(new_state))
                        scan_list.append(new_block)
                    else:
                        continue
        if flag==0:
            print('The problem can not be solved by BFS')
                
    def A_star(self):
        history=[]
        out_history=[]
        start_time = time.perf_counter()
        max=self.__max_loop
        scan_list=[]
        cur_block=Block(self.__state_1,None)
        n=self.__state_1.shape[0]
        scan_list.append(cur_block)
        i=0
        flag=0
        while i<=max and scan_list!=[]:
            if i%10000==0:
                if self.__max_loop>100000:
                    print('Current nodes:'+str(i))
                else:
                    pass
            i+=1
            cur_block=scan_list.pop(0)
            cur_state=cur_block.get_state()
            if (cur_state==cur_block.get_goal()).all():
                #reach the
                flag=1
                end_time=time.perf_counter()
                self.__time=end_time-start_time
                block=cur_block
                self.__state_path.insert(0,cur_state)
                self.__move_path.insert(0,'')
                while block.get_last_block():
                    state=block.get_last_block().get_state()
                    move=block.get_last_move()
                    self.__state_path.insert(0,state)
                    self.__move_path.insert(1,move)
                    block=block.get_last_block()
                self.__step=len(self.__move_path)-1
                self.__is_success=1
                #print('Success')
                break
            zero_loc=np.where(cur_state==0)
            cur_x=zero_loc[0][0]
            cur_y=zero_loc[1][0]
            move_x=[1,-1,0,0]
            move_y=[0,0,1,-1]
            for x,y in zip(move_x,move_y):
                new_x=cur_x+x
                new_y=cur_y+y
                if new_x>=0 and new_x<n and new_y>=0 and new_y<n:
                    new_state=np.array(cur_state)
                    new_state[cur_x,cur_y],new_state[new_x,new_y]=new_state[new_x,new_y],new_state[cur_x,cur_y]
                    new_block=Block(new_state,cur_block)
                    if str(new_state) not in history:
                        history.append(str(new_state))
                        scan_list.append(new_block)
                        scan_list.sort(key=lambda x: x.get_score())
                    else:
                        continue
        if flag==0:
            print('The problem can not be solved by A*')
        
                    
                
            
            
        

    
        
    