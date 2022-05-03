import numpy as np
def Goal(state):
    #return the goal block
    n2=state.shape[0]*state.shape[1]
    goal=np.arange(1,n2)
    goal=np.insert(goal,0,0).reshape(state.shape[0],state.shape[1])  
    return goal

def Check(state):
    #Check whether state is a correct block
    if state.shape[0]!=state.shape[1]:
        print('Shape of block is wrong, number of row and column should be same')
        return False
    n2=state.shape[0]*state.shape[1]
    for i in range(n2):
        if i in state and i < n2-1:
            continue
        elif i in state and i== n2-1:
            print('The block is correct')
            return True
        else:
            print('There is number miss in the block')
            return False

        
def M_distance(state,goal):
    #manhattan distance calculator
    if state.shape!=goal.shape:
        print('Goal shape different from Block shape')
        exit(1)
    score=0
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            a=abs(goal[i,j]-state[i,j])
            score+=a
    return score
 
def move_detect(state,last_state):
    #detect each step's movement - move which number in what direction
    #e.x: move 3 right
    if last_state is None:
        str_1='no move'
        return str_1
    zero_loc_cur=np.where(state==0)
    zero_loc_last=np.where(last_state==0)
    cur_x=zero_loc_cur[0][0]
    cur_y=zero_loc_cur[1][0]
    last_x=zero_loc_last[0][0]
    last_y=zero_loc_last[1][0]
    x=cur_x-last_x
    y=cur_y-last_y
    if x==-1:
        str_1='move '+str(state[last_x,last_y])+' down'
        return str_1
    elif x==1:
        str_1='move '+str(state[last_x,last_y])+' up'
        return str_1
    elif y==-1:
        str_1='move '+str(state[last_x,last_y])+' right'
        return str_1
    elif y==1:
        str_1='move '+str(state[last_x,last_y])+' left'
        return str_1
    
def read_problem(file_path):
    #just for sample problem sets
    arr=[]
    file = open(file_path)
    lines=file.read()
    lines=lines.split('\n')
    n=len(lines)
    for i in range(1,n-1):
        if lines[i][0].isdigit():
            line=lines[i]
            line=line.split(' ')
            for j in range(len(line)):
                line[j]=int(line[j])
            arr.append(line)
    return arr
          
            