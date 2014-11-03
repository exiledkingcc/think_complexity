"""bisection: binary search"""

import random

def bisection(seq, item):
    low=0;high=len(seq)-1
    while low<high:
        mid=(low+high)//2
        if item<seq[mid]:
            high=mid-1
        elif item>seq[mid]:
            low=mid+1
        else:
            return mid
    return None

def test(script,a='1',b='20',*args):
    a=int(a)
    b=int(b)
    seq=[i for i in range(a,b,2)]
    print(*seq)
    ks=[ random.randint(a-1,b+1) for i in range(10)]
    for k in ks:
        print(k,bisection(seq,k))

if __name__=="__main__":
    import sys
    test(*sys.argv)
