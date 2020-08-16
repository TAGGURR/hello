def function():
	print("hi i am function")

function()	
def greet():
	print("hello")
	print("good morning")

greet()	

def add(x,y):
	c = x+y
	print(c)

add(5,4)	

def add(x,y):
	c = x+y
	return c

result = add(50,40)	
print(result)

def add_sub(x,y):
	c = x+y
	d = x-y
	return c,d

result = add_sub(500,400)	
print(result)

result1,result2 = add_sub(700,300)	
print(result1,result2)