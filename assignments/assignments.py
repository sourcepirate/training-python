# -----------------------------------------------------------
# demonstrates different kind of assignments
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# single assignments
colour = "blue"					# string assignment
size = 17						# integer assignment
length = 2.5					# float value assignment

print ("colour:", colour)
print ("size  :", size)
print ("length:", length)

# multiple assignments
a = b = c = 1					# set a, b, and c to 1
d,e = 2, 3						# set d to 2, and e to 3
print (("a,b,c : %i,%i,%i") % (a,b,c))
print (("d,e   : %i,%i") % (d,e))

# assignments with calculations
total = a + b - c + d -e		# simple addition
output = colour * 4				# concatenate a string four times
output2 = "light" + colour		# concatenate two strings
output3 = colour + str(total)	# concatenate a string with converted integer
print (("total : %i") % (total))
print (("colour: %s") % (colour))
print (("output: %s") % (output))
print (("output2: %s") % (output2))
print (("output3: %s") % (output3))

# print a partial string
partialString = output2[2:4]
print ("partialString:", partialString)
