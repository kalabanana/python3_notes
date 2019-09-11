##Variables & Formats:

name = "Bob"
greeting = f"Hello, {name}"

or 

name = "John"
greeting = "Hello, {}"
with_greeting = greeting.format(name)

##Tuple, List, and Set:

list = [1,2,3,4] ## can be modify, access, add, or remove
tuple = (1,2,3) ## cannot be modified, no add or remove
set = {1,2,3,4} ##not in order, no duplicates, no subscription notation
singleTuple = (1,)

##Set: finding the difference

friends = {"Angelababy","Lily","Thomas"}
abroad = {"Yao","Lily","Thomas"}
local = abroad.difference(friends) ## print - {"Yao"}
international = friends.difference(abroad) ## print - {"Angelababy"}

##Set: Union

numb1 = {1,2,3,4}
numb2 = {4,5,6}
unionNum = numb1.union(numb2) ## print {1,2,3,4,5,6}

numb1.append(10) ## will add 10 to numb1 set

if...elif...else

numbers_collected =  7
user_number = input("Enter 'y' if you like to play").lower()

if user_number == "y":
	user_input = int(input("Great! Let's guess our number"))
	if user_input == numbers_collected:
		print("You guessed correctly")
	elif abs(numbers_collected-user_input)  == 1:
		print("You are one number off")
	else:
		print("Wrong")
		
else:
	print("Play next time!")
	
	
numbers_collected =  6

while True:
	user_number = input("Would you like to play?(y/n)")
	if use_number == "n":
		break
		
	user_input = int(input("Great! Let's guess our number"))
	if user_input == numbers_collected:
		print("You guessed correctly")
	elif abs(numbers_collected-user_input)  == 1:
		print("You are one number off")
	else:
		print("Wrong")
		
##For loop:

friends = ["Rolf","James","Apple"]

for friend in friend:
	print(f"{friend} is my friend")
	
for friend in range(4): ## create a list with list of numbers


##Sum and length:

grades = [45,67,89,100]
total = sum(grades)
people = len(grades)
average = total/people

##List Comprehension:

numbers = [1,2,3,4]
double = [i * 2 for i in numbers]

workers = ["Soul","Sam","Samantha"]
start_s = [worker for worker in workers if worker.startswith("S")]
print(workers is start_s) ##false, list comparing to another list is false; they have different ID - relating to memory address
print(workers[0] is start_s[0]) ## true

##Dictionaries:

friend_ages = {"Rolf": 25, "Adam":26, "Anne":29}
print(friend_ages["Adam"]) ## 26
friend_ages["Bob"] = 28
#{"Rolf": 25, "Adam":26, "Anne":29, "Bob":28}

friends = [
	{"name":"Adam","age":25},
	{"name":"Ada","age":26},
	{"name":"Ally","age":28},
]

## destructuring the set of key value pairs onto friend and ages
## If there's not enough value to destruct, it will return value error
for friend, ages in friend_ages.items():
	print(f"{friend}: {ages}")
	
if "Adam" in friend_ages:
	print("Adam is one of my friends")
	

Destructuring:

t = 1,5
x, y = t
print(x) ##1
print(y) ##5


head, *tail = [1,2,3,5,6]
##head will be the first value
##tail would be the rest

*head, tail = [1,2,3,5,6]
##head will be rest of the value
##tail would be the last value


#Function

def hello():
	print("Hello World")
	
#created a callable variable 

def user_age_in_seconds():
	user_age = int(input("Enter your age:"))
	age_seconds = user_age*365*24*60*
	print(f"{age_seconds} is how many seconds in your age.")


user_age_in_seconds
print("Thanks for using.")

animal = []

def add_animal():
	animal.append("Wolf")

add_animal()
add_animal()
add_animal()

print(animal) ## ['Wolf','Wolf','Wolf']

def say_hello(surname, name):
	print(f"Hello, {name} {surname}")

say_hello(name="Bob",surname="Smoth")

or 

say_hello("Smoth", name="bob")
#positional arguments go first and keyword arguments go later

def add(x, y=8):
	return x+y
add(5) #print 13, default parameter must go at the end

default_y = 3

def add(x, y=default_y)
	return x + y
	
default_y = 6

##Do not recommend assigning variable name as the value in an parameter, and dafult_y will not change to 6 because y is defined when the function is created and it will not change after when you try to reassign

None: #means no value, missing value or undeclared in python


#Lambda functions: #exclusively use for I/O, can be difficult to read

lambda x,y: x + y
# no need to specify return key word

#function that has a name
add = lambda x,y: x+y
print(add(5,6)) #11

# ex.1
def double(x):
	return x*2
	
sequence = [1,3,5,9]
doubled = [double(x) for x in sequence]
#similar to js
doubled = map(double, sequence)

#lambda function
doubled = list (map (lambda x:x*2, sequence))
#map will return a map object, surround by list to see them in console


# Dictionary comprehension
user = [
	(0,"Rolf","password")
	(1,"Bob","usernam1")
	(1,"Bob1","usernam12")
]

user_mapping = {user[1]: user for user in users}
#prints {"Rolf": (0,'Rolf','password')}

username_input = input("Enter your username")
password_input = input("Enter your password")

_, user, passw = user_mapping[username_input]

if password_input == password:
	print ("You are Login")
else:
	print("Sorry, the password did not match")
	
#Multiple Args
def multiply (*args):
	total = 1
	for arg in args:
		total = total * arg
	return total
	
print(multiply(1,3,4)) 
print(multiply(-1))

def add(x,y):
	return x+y
	
num = [4,5]
print(add(*num)) ## very similar to spread function

##In dictionary term

nums = {"x":2, "y":25}
print(add(**nums))



##Touples

def apply(*arg, operator):
	if operator == "*":
		return multiply(*args) ## unpack it so to takes in the individual value in touple
	elif operator == "+":
		return sum(args)
	else:
		return "No valid operator provided to apply()"
		
print(apply(1,3,4,6, operator = "*"))


#Dictionary

def named(name, age):
	print(name, age)
	
details = {"name": "Bob", "age":25}

named(details) ## yield {"name": "Bob", "age":25}
named(**details) ## yield  Bob 25
