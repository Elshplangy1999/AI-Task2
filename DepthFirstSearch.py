# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:47:22 2021

@author: Emad Elshplangy
"""

adj_list={
         'A':['B','C'],
         'B':['D','E'],
         'C':['B','F'],
         'D':[],
         'E':['F'],
         'F':[],
        }
 
Color={}
Parent={}
Traverse_time={}
 
dfs_traverse_output=[]
for node in adj_list.keys():
    Color[node]='W'
    Parent[node]=None
    Traverse_time[node]=[-1,-1]
print(Color)     
print(Parent)     
print(Traverse_time)     
time=0
def dfs(u):
    global time
    Color[u]='G'
    Traverse_time[u][0]=time
    dfs_traverse_output.append(u)
    for v in adj_list[u]:
        if Color[v]=='W':
            Parent[v]=u
            dfs(v)
    Color[u]='B'
    Traverse_time[u][1]=time
    time+=1
dfs('A')
print()
print(Parent)     
print(Color)     
print(dfs_traverse_output)
for node in adj_list.keys():
    print(node,"=>",Traverse_time[node])




















    
