

from sys import argv
from os.path import exists

script, frm_file, to_file = argv

print (f"copying from {frm_file} to {to_file}")

in_file = open(frm_file)
indata = in_file.read()

print (f"the input file is {len(indata)} bytes long")

print (f"Does the output file exists? {exists(to_file)}")

print ("Hit return to countinue or Ctrl-C to abort")
input()

out_file = open (to_file, 'w')
out_file.write(indata)

print ("copying done")
out_file.close()
