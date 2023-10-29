#Palindrome
#Day 59 challenge
def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])

print(palindrome("malayalam"))

print()
print("Aliter")

def is_palindrome(input_string):

  clean_string = input_string.replace(" ", "").lower()

  return clean_string == clean_string[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
  print("The input is a palindrome.")
else:
  print("The input is not a palindrome.")
