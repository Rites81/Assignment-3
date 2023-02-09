#!/usr/bin/env python
# coding: utf-8

# # Assignment 3 based on tuples

# ##  Tuples help to store multiple items in a sings variable.
# ## characteristics of tuple:
#   ###  It is a Ordered and changeable.
#    ### It allow dublicate item.
#   ###  tuple are immutable.
#   ### it also follow concatenation property.
# ### Yes, tuble is immutable it means we didn't able to change its items

# In[12]:


# The two method of tuple is - count() and index()
# count() help to identify the position of item.
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res=Tuple.count(3)
print("count of tuple 3 is::",res)
res=Tuple.count(1)
print("count of tuple 1 is::",res)



# In[26]:


#index() help to identify the presence of item.

Tuple = (0,3,5,7,3,2,5,8,2,6)
res = Tuple.index(7)
print("Index of 7 is::",res)
res = Tuple.index(8)
print("Index of 8 is::",res)

# Because of tuples are immutable, they are faster than the list because they are static in python.


# ## Set() is unique datatype how didn't allow duplicate items we can use build-in-set() function to convert list to a set. 

# In[29]:


#list in python
list = [1,1,1,2,1,3,1,4,2,1,2,2,2,3,2,4,3,1,3,2,3,3,3,4,4,1,4,2,4,3,4,4]
print(list)

# set in python
list1={1,1,1,2,1,3,1,4,2,1,2,2,2,3,2,4,3,1,3,2,3,3,3,4,4,1,4,2,4,3,4,4}
print(list1)


# # Difference between union() and update()
# 
# ##  union() set method is use to contain all the value of diifernt set and make single set where all elementare present there. union() set mehin is use to contain all the value of diifernt set and make single set where all elementare present there.
# 
# ## Update() set method is use to update a value in different set using update keyword, Python update() function in set adds elements from a set (passed as an argument) to the set. 

# In[31]:


A = {1,2,3,4,"Ritesh","Python"}
B = ("Course",6,22)
print("All element are ::",A.union(B))


# In[35]:


A = {1,2,3,4,"Ritesh","Python"}
B = ("Course",6,22)
set1=set(B)
set2=set(A)
set1.update(set2)
print(set1)


# # Dictionary is used to store data in a key and value pair. Dictionary define keyword is dict(). Dictionary written in curly bracketes.
# 
# ## Dictionary are ordered item.

# In[38]:


item = {
    "Name" : "Ritesh",
    "Course" : "Data SCience",
    "Location " : "New Delhi"
}
print(item)


# In[39]:


item = {
    "Name" : input(),
    "Course" : input(),
    "Location " : input()
}
print(item)


# # A dictionary can contain dictionaries, this is called nested dictionaries.

# In[49]:


person1={
   "Name":"Rites",
    "Work":"Bussiness",
    "year":2012
}
person2={
     "Name":"Vikas",
    "Work":"Workshop",
    "year":2010
}
person3={
     "Name":"Sachin",
    "Work":"Entrepreneur",
    "year":2017
}
myemployee={
    "person1": person1,
    "person2": person2,
    "person3": person3
}
print(person1)
print(person2)
print(person3)


# # Setdefault()

# In[53]:


dict1 = {
  "language": "python",
  "Course": "Data science master"
}
list = ["python","Machine learning","Deep learning"]
x = dict1.setdefault("course", "Machine Learning")

print(x)
print(list)


# ## The main three view objects of dictionary in python are keys, values and items.

# In[57]:


dict1 = {'sport':"cricket","team":["India","New Zealand","South Africa","England","Australia","Sri Lanka"]}
keys = dict1.keys()
values = dict1.values()
print(keys)
print(values)
print(dict1)


# In[ ]:




