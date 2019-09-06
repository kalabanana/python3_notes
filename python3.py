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

for friend, ages in friend_ages.items():
	print(f"{friend}: {ages}")
	
if "Adam" in friend_ages:
	print("Adam is one of my friends")