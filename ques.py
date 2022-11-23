#numbers = [1,2,3,4,5,2,6]

#num = numbers.copy()
#print(num2)

#newlist = [x**2 for x in numbers]
#print(newlist)

#indx = numbers.index(2)
#numbers[indx] = 200
#print(numbers)




list1 = ["x", "y", "z"]
list2 = [1,2,3]
#list3 = list1 + list2
#print(list3)
for x in list2:
 #   list1.append(x)
#print(list1)
list1.extend(list2)
print(list1)