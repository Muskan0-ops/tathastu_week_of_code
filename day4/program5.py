votes = list(map(int, input().split()))
v = []
for name in votes:
    v.append((name, votes.count(name)))  
v.sort(key = lambda x : x[0], reverse = True )
v.sort(key = lambda x : x[1])
print("The name who won the election is", v[-1][0])votes = list(map(int, input().split()))
v = []
for name in votes:
    v.append((name, votes.count(name)))  
v.sort(key = lambda x : x[0], reverse = True )
v.sort(key = lambda x : x[1])
print("The name who won the election is", v[-1][0])
