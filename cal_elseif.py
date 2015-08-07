#calculater
print ('''For addition Enter value of a is above 1..!
For addition Enter value of a is above 15..!
For addition Enter value of a is above 50..!''')

a=eval(input("Enter 1st nub:"))# first value
b=eval(input("Enter 2st nub:"))# second value
c=eval(input("Enter 3st nub:"))# third value
d=eval(input("Enter 4st nub:"))# foourth value

if a>1:
	z=a+b+c+d
	print("\nYour addition is :" , z) #addition of all nub..
elif a>15:
	x=d-c-b-a
	print("\nYour substarction is :" , x)# substraction of all nub..
	
elif a>50:
	y=a*b*c*d
	print("\nYour multiplication is :" , y)# multiplication of all nub..

