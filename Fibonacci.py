n=int(input("enter the number of terms  "))
a=0
b=1
s=0

for x in  range(n):
 print(s,end=" ")
 s=a+b
 b=a
 a=s
 
 enter the number of terms  13
0 1 1 2 3 5 8 13 21 34 55 89 144 
