
st = str(input("Enter string  "))
s = ""
for i in st:
    if i not in s:
        s = s+i
print(" After removing duplicate of string:", s)
