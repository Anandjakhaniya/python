#function
def name():
	print "he11llo,Anand"
	print ('''For addition Enter value of a is above 1..!
For addition Enter value of a is above 15..!
For addition Enter value of a is above 50..!''')

	a=eval(raw_input("Enter your first value:"))# first value
	b=eval(raw_input("Enter your second value:"))# second value
	c=eval(raw_input("Enter your third value:"))# third value
	d=eval(raw_input("Enter your fourth value:"))# foourth value
#called that function
	
	print "\nYour ans is:\n",cal(a,b,c,d)
	

	
def sbcal(a,b,c,d):
	if a==0:
		z=a+b+c+d #addition of all nub..
		return z
		
	elif a>=10:
		x=d-c-b-a # substraction of all nub..
		return x
		
	elif a<10:
		y=a*b*c*d # multiplication of all nub..
		return y
	
def cal(a,b,c,d):

		if a==0:
			return sbcal(a,b,c,d)
			
		elif a>10:
			return sbcal(a,b,c,d)

		elif a<10:
			return sbcal(a,b,c,d)
		else:
			return whl(a)
def whl(a):

	def loop(a):
		i=0
		while i<=a:
		    if(i==11):
				break
		    print i
		    i +=1
			
	
	return loop(a)
		
name()
	#"Your addition :" ,
	#"Your substarction :" ,
	#"Your multiplication :" ,

	
