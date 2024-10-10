# string formatting     it is a lenghthy way 
'''letter = "Hey my name is {} and I am from {}!!"
name = "Sameer Walia"
country = "India"
print(letter.format(name,country))
# print(letter.format(country, name))    #due to this our code will run but will give wrong output thatswhy f-string come

# in f-string we directly can add name of variables!!
print(f"Hey my name is {name} and I am from{country}!!!!") 


texts = 20.990987
print(f"I have {texts :.2f} dollars in my account..")  #this will only take 2 decimal values only'''



#doc-strings - these appears right after the definitions of a function,method,class,module (description)

def square(n):
    '''it takes a number and gives its square'''
    print(n**2)

square(5)
print(square.__doc__)


#python enhancement proposal - PEP8
import this        #(zen of python)