for counter in range(10):
  print(counter)

for days in range(7):
  print("Day", days)

total = 10
for counter in range (100):
  total += 10
  print(total)

#Day19 challenge
loan = 1000
apr = 0.05
for i in range(10):
  loan+=(loan*apr)
  print("Year", i+1, "is", round(loan,2))
