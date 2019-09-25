a = list(map(int, input().split()))
n = len(a)
t = [0]*(4*n)

def buildSegmentArray(v,tl,tr):
    if(tl == tr):
        t[v] = a[tl]
    else:
        tm = (tl+tr)//2
        buildSegmentArray(v*2,tl,tm)
        buildSegmentArray(v*2+1,tm+1,tr)
        t[v] = t[v*2]+t[v*2+1]


def querySum(v,tl,tr,l,r):
    if(l>r):
        return 0
    if(l == tl and r == tr):
        return t[v]
    tm = (tl+tr)//2
    return querySum(v*2,tl,tm,l,min(r,tm))+querySum(v*2+1,tm+1,tr,max(l,tm+1),r)

def update(v,tl,tr,pos,new_val):
    if(tl == tr):
        t[v] = new_val
    else:
        tm = (tl+tr)//2
        if(pos <=  tm):
            update(v*2,tl,tm,pos,new_val)
        else:
            update(v*2+1,tm+1,tr,pos,new_val)
        t[v] = t[v*2]+t[v*2+1];
    


# 1index
buildSegmentArray(1,0,n-1)
print(querySum(1,0,n-1,0,4))
update(1,0,n-1,3,4)
print(querySum(1,0,n-1,0,4))
"""
Segment Tree:
    Use complete binary tree concept for build up and query
    Based upon Recursion
    
O(n) = Build up Time Complexity
O(n) = Space Complexity (4n size)
O(logn) = Query Complexity
"""
