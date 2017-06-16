#-*-coding: UTF-8-*-
#Filename: extract.py

#make the item be standard type
def standnize(the_string):
    if '-' in the_string:
        spliter='-'
    elif ':' in the_string:
        spliter=':'
    else:
        return(the_string)
    (mins,secs)=the_string.split(spliter))
    return(mins+'.'+secs)

#try to open the file
def getdata(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        temp=data.strip().split(','))
        return({'name':temp.pop(0),'dob':temp.pop(0),
                'time':str(sorted(set(standize(t) for t in temp))[0:3])})
    except IOError as ioerr:
        print('Fiel error: '+str(ioerr))
        return(None)
    
list1=getdata('test.txt')
