# Class = python for data informatics
# Student = John Houghton

string = raw_input('provide the string to parse >')
my_float = float(string[string.find(':')+2:])
print my_float
print type(my_float)