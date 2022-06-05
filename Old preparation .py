#!/usr/bin/env python
# coding: utf-8

# In[2]:


name = "Dhaval"
my_string = f"hello {name}"
print(my_string)


# In[3]:


name = "Dhaval"
my_string = f"hello {name}"
print(my_string)


# In[6]:


list_of_strings = ["my","name", "is","Dhaval"]
list_of_strings = " ".join(list_of_strings)
print(list_of_strings)


# In[1]:


d1 = {"name","age","24","rahul"}
d2 = {"kkr","ragrg","name",}


# In[2]:


import re

df = re.findall("Dhaval","Dhaval is the smart guy is called Dhavaldon")

for i in df:
    print(i)


# In[15]:


import re

randstr = '''
the red flag 
is flying to 
the cheaer's of 
RCB team '''

print(randstr)

regex = re.compile("\n")

randstr = regex.sub(" ",randstr)

print(randstr)




# In[1]:


import random 

def guess(x):
    random_number = random.randint(1,x)
    
    while guess != random_number:
     


# In[ ]:




