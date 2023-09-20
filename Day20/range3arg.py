#specifying range values using range()
for i in range (100,110):
  print(i)
#13 times table using range()
for j in range(1,11):
  print(j,"x13=",j*13)
#printing values by skipping a specified gap of numbers using third argument in range()
for k in range(1,200,25):
  print(k)
#printing in reverse order
for l in range(10,0,-1):
  print(l)
#fixing the error
for m in range (20, 40, 1):
  print(m)

#day 20 challenge
print("List generator")
print()
s=int(input("enter start value: "))
e=int(input("enter end value: "))
inc=int(input("enter increment value: "))
for n in range(s,e,inc):
  print()
  print(n)
  
