

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here is your file {filename}:")
print (txt.read())

txt.close()

print ("type the file name again: ", end=' ')
file_again = input()

txt_again = open(file_again)

print (txt_again.read())
txt_again.close()
