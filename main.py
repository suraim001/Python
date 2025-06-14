# My new python project

print("I like Pizza")
print("It is good")
print("I want be a great Engineer\n")

# Strings
name = "SURAIM"
food = "Biryani"
email = "fawajsuraim@gmail.com"

print(name)
print(type(name))
print("\nHey guys")
print(f"MY name is {name}")# it is an f string where a variable can be used inside a string
print(f"My favourite food is: {food}")
print(f"My email is : {email}\n")

# Integer
age = 22
quantity = 3
num_of_students = 30

print(f"I am {age} years old")
print(f"i am buying {quantity} items")
print(f"My class has {num_of_students} students\n")

# float
price = 10.99
cgpa = 3.30
distance = 5.5

print(f"The price is {price} TK")
print(f"My CGPA is {cgpa}")
print(f"I have ran around {distance} kilometer.\n")

# Boolean
is_student = True
print(f"Am I a student? : {is_student}")

if is_student:
    print("Yes. I am a student.\n")
else:
    print("No. I am not a student.\n")

for_sale = False
print(f"Is the item for sale? : {for_sale}")

if for_sale:
    print("yes. The item is for sale.\n")
else:
    print("No. The item is not for sale.\n")

is_online = True
print(f"Am I online right now : {is_online}")

if is_online:
    print("Yes. I am.\n")
else:
    print("No. I am not.\n")


# TypeCasting = the process of converting a variable from one data type into another
#                 str(), int(), float(), bool(), ord()

name = "SURAIM"
age = 22
cgpa = 3.30
is_student = True

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

#TypeCast
cgpa = int(cgpa)
print(cgpa) # cgpa = 3
age = float(age)
print(age) # age = 22.0
age = str(age)
print(age) # age = '22.0'
print(type(age))
# age += 1 (TypeError: string + int
age += '1' # Will add 1 at the end of the str age
print(age) # '22.0' + '1' = '22.01'
age += 'a'
print(age) # '22.01' + 'a' = '22.01a'

name = bool(name)
print(name)

name = '10'
name = int(name) # Expects numerical integer character
print(name)

name = '159.344'
name = float(name) # Expects numerical float character
print(name)

#name = "SURAIM"
#name = int(name)
#print(name) # ValueError : Expects numerical integer character
#name = ord(name)
#print(name) # TypeError: ord() function only works on single character.
#              A sting cannot be converted into a Unicode value.
name = '1'
name = ord(name) # ord() function returns the Unicode value of any single character
print(name) # 49


#Take Input
#input() = A fuction that prompts the user to enter data
#          Returns the entered data as a string

name = input("What is your name? : ")
print(f"Hello, {name}!")
age = input("What is your age? : ")
#age += 1  #TypeError: str + integer

age = int(age)
age += 1
print(f"Wow! You are going to be {age} years old soon.")

cgpa = float(input("What is your CGPA? : "))
salami = cgpa * 10
print(f"I will get only {salami} TK as my EID bonus.")




