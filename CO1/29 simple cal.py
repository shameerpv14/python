def add(a,b):
    c=a+b
    print("sum is",c)
def sub(a,b):
    c=a-b
    print("answer after sub is:",c)
def div(a,b):
    c=a/b
    print("answer after div is:",c)
def mul(a,b):
    c=a*b
    print("answer after mult is:",c)

x=int(input("enter the first num:"))
y=int(input("enter the second num:"))
z=input("enter the operation:")
if(z=='+'):
    add(x,y)
elif(z=='-'):
    sub(x,y)
elif(z=='/'):
    sub(x,y)
elif(z=='*'):
    sub(x,y)
