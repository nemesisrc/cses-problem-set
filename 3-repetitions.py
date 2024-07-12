# https://cses.fi/paste/2df9b4c7fd0e9bf79616cd/
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
 
s=input()
ans=1
cnt=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        cnt+=1
    else:
        cnt=1
    ans=max(ans,cnt)
print(ans)
