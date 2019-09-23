import math
def buildBlocks(arr,ln,n):
    blocks = [0]*(ln)
    i = -1
    for j in range(n):
        if j%ln == 0:
            i+=1
        blocks[i]+=arr[j]
    return blocks

def query(arr,b,L,R,ln):
    ans = 0
    i = L
    while(i<R+1):
        if i%ln == 0 and i+ln-1 <=R:
            ans+=b[i//ln]
            i+=ln
        else:
            ans+=arr[i]
            i+=1
    return ans

def update(arr,b,i,val,ln):
    b[i//ln]+=val-arr[i]
    arr[i] = val    
    




arr = list(map(int, input().split()))
n = len(arr)
ln = math.floor(n**(1/2))+1
b = buildBlocks(arr,ln,n)
print(query(arr,b,3,8,ln))
print(query(arr,b,1,6,ln))
update(arr,b,8,0,ln)
print(query(arr,b,8,8,ln))

