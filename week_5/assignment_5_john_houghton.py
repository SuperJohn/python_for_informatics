import re
import string

fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    if re.search('^From.+@', line) :
        parsed = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
        if len(parsed) > 0 :
            parsed = parsed[0]
            if parsed not in counts:
                counts[parsed] = 1
            else:
                counts[parsed] += 1

# Sort the dictionary by value
lst = list()
for key, val in counts.items():
    lst.append( (val, key) )

lst.sort(reverse=True)

for key, val in lst[:100] :
    print key, val