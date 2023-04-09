#!/usr/bin/env python
# coding: utf-8

# # New code- heading

# In[4]:


'data science' #shift+enter


# In[12]:


print('hello world', 'Welcome to my own world', sep= ' & ') #to separate two string we use sep &


# In[13]:


var= 'hello world'
print(var)


# In[14]:


var= 'hello world' 
print('var') #'' use korle string hisebe print korbe


# In[15]:


var= 'hello world'
print('My name is '+var) #to use this +var the benefit is we dont have to write it again


# In[16]:


id(var) # to see which location it was saved


# In[17]:


import sys
sys.getsizeof(var) # to know how much memory byte need


# In[1]:


x=10
x


# In[2]:


x,y,z=1,2,3
print(x,y,z)


# In[3]:


x


# In[4]:


var


# In[6]:


var_2=10
var_2


# In[7]:


Var_2 #case sensitive


# In[8]:


var_2


# In[9]:


varsityid


# In[10]:


varsity_id


# In[12]:


varsity_id =1810057
varsityid =1810057
varsity_id #looks perfect snake case


# In[13]:


varsityid #not perfect


# # local vs global

# In[5]:


v=300 #global

def func1():
    v=200 #local
    print('my price is: ',v)
    func1()


# In[31]:


print('my price is: ',v)


# In[6]:


v=300 #global

def func1():
    v=200 #local
    print('my price is: ',v)
    func1()


# In[ ]:




