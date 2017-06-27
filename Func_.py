#Changeable parameters
def calc(*number):    #can be seen as a list/tuple
                      #automatically seen  
    s=0
    for n in number:
        s=s+n*n
    return s

#This input must be a list or tuple without the star mark
def calc(number):    #can be seen as a list/tuple
                      #automatically seen  
    s=0
    for n in number:
        s=s+n*n
    return s


#Default parameters
def defunc(x,n=2):    #if no input of n, the n is defaulted as 2
    s=0
    while n>0:
        n-=1
        s=s+x*x
    return s
#f(*arg,**arc)funtion can be used 
#All different kinds of 
print(calc(1,2,3,4))  #just input directly without be in list or tuple style  
print(defunc(3,4))
        
