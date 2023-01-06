def fib(n):
     f1=0
     f2=1
     count=0
     while(count<n):
          print(f1)
          fib=f1+f2
          f1=f2
          f2=fib
          count+=1
n=int(input("enter the limit"))
print("the series is:")
fib(n)
