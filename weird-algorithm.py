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
ans=n
while ans>1:
    print(ans, end=" ")
    if ans%2==0:
        ans=ans//2
    else:
        ans=ans*3+1
if ans==1:
    print(ans,end=" ")
