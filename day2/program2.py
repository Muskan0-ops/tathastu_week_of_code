def fib(n):
    
    if(n<0):
        print("ivalud number")
    elif(n==1):
        return(0)
    elif(n==2):
        return(1)
    else:
        return(fib(n-1)+fib(n-2))
    
    n=int(input("enter the number:"))
    
    for i in range(n):
      print(fib(i+1),end="")
 
