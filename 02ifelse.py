# Day 4

'''applePrice = 210
budget = int(input("Enter a budget: "))

if applePrice <= budget:
    print("Alexa, add 1Kg apples in the cart..")
    
else:
    print("Alexa, don't add apples in the cart..")'''
    
    
'''num = int(input("Enter a number: "))

if num < 0:
    print("The number is negative!!")
    
elif num == 0:
    print("The number is equal to zero!!")
    
elif num == 77:
    print("The number is special!!")
    
else:
    print("The number is positive!!")
    
print("I am happpy now!!")'''


# nested if-else

num = int(input("Enter a number: "))

if num < 0:
    print("The number is negative!!")
    
elif num > 0:
    if num <= 10:
        print("The number is positive, and also between 1-10!!")
        
    elif num > 10 and num <= 20:
        print("The number is greater then 10 but less then 20 i.e. between 11-20!!")
        
    else:
        print("The number is positive, and more then 20!!")
        
else:
    print("The number is equal to zero!!")