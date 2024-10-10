# a function is a block of code that is used for performing particular tasks whenever it is called

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if a>b:
     print("First number is greater!!")
    
    else:
     print("Second number is greater or equal!!")
        
    
a = 9
b = 8

isGreater(a, b)

# if a>b:
#     print("First number is greater!!")
    
# else:
#     print("Second number is greater or smaller!!")
# gmean1 = (a*b)/(a+b)
# print(gmean1)
calculateGmean(a, b)
c = 8
d = 44

isGreater(c, d)
# if (c>d):
#     print("First number is greater!!")
    
# else:
#     print("Second numbe ris greater or equal!!")
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean(c, d)