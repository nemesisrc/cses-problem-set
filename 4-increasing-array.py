# https://cses.fi/paste/6079b3adbc3ba62196246f/
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
for i in range(1,n):
    if a[i]<a[i-1]:
        ans+=(a[i-1]-a[i])
        a[i]=a[i-1]
print(ans)
