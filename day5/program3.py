def stolen(l):
    if len(l) == 2:
        return max(l)
    if len(l) == 1:
        return l[0]
    if len(l) == 3:
        return max(l[1], l[0] + stolen(l[2:]))
    return max(l[1] + stolen(l[3:]), l[0] + stolen(l[2:]))
n = int(input("Enter the number of Houses: "))
L = []

for i in range(n):
    a =int(input())
    l.append(a)
        
result = stolen(l)
print(result)
