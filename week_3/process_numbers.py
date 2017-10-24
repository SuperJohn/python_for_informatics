# Class = python for data informatics
# Student = John Houghton

done = ''
numbers = []
while done != 'done':
    done = raw_input('add a number or type "done" to kill job > ')
    if done == 'done':
        total = sum(numbers)
        counts = len(numbers)
        maximum = max(numbers)
        average = float(sum(numbers)/len(numbers))
        print('\tnice! you killed the job! \n\nfinal numbers were' + str(numbers))
        break
    else:
        numbers.append(int(done))
        print('\tnumbers updated! ' + str(numbers))
print '\ntotal= ' + str(total), '\ncounts= ' + str(counts), '\nmaximum = ' + str(maximum), '\naverage = ' + str(average)