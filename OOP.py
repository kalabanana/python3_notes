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

		
##

class Device:
	def __init__(self, name, connected_by)
		self.name = name
		self.connected_by = connected_by
		self.connected = True
	
	def __str__ (self):
		return f"Device {self.name!r} ({self.connected_by})"
		# !r wrapper into quotes
		# Device 'Printer 250' (Phone)
		
	def disconnect(self):
		self.connected = False
		print("Disconnected")
		
printer = Device ("Printer 250", "Phone")
print(printer)

#now to disconnect
printer.disconnect() #prints Disconnected


## Inheritance, keyword IS: printer is a Device
class Printer(Device):
	def __init__(self, name, connected_by, capacity):
		super().__init__(name, connected_by)
		self.capacity = capacity # max capacity
		self.remain_pages = capacity # how much it remains
		
	def __str__(self):
		return f"{super().__str__()} ({self.remain_pages} ava. pages remain)"
	
	def printing(self, pages):
		if not self.connected:
			print("Printer is not connected")
			return
		print(f"Printing {pages} pages.")
		self.remain_pages -= pages
		
printer = Printer("Printer 111", "USB", 500)
printer.printing(20)

print(printer)
# Device 'Printer' (USB) (480 ava. pages remain)

printer.disconnect()
# it will try to start looking from Printer, if it's not there, then it goes up to Device, and Device actually inherits from Python Object Class (3 level check)

printer.printing(50)
# Printer is not connected


#Composition, keyword HAS, Bookshelf HAS books

class BookShelf:
	def __init__ (self, *books):
		self.books = books
	
	def __str__(self):
		return f"BookShelf with {len(self.books)} books."
		
shelf = BookShelf(300)

class Book:
	def __init__(self,name):
		self.name = name;
		
	def __str__(self):
		return f"Book {self.name}"
		
book = Book("Book Name1")
book2 = Book("Book Name2")

shelf = BookShelf(book, book2)

print(shelf)

#Type Hinting 3.5

def list_avg(sequence: List) -> float: #signal to return Float type
	return sum(sequence) / len(sequence)

list.avg(123) 
# it will hint that you should use a LIST not integer

class Book:
	def __init__(self, name: str, page_count: int):
		self.name = name
		self.page_count = page_count
		
class Book:
	TYPES = ("hardcover","paperback")
	#only book will use it?
	
	def __init__(self, name: str, book_type, weight:int):
		self.name = name
		self.book_type = book_type
		self.weight = weight
		
	def __repr__(self) -> str:
		return f"<Book {self.name}, {self.book_type}, weight {self.weight}>"
	
	@classmethod
	def hardcover(cls, name: str, page_weight:int) -> "Book":
		return cls(name, cls.TYPES[0], page_weight + 100)
		
	##new object inside a class
	
	@classmethod
	def paperback(cls, name: str, page_weight:int) -> "Book":
		return cls(name, cls.TYPES[1], page_weight)
		
