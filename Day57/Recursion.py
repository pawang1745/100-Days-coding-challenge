#Recursion
def reverse(value):
  if value <= 0:
    print("Done!")
    return


  else:
    for i in range(value):
      print("100", end="")
    print()
    reverse(value - 2)
reverse(5)
print("============")
print("challenge")
#Day 57 challenge
def factorial(value):
  if value == 1:
    return 1
  else:
    return value * factorial(value-1)

print(factorial(5))
