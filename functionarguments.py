'''def average(a=7, b=1):   # here a and b are default arguments
    print("Average is= ", (a+b)/2)
    # average(4,6)
    
average(3)  #we give a new value for a and for b default value is taken

def name(fname="Sameer",lname="Walia",age=20):
    print("My name is ",fname, lname," and my age is", age)
    
name("Anchal")

#Keyword Arguments:  in this we can add elements in any order
average(b=9,a=7)'''

def average(*numbers):   #  * is used for taking n number of arguments
    sum=0
    for i in numbers:
        sum=sum+i
    # print("Average of numbers is:",sum/len(numbers))
    return(sum/len(numbers))
    
c=average(5,5,7,1)
print(c)