# Tuples are the ordered collection of data items, and are immutable.

'''tup = (1,2,77,567,983, "Green")
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[4])

if 567 in tup:
    print("Yes 567 in tup!!")
    
print(tup[1:5])
print(len(tup)) # still it will return the original length after slicing also'''


'''countries = ("Bharat", "Italy", "Spain", "Germany", "Laos", "France", "Paris")
#as tuple is immutable so we firstly convert it into list
temp = list(countries)
temp.append("Russia")     # add item
temp.pop(3)          # remove item
temp[5] = "Finland"    # change item
countries = tuple(temp)
print(countries)

countries2 = ("Canada", "Singapore", "Japan", "Thailand")
my_countries = countries + countries2
print(my_countries)'''



tup = (1,2,3,45,3,78,57,93,3,11,23,3)
res = tup.count(3)
print("The number 3 occured", res, "times")
res1 = tup.index(3)   #it will give us the index of 1st 3.
print(res1)
res2 = tup.index(3, 5, 9)  #it will tell us the index of number 3 that is present between index 5-9
              # no.,index1=from where slicing start,index2=slicing end  
print(res2)


