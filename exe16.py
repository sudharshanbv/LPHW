

from sys import argv

script, filename = argv

print (f"we are going to erase the comtents of the file {filename}")
print ("if you dont want that to happen press Ctrl-C")
print ("if you have no problem with that hit RETURN")
input()
print ("opening the file....")
target = open(filename, 'w')

print ("Truncating the file...")
#target.truncate()

print ("Now i'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these lines to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally we close it")
target.close()
