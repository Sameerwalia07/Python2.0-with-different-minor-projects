'''# ordered collection of data items and also we can change/alter list after creation

marks = [1,2,3,"Sameer",True, 7, 8, 9,77,44,47]
# print(marks(-3))        use len(marks)-3

if "Sameer" in marks:
    print("yes")
    
else:
    print("no")

if "Same" in "Sameer":
    print("Yes")
    
print(marks)
print(marks[1:4])
# jump index 
print(marks[1:7:2]) #here 2 means that we will print 1 index element then one gap and after that third element

# list comprehension
lst = [i for i in range (10)]
print(lst)

lst = [i for i in range (10) if i%2==0]
print(lst)'''

lst=[1,2,34,54,7,18,9,7,7]
print(list.append(77))
print(list.sort)
print(list.sort(reverse=True))
print(list.index(1))
print(list.count(7))

# Copy method in list
# m=lst
# m[0]=0
# print(m)

print(lst.insert(1, 899))

m=[900, 1000,1100]
print(lst.extend(m))   #it means we will join list m in the end of list lst

# join the list  
k=lst+m
print(k)

