#builiding a calculator using python
a=int(input("enter your 1st number "))
b=int(input("enter your 2nd number "))
o=input("enter your sign")
if o=="+":
  print(a+b)
elif o=="-":
  print(a-b)
elif o=="*":
  print(a*b)
elif o=="/":
  print(a/b)
else:
  print("invalid operator")
