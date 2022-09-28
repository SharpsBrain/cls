#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def myfunc(self):
        print("Hi! My name is "+self.name)
        
p1=Person("Sharps",19)
p1.myfunc()


# In[3]:


class Person:
    def __init__(mysillyobject,name,gender):
        mysillyobject.name=name
        mysillyobject.gender=gender
        
    def myfunc(abc):
        print("hi i am a "+abc.gender)
p1=Person("Sharps","male")
p1.myfunc()


# In[ ]:




