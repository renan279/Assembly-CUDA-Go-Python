import numpy as np
import time
from queue import PriorityQueue
import random
import math
global pq
import copy
pq=PriorityQueue()
global pq_list
pq_list=[]

class Node:
    def __init__(self,N=0):
    
        self.state=np.zeros((N,N))
        self.g_x=0
        self.h_x=0
        self.cost_so_far=0
        self.parent= None

def is_goal(state):
    x=np.where(state == 1)
    N=len(state)
    for i in range (len(x[0])):

        row=x[0][i]
        col=x[1][i]
        
        count=0
        for i in range(N):
            if(state[row][i]==1):
                count=count+1
        
        if count>1:
            return 0
        
        count=0
        for i in range(N):
            if(state[i][col]==1):
                count=count+1
        
        if count>1:
            return 0
        
        count=0
       
        #primeira Diagonal 
        row1=row-1
        col1=col-1
        
        while row1>=0 and row1<N and col1>=0 and col1<N:
           
            if(state[row1][col1]==1):
                return 0
            row1=row1-1
            col1=col1-1
        
        row1=row+1
        col1=col+1
        
        while row1>=0 and row1<N and col1>=0 and col1<N:
            
            if(state[row1][col1]==1):
                return 0
            row1=row1+1
            col1=col1+1
            
        row1=row-1
        col1=col+1
        
        #secunda diagonal
        while row1>=0 and row1<N and col1>=0 and col1<N:
            
            if(state[row1][col1]==1):
                return 0
            row1=row1-1
            col1=col1+1
            
        row1=row+1
        col1=col-1
        
        while row1>=0 and row1<N and col1>=0 and col1<N:
            
            if(state[row1][col1]==1):
                return 0
            row1=row1+1
            col1=col1-1
            
    return 1

def random_state(N):
    
    board=np.zeros((N,N))
    print("Criando estado aleatorio para N =",N)
    for x in range(N):
        row=random.randrange(0,N)
        #print(row,x)
        board[row][x]=1

    return board

def cal_heuristic(state):
    N=len(state)
    x=np.where(state == 1)
    attack=[]
    count=0
    for i in range (len(x[0])):
        #print (x[0][i],x[1][i])
        row=x[0][i]
        col=x[1][i]
        
        #mesma lina
        for i in range(N):
            if(state[row][i]==1 and i!=col):
                
                count=count+1
                attack.append([[row,col],[row,i]])
        
        #mesma coluna
        for i in range(N):
            if(state[i][col]==1 and i!=row):
                count=count+1
                attack.append([[row,col],[row,i]])
                        
        #primeira diagonal - cima esq
        row1=row-1
        col1=col-1
        
        while row1>=0 and row1<N and col1>=0 and col1<N:
            
            if(state[row1][col1]==1):
                count=count+1
                attack.append([[row,col],[row1,col1]])
            row1=row1-1
            col1=col1-1
        
        #baixo dir
        row1=row+1
        col1=col+1
        
        while row1>=0 and row1<N and col1>=0 and col1<N:
            
            if(state[row1][col1]==1):
                count=count+1
                attack.append([[row,col],[row1,col1]])
        
            row1=row1+1
            col1=col1+1
            
        row1=row-1
        col1=col+1
        
        #secunda diagonal - cima dir
        while row1>=0 and row1<N and col1>=0 and col1<N:
            
            if(state[row1][col1]==1):
                count=count+1
                attack.append([[row,col],[row1,col1]])
        
            row1=row1-1
            col1=col1+1
            
        row1=row+1
        col1=col-1
        
        #baixo esq
        while row1>=0 and row1<N and col1>=0 and col1<N:
            
            if(state[row1][col1]==1):
                count=count+1
                attack.append([[row,col],[row1,col1]])
        
            row1=row1+1
            col1=col1-1
    temp=math.floor((count/2))
    if temp==0:
        return 0
    return (10+math.floor((count/2)))


def cal_g(state1,state2):
    if (np.array_equal(state1,state2)==0):
        changed_state=np.absolute(state1-state2)
        ones=np.where(changed_state==1)[0]
        ones2=np.where(changed_state==1)[1]
        diff=abs(ones[1]-ones2[1])
        return (10+(diff*diff))
    else:
        return 10

def populate(x):
    global pq
    global pq_list
    a=None
    temp=None
    state=np.copy(x.state)
    for col in range(len(state)):
        state=np.copy(x.state)
        for row in range(len(state)):
            temp=None
            
            temp=Node()
            temp.parent=x
            
            for k in range(len(state)):
                state[k][col]=0
            
            state[row][col]=1
            temp.state=state
            temp.h_x=cal_heuristic(temp.state)
            temp.g_x=cal_g(temp.state,x.state)
            temp.cost_so_far=temp.h_x+temp.g_x+x.g_x
            if np.array_equal(x.state,temp.state)==0:
                a=copy.deepcopy(temp)
                pq_list.append(a)
                
                pq.put((temp.cost_so_far,len(pq_list)-1))

def print_soln(state1):
    list_soln=[]
    while(state1.parent!=None):
        list_soln.append(state1.state)
        state1=state1.parent
    print ("RAMIFICAÇAO",float(len(pq_list)/len(list_soln)))
    while(len(list_soln)!=0):
        a=list_soln.pop()
        print(a)

N=8
time_start=time.clock()
start_state=random_state(N);
print("INICIANDO ESTADO INICIAL")
print(start_state)
start=Node()
start.state=start_state
while(True):
    populate(start)
    next_indice=pq.get()
    print("Indice",next_indice[1])
    next_state=pq_list[next_indice[1]]
    print("Proximo Estado")
    print (next_indice[0])
    print(next_state.state)
    if(is_goal(next_state.state)==1):
        time_end=time.clock()
        print("Solucionado!")
        print_soln(next_state)
        print("Numero de nos expandidos ",len(pq_list))
        print ("Efetividade na solução do problema ",next_state.cost_so_far)
        print ("Tempo total ",time_end-time_start)
        break
    
    start=next_state