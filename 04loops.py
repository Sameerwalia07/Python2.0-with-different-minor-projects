# Day - 5



'''name = "Sameer"
for i in name:
    print(i)
    if i == "a":
        print("This is special")'''
        
    
'''colors = ["Red", "Blue", "White", "Green", "Orange"]
for color in colors:
    print(color)
    for i in color:
        print(i)'''
        
        
# print numbers 1 to 20 using for loop

# for i in range( 0, 21, 2):  #2 is the steps
#     print(i)


# while loop
'''i=4
while(i<25):
    i=int(input("Enter a number: "))
    print(i)
    # i = i+1
    
print("The loop is done")'''

# Decrementing while loop
'''num = 7
while(num>0):
    print(num)
    num = num-1'''
    
    
# Break Statement - in this we came out from the loop

for i in range (18):
    if i == 10:
        break
    print("5 X ", i+1,"=", 5*(i+1))
    
print("Exited the loop!!")

#Continue statment - in this we skip the iteration
for i in range(14):
    if i == 10:
        continue
    print("5 X",i,"=", 5*(i+1))
    
print("Skipped the iteration!!")
   
   