#!/usr/bin/env python
# coding: utf-8

# In[63]:


#1. Write a Python program to find sum of elements in list?
l=[1,2,3,4,5,6]
sum=0
for i in l:
    sum=sum+i
print("sum  of elements in l :",sum)


# In[62]:


#2. Write a Python program to Multiply all numbers in the list?
l=[1,2,3,4,5,6]
count=1
for i in l:
    count=count*i
print("product of elements in l :",count)


# In[59]:


#3. Write a Python program to find smallest number in a list?
l1=[23,67,19,789,3,78,55]
for i in l1:
    a=min(l1)
print("smallest number in list l1 is:",a)


# In[58]:


#4. Write a Python program to find largest number in a list?
l1=[23,67,19,789,3,78,55]
for i in l1:
    b=max(l1)
print("largest number in list l1 is:",b)


# In[40]:


#5. Write a Python program to find second largest number in a list?
l1=[23,67,19,789,3,78,55]
for i in l1:
    a=sorted(l1)
print("second largest number is",a[-2])


# In[65]:


#6. Write a Python program to find N largest elements from a list?

myList = [120, 50, 89, 170, 45, 250, 450, 340]

print("List = ",myList)
n = 4
myList.sort()
print("Largest integers from the List = ",myList[-n:])


# In[46]:


#7. Write a Python program to print even numbers in a list?
l2=[3,2,5,7,8,90,44,32,77,95,349,29]
for i in l2:
    if i%2==0:
        print(i)


# In[47]:


#8. Write a Python program to print odd numbers in a List?
l2=[3,2,5,7,8,90,44,32,77,95,349,29]
for i in l2:
    if i%2!=0:
        print(i)


# In[50]:


#9. Write a Python program to Remove empty List from List?
l=[1,33,"hello",87.55,564,[     ],[1,2,34,44]]
for i in l:
    if type(i)==list:
        l.remove([])
        print(l)


# In[53]:


#10. Write a Python program to Cloning or Copying a list?
l=[1,2,33,444,78,49,44,"python","code",67.4]
l3=l.copy()
print(l3)


# In[57]:


#11. Write a Python program to Count occurrences of an element in a list?
l4=["name",34,88,962,"age",14,34,77,88,34,988,77]
print("count of 34 is:", l4.count(34))


# In[ ]:




