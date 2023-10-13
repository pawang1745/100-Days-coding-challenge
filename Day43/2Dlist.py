#2D List
my2DList = [ ["AJ", 21, "Mac"], ["Roman", 19, "PC"], ["Dean", 17, "PC"] ]
print(my2DList)
print(my2DList[0])
print(my2DList[0][0])
print("==================")
#Editing a 2D List
my2DList = [ ["AJ", 21, "Mac"],
   ["Roman", 19, "PC"],
   ["Dean", 17, "PC"] ]

my2DList[1][2] = "Linux"
# The line above changes list 1, item 2 from PC to Linux

print(my2DList[1])
# I'm using this line to output list 1 to check that the change has happened correctly.
print("==================")
#day43 challenge
print("Bingo game")
print("=================")
import random

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(ran())

numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

prettyPrint()
