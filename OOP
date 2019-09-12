# Oject Oriented

class Student:
	def __init__(self, name,grades):
		self.name = name
		self.grades = grades

	def average(self):
		return sum(self.grades)/len(self.grades)
		
student = Student("Bob",(80,94,67,85))
student2 = Student("Bob",(85,90,45,89))
print(student.name)
print(student.grades)
# Bob

print(student.average())
print(student2.average())

class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
	def __str__(self):
		return f"Person {self.name}, {self.age} years old."
	## this will print a nice to read string

bob = Person("Bob", 35)
print(bob)  #this prints out a OBJECT without __str__ method

print(str(bob)) # this prints in string 

# Exercise
class Store:
    def __init__(self,name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        items = {'name':name,'price':price}
        self.items.append(items)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = 0
        
        for item in self.items:
            total += item['price']
        
        return total

		
class ClassTest:
	def instance_method(self):
		print(f"Called instance_method of {self}") #singletone?
	
	@classmethod
	def class_method (cls):
		print(f"Called class_method {cls}") #use a factories
		
	@staticmethod
	def static_method ():
		print("Called static_method.")
		
test = ClassTest()
#print the instance
ClassTest.class_method()
# will pass the ClassTest into the argument itself

ClassTest.static_method()
#its own seperate function that lives inside a function


class Book:
	TYPES = ("hardcover","paperback")
	#only book will use it?
	
	def __init__(self, name, book_type, weight):
		self.name = name
		self.book_type = book_type
		self.weight = weight
		
	def __repr__(self):
		return f"<Book {self.name}, {self.book_type}, weight {self.weight}>"
	
	@classmethod
	def hardcover(cls, name, page_weight)
		return cls(name, cls.TYPES[0], page_weight + 100)
		
	##new object inside a class
	
	@classmethod
	def paperback(cls, name, page_weight)
		return cls(name, cls.TYPES[1], page_weight)
		
print(book.name)
book = Book("Book Name","hardcover",250)
# does not check the book type

book = Book.hardcover("name 2", 100)
lightbook = Book.paperback("name 3", 100)


##Exercies
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))
