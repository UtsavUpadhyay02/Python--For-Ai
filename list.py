#list is a python Collections 
# it is indexed ,mutable means change ho skti hai 
# any datatype ke items hum isme daal skte hain
# ordered follow krti hai negative indexing bhi allow hai  isme
# means [banana , appple ,cherry] cg=herry ka index hoga -3 and apple ka -2 and so onn
# duplicate items bhi allow hain isme    
fruits=["Apple","Banana","Cherry","Guava"]
print(fruits)
print(type(fruits))
print(len(fruits))
# checking of items present or not in list 
if "Apple" in fruits:
    print("Apple is a part of list ")
print(fruits[1:3])# index 3 wala excluded hai ye 1 to 2 index wale item de dega     
#adding elements to a list
fruits.append("grapes") # end mai add kr dega list ke
print (fruits)
fruits.insert(3,"Anar")#ye 3 index pr anar ko add kr dega
print (fruits)
list=[1,2,3,4]
fruits.extend(list)# fruits and list ko jod degi 
print(fruits)
list2=[23,45,63,76,25,48,5,34,75,245,67]
list2.sort()
print(list2)
list2.sort(reverse=True)#descending order mai hoga
print(list2) 
list2.reverse()
print(list2)
#list comprehension
new_list=[i for i in list2 if  i>30]
print (new_list)
list=["new branch added named utsav-feat"]
