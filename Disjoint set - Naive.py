"""
This article discusses the data structure Disjoint Set Union or DSU. Often it is also called Union Find because of its two main operations.
This data structure provides the following capabilities. We are given several elements, each of which is a separate set. A DSU will have an operation to combine any two sets, and it will be able to tell in which set a specific element is. The classical version also introduces a third operation, it can create a set from a new element.
Thus the basic interface of this data structure consists of only three operations:

make_set(v) - creates a new set consisting of the new element v

union_sets(a, b) - merges the two specified sets (the set in which the element a is located, and the set in which the element b is located)

find_set(v) - returns the representative (also called leader) of the set that contains the element v. This representative is an element of its corresponding set. It is selected in each set by the data structure itself (and can change over time, namely after union_sets calls). This representative can be used to check if two elements are part of the same set of not. a and b are exactly in the same set, if find_set(a) == find_set(b). Otherwise they are in different sets.


Time Complexity = O(n)
"""


"""
Suppose there n element , We store elements in an array
We Just Store the parent of element

first All the element in the unique set , All are indepedent

When We Union the set , We Simply Change the Parent of a element

"""
def makeSet(v):
    parent[v] = v

def findSet(v):
    if(v == parent[v]):
        return v
    return findSet(parent[v])

def unionSet(a,b):
    a = findSet(a)
    b = findSet(b)
    if(a != b):
        parent[b] = a

n = 5        
parent = [0]*n
for i in range(n):
    makeSet(i)

q = 4
print(parent)
unionSet(1,2)
print(parent)
unionSet(0,4)
print(parent)
unionSet(2,3)
print(parent)
