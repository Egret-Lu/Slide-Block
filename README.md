


## Contents

- [Backgroud](#Background)
- [Install](#install)
- [Usage](#usage)
- [Badge](#badge)
- [Example Readmes](#example)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)

## Background

This project is designed for solving a slide block game. In the directory we used two kind of algorithmns - BFS and A*.  Both of them are basic methods of problem solving and this project apply them to slide block game to see in what level each of them are effective.

## Install

To use the method in this project you need to import the module in the directory

```python
from solver import *
#the project also use some ready modules including numpy and time
```

## Usage

To use the slide block problem solver, you need to build a Solver object and attribute the functions in the object. The solution of the game will be included in the object and you can attribute solution by using attribute funtion.

```python
#initial state a should be an numpy.array 
a=np.array([[1,4,2],[3,0,5],[6,7,8]])
#build a solver object
s=Solver(a)
#solve problem with A*
s.A_star()
#you can also solve the problem with BFS by using:
#s.BFS()
```



## Example 

The example shows how to use the slide block solver and how to attribute the solution. Here I list an example code to show how to layout the solution.The output will print each step of the solution and current status of the block.

```python
a=[[1,4,2],[3,0,5],[6,7,8]]
a=np.array(a)
s=Solver(a)
s.A_star()
print('A* done the problem in '+str(s.get_time())+' seconds, and the solution includes '+str(s.get_step())+ ' steps')
for state,move in zip(s.get_state_path(),s.get_move_path()):
    print(move)
    print(state)
```

```
A* done the problem in 0.006938504000000734 seconds, and the solution includes 2 steps

[[1 4 2]
 [3 0 5]
 [6 7 8]]
move 4 down
[[1 0 2]
 [3 4 5]
 [6 7 8]]
move 1 right
[[0 1 2]
 [3 4 5]
 [6 7 8]]
```

## Maintainers

Xinxuan Lu (Lucinda)

ID: 31870054

