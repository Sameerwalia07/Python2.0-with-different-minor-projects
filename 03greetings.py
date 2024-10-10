import time
timestamp = (time.strftime('%H:%M:%S'))#strf is a function that gives us hour and minutes
print(timestamp)
hour = int(time.strftime('%H'))
# hour = int(input("Enter the hour: "))    for taking input from user
# timestamp = int(time.strftime('%M'))
# timestamp = int(time.strftime('%S'))

if  hour>=0 and hour<12:
    print("Good Morning!!")
    
elif hour>=12 and hour<18:
    print("Good Afternoon!!")
    
elif  hour>=18 and hour<20:
    print("Good Evening!!")

else:
    print("Good Night!!")
