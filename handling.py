# Import

#mymodule.py ->
def divide(dividend, divisor):
	return dividend/divisor

print("module name: ", __name__)
#code.py	
from mymodule import divide

import sys
print(sys.path) #first path always the path of the file u ran


# adding a libs folder
#path = module/libs/mylib.py
#sometimes it require the __init__.py file

## Catching error

def divide (dividend, divisor):
	if divisor == 0 :
		return ZeroDivisionError("No 0")
	
	return dividend/divisor

grades =[]

try:
	average = divide(sum(grades), len(grades))
	print(f"The grade point average is {average}.")
except ZeroDivisionError as e:
	print(e) # prints "No 0"
	print("There are no grades yet")
else:
	# not putting in try block
	print(f"The grade point average is {average}.")
finally:
	print("Thanks")

	
#Types of Error
RuntimeError
ValueError
TypeError
CustomeErrors - created by programmer

class TooManyPagesReadError(ValueError):
	pass

class Book:
	def __init__(self, name:str, page_count:int):
		self.name = name
		self.page_count = pages
		self.page_read = 0
		
	def __repr__(self):
		return(
		f"<Book {self.name}, read{self.page_read} out of {self.page_count}>"
		)
		
	def read(self, pages:int):
		if self.page_read + pages > self.page_count:
			raise TooManyPagesReadError(
				f"You are trying to read too many pages, this book only has {self.page_count}"
			)
		
		self.page_read += pages
		print(f"You now read {self.page_read} pages out of {self.page_count}.")

python101 = Book("Python 101", 100)
try:
	python101.read(20)
	python101.read(90)
except TooManyPagesReadError(e):
	print(e)
