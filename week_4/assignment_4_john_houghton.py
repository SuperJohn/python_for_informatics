# use file romeo.txt

filename = raw_input('what is the name of the file? > ')
try:
    my_file = open(filename)
except:
    print filename , ' cannot be found.'
    exit()
script_list = []
for line in my_file:
    line_list = line.split()
    # take the first line and split it
    for word in line_list:
        # check to see whether it's in script_list
        if word.lower() not in script_list:
            # if it's not in script_list, append it
            script_list.append(word.lower())
        else:
            continue
script_list.sort()

string = raw_input('what string do you want to count? > ')
counter = 0
for word in script_list:
    if string in word:
        counter += 1
    else:
        continue
print '\'' + string + '\'' + ' appears ' + str(counter) + ' times.'