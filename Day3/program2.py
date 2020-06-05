from itertools import permutations
def permut():
 s=input("enter string")
 perms = [''.join(p) for p in permutations(s)]
 print(perms)
