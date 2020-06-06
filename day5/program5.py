def sorting(List):
    even=[]
    odd = []
     for x in List:
        if x % 2 == 0:
            even.append(x)
        else :
            odd.append(x)
    return sorted(odd, reverse = True) + sorted(even)

n= int(input())
l = []
for i in range(n):
    x=int(input())
    l.append(x)
print( str( sorting(l) ) [1:-1] )
