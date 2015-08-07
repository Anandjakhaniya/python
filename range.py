print "\n This is a new for loop"
day = ["sunny day","warm day","high tempreture"]
a=eval(raw_input("Enter you tempreture value:"))
b=eval(raw_input("Enter you tempreture value:"))
for tempre in range(a,b):
	if tempre<=35 and tempre>31:
		print day[0]
	elif tempre>35 and tempre<40:
		print day[1]
	elif tempre>40 and tempre<50:
		print day[2]
	else:
		print "invalid"