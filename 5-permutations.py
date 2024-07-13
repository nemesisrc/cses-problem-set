# https://cses.fi/paste/44fcd84a2b261caf963120/
import math
import sys
import threading
input = sys.stdin.readline
from collections import defaultdict as dd
from collections import deque
from collections import Counter
# sys.setrecursionlimit(3*(10**5)+50)
# threading.stack_size(10**8)
# t=threading.Thread(target=shouvik)
# t.start()
# t.join()
 
n=int(input())
if n==1:
    print(n)
elif n==2 or n==3:
    print("NO SOLUTION")
else:
    for i in range(2,n+1,2):
        print(i,end=' ')
    for i in range(1,n+1,2):
        print(i,end=' ')
