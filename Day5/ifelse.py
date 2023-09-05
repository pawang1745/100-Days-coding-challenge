# if else loops
name = input("what is your name? ")
print()

if name == "PAWAN":
    print("Access granted!!")
    print("Welcome to our community...")
else:
    print("Access denied")
    print("Please verify your name ")
    
#Day 5 challenge
print("Marvel character creator")
spiderman = input("Do you like 'hanging around?:")
korg = input("Do you have a 'gravelly' voice?:")
marvel = input("Do you often feel 'Marvelous?:")
print()

if spiderman == "yes":
    print("woo! you are spiderman. Hi!")
elif korg == "yes":
    print("Woo! you are korg. Hi!")
elif marvel == "yes":
    print("aha! you are captain marvel. Hello!")
else:
    print("AWW! Not fair.")

