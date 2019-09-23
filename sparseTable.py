import math

def buildTable(arr):
    n = len(arr)
    k = math.floor(math.log2(n))+1
    table = [[-1]*k for i in range(n)]
    for i in range(0,n):
        table[i][0] = arr[i]
    j = 1
    while(1<<j) <= n:
        i = 0
        while i<= n -(1<<j):
            table[i][j] = math.gcd(table[i][j-1],table[i+(1<<(j-1))][j-1])
            i+=1
        j+=1
    return table

def query(L,R,table): 
    j = int(math.log2(R - L + 1))   
    return math.gcd(table[L][j],table[R - (1 << j) + 1][j]) 



arr = list(map(int, input().split()))
table = buildTable(arr)
print(table)
print(query(4,5,table))


