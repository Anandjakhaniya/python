#function
def name():
	print "he11llo,Anand"
	a=eval(raw_input("Enter your first value:"))
	b=eval(raw_input("Enter your second value:"))
#called that function
	
	print "Your ans is:",demo(a,b)
	
def demo(a,b):

	c=a+b
	return c


name()