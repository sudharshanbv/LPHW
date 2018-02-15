"""
1	#	this	one	is	like	your	scripts	with	argv
2	def	print_two(*args):
3	arg1,	arg2	=	args
4	print(f"arg1:	{arg1},	arg2:	{arg2}")
5
6	#	ok,	that	*args	is	actually	pointless,	we	can	just	do	this
7	def	print_two_again(arg1,	arg2):
8	print(f"arg1:	{arg1},	arg2:	{arg2}")
9
10	#	this	just	takes	one	argument
11	def	print_one(arg1):
12	print(f"arg1:	{arg1}")
13
14	#	this	one	takes	no	arguments
15	def	print_none():
16	print("I	got	nothin'.")
17
18
19	print_two("Zed","Shaw")
20	print_two_again("Zed","Shaw")
21	print_one("First!")
22	print_none()
"""
def print_two(*args):
    arg1, arg2 = args
    print (f"arg1 : {arg1}, arg2 : {arg2}")

def print_two_again(arg1, arg2):
    print (f"arg1 : {arg1}, arg2 : {arg2}")

def print_none():
    print ("I got nothing")

print_two("Zed","Shaw")
print_two_again("Zed", "Shaw")
print_none()
