#!/usr/bin/env python
# coding: utf-8

# Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.

# In[17]:


def stutter(word):
    stuttered = word[:2] + "...."
    return stuttered + stuttered + word + "?"


# In[15]:


stutter("incredible")


# In[16]:


stutter("enthusiastic")


# In[18]:


stutter("outstanding") 


# 2..Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.

# In[33]:


import math
def radians_to_degrees(angle_in_radian):
    angle_in_degrees= angle_in_radian  *  (180 / math.pi)
    return round(angle_in_degrees, 1)


# In[36]:


radians_to_degrees(57.3)


# In[37]:


radians_to_degrees(1145.9)


# In[38]:


radians_to_degrees(2864.8)


# 3.In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
# Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.

# In[5]:


import math
def is_curzon_number(num):
    numerator = 2**num + 1
    denominator = 2**num + 1
    return numerator % denominator == 0


# In[6]:


is_curzon_number(5)


# In[43]:


is_curzon_number(10)


# In[44]:


is_curzon_number(14)


# 4..Given the side length x find the area of a hexagon

# In[7]:


import math
def area_of_hexagon(x):
    area = (3 * math.sqrt(3) * x**2) / 2
    return area


# In[8]:


area_of_hexagon(2.6)


# In[9]:


area_of_hexagon(10.4)


# In[10]:


area_of_hexagon(23.4)


# 5.
# Question 5. Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
# Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
# 

# In[11]:


def decimal_to_binary(decimal_str):
    return bin(int(decimal_str))[2:]


# In[12]:


decimal_to_binary("1")


# In[13]:


decimal_to_binary("101")


# In[14]:


decimal_to_binary("1010")


# In[ ]:




