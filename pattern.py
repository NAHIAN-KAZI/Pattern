# -*- coding: utf-8 -*-
"""Pattern.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15wXC_vYOwspZDLWYIDW0MII4LuEaXpVa
"""

#Increasing Triangle/Left Justified Triangle
n= int(input("Enter any nuber: "))
for i in range(n+1):
  for j in range(1,i+1):
    print(j,end=" ")
  print(" ")

#Rectangle
n=int(input("enter any number: "))
for i in range(n):
  for j in range(1,n+1):
    print(j,end=" ")
  print(" ")

#Increasing Triangle(Star)
n = int(input("Enter any number: "))
for i in range(n+1):
  for j in range(1,i+1):
    print("*",end=" ")
  print(" ")

#Right Justified Triangle(Space decreasing,star increasing)
n=int(input("Enter a number: "))
for i in range(n):
  for j in range(i,n):
    print(" ",end=" ")
  for k in range(i+1):
    print(" *",end="")
  print(" ")

#Hill Pattern (star)
n = int(input("Enter a number: "))
for i in range(n):
  for j in range(i,n):
    print("",end=" ")
  for j in range(i):
    print("*",end="")
  for j in range(i+1):
    print("*",end="")
  print(" ")

#Right Justified Triangle(Space decreasing,number increasing)
n = int(input("Enter any number: "))
for i in range(1,n+1):
  for j in range(i,n+1):
    print(" ",end = " ")
  for k in range(1,i+1):
    print("",k,end="")
  print(" ")

#Hill pattern(Number)
n = int(input("Enter any number: "))
for i in range(1,n+1):
  for j in range(i,n+1):
    print("",end = " ")
  for k in range(1,i+1):
    print(k,end="")
  for l in range(1,i):
    print(l,end="")
  print("")

#Decreasing Triangle
n = int(input("Enter any number: "))
for i in range(1,n+1):
  for j in range(i,n+1):
    print(j,end=" ")
  print(" ")

#Decreasing Triangle(star)
n = int(input("Enter any number: "))
for i in range(1,n+1):
  for j in range(i,n+1):
    print("*",end=" ")
  print(" ")