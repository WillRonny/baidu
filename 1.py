# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:12:45 2018

@author: Will
"""

N,M=map(int,input().split())
x = [1]   # 一个解（n元0-1数组）
X = []   # 一组解
# 冲突检测：无
    
# 一个例子
def conflict2(k):
    global N, x, X
    if x[k] == x[k+1]:
        return True
    if k==0:
        return False
    return False # 无冲突
   
# 子集树递归模板
def subsets(k): # 到达第k个元素
    global N, x, X
    if len(x) == N:  # 求和目标值
        X.append(x[:])
 # 保存（一个解）
    else:
        for i in [i for i in range(1,M)]: 
            x.append(i)
            if not conflict2(k): # 剪枝
                subsets(k+1)
            x.pop()            # 回溯
subsets(0)
result = []
for j in X:
    if j[-1] !=1:
        result.append(j)
     
print(len(result)%(10**9+7))

