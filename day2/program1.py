def p():
 n=int(input("Enter number:")
 if n%2==0:
      print("Given number is even")
 else:
    print("Given number is odd")
 N=str(n)
 rev=N[::-1]
 if(rev==N):
    print("number is palindrome")
 if(n<=3):
    print("no. is prime")
 else:
    flag=True
    for i in range(2,n):
        if(n%i==0):
            flag=false
            break
    if flag==True:
        prin("Number is prime")
 sum=0
 temp=n
 while(temp>0):
    d=temp%10
    sum=sum+(d**3)
    temp=temp//10
 if sum==n:
    print("given no. is armstrong")
