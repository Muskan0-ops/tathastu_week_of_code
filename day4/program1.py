def element():
    tuples=input("enter tuple")
    element=input("enter the element to be checked")
    count=0
    for i in tuples:
        if(i==element):
            count=count+1
    print(count)
