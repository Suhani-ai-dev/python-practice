n=int(input("enter a number of rows:"))
for i in range(n,0,-1):
    print(" " * (n-i)+ "*" * (2*i-1))