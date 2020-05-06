#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Project:- Strong password generator, generate 3 passwords
import string
from random import *

for x in range(0,3):
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(8, 16)))
    print("Your Recommend Password is:- ", end="")
    print(password)

