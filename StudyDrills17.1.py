#LPTHW Study Drill from Ex17

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#We could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

#If we need a more simple version, we can delete the feature in line16.
#print(f"The input file is {len(indata)} byte long")

print(f"Does the output file exist?{exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

#We can use the same way(?) in line 13 to simplify this. 
#out_file = open(to_file,"w")
#out_file.write(indata)
open(to_file,"w").write(indata)

print("Alright, all done.")

#According to www.josharcher.uk   If you open and reading/writing the
#file immediately without storing, it will not be necessary to close the file.
#AND there is more sources about this question on 
#https://stackoverflow.com/questions/36046167/is-there-a-need-to-close-files-that-have-no-reference-to-them/36063184#36063184
#out_file.close()
#in_file.close()