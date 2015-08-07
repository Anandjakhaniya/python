#dectionary

sub = eval(raw_input("Enter your number of Subject :"))
dic={}
for x in range(0,sub):
	Sub_name=raw_input("Enter your first Subject :")
	#Sub_no=raw_input("Enter your Subject no:")
	Sub_mark=raw_input("Enter your marks of Subject :")
	dic[Sub_name]=Sub_mark
print dic