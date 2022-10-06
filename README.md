#Rectangle
for i in range(5):
  for j in range(1,7):
    print(j,end=" ")
  print(" ")

#Left_Justified_Triangle
for i in range(5):
  for j in range(1,i+1):
    print(j,end=" ")
  print(" ")
  
#Right_Justified_Triangle
n=5
var = n-1
for i in range(1,n):
  print(" "*var,end=" ")
  for j in range(0,i):
    
    print("*",end="")
  print(" ")
  var-=1
