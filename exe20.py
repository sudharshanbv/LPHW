
from sys import argv

script, input_file = argv

current_file = open(input_file)

def print_all(f):
    print (f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_num, f):
    print (line_num, f.readline())

print ("first lets print the whole file:\n")
print_all(current_file)

print ("now lets rewind the file to print again ")

rewind(current_file)

"""
Why	are	there	empty	lines	between	the	lines	in	the	file?
The readline()	function	returns	the	\n	that’s	in	the	file	at	the	end	of
that	line.	Add	a	end	=	""	at	the	end	of	your	print	function	calls
to	avoid	adding	double	\n	to	every	line.
"""
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
