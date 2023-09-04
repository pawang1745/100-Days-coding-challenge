#story creation using print statement
print("Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create "
      "an epic story with you as the star!")
print()

name = input("What is your name? ")
enemy_name = input("What is your worst enemy’s name? ")
superpower = input("What is your superpower? ")
place = input("Where do you live? ")
food = input("What is your favorite food? ")
print()

print("Hello" , name , "!" , "your ability to" , superpower ,"will make sure you never have to look at" ,
      enemy_name , "again." , "Go eat" , food , "as you walk down the streets of" , place , "and use" ,
      superpower , "for good and not evil!")

#printing using color code
print("Uh, oh, David! you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")
