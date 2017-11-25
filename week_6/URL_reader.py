# author = John Houghton

import urllib

# url = 'http://www.py4inf.com/code/romeo.txt'
url = raw_input('Enter URL read from > ')

try:
    fhand = urllib.urlopen(url)
except:
    print 'File cannot be opened: \"' + url + '\" Maybe try adding \"http://\" ?'
    exit()

print '\n'
characters = 0    
for line in fhand:
    line = line.strip()
    chars = len(line)
    characters += chars
    if characters < 3000:
        print line

print '\n<<< Exiting. The complete document had ' + str(characters) + ' characters, exceeding the 3k character print limit. >>>\n'