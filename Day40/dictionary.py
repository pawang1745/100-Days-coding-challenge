#Dictionary

myUser = {"name": "David", "age": 128}


print(myUser["name"])

# This code outputs 'David'.
#changing item
myUser = {"name": "David", "age": 128}

myUser["name"] = "The legendary David"
print(myUser)

# This code outputs 'name:'the legendary David', 'age':'128.
print()
name = input("Name: ").strip().capitalize()
dob = input("Date of Birth: ").strip()
tel = input("Telephone number: ").strip()
email = input("Email: ")
address = input("Address: ")
contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}

print()
print(f"""Name: {contact["name"]}""")
print(f"""DOB: {contact["dob"]}""")
print(f"""Tel: {contact["tel"]}""")
print(f"""Email: {contact["email"]}""")
print(f"""Address: {contact["address"]}""")
