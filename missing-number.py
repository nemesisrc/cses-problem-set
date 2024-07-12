# https://cses.fi/paste/429f467d49a621679608e2/
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
a=[int(x) for x in input().split()]
ans=0
for i in range(n-1):
    ans=(ans^a[i])^(i+1)
ans=ans^n
print(ans)
