#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1st lab

num1 = input('please enter 1st no:')
op = input('select operation:')
num2 = input('please enter 2nd no:')



num1 = float(num1)
num2 = float(num2)

if op =='+':
   result = num1+num2
   print(result)
   
elif op == '-':
     result= num1-num2
     print(result)

elif op == '*':
     result= num1*num2
     print(result)
     
elif op == '/':
     result= num1/num2
     print(result)


# In[25]:


for line  in range (2):
    for i in range(0,5):
       print('*' , end=' ')
    print('\n')


# In[37]:


word = 'Mhohamed'
for c in word:
    print(c) 
    if c == 'a':
     break


# In[40]:


word = 'Mhohamed'
for c in word:
    
    if c == 'a':
     continue
    print(c)


# In[41]:


word = 'Mhohamed'
for c in word:
    print(c) 
    if c == 'a':
     continue
    print(c)


# In[74]:


# defin fancation


def printstar(row,clo=5):
  for line in range(row):
     for i in range(0,clo):
        print('*' , end ='')
     print( '\n' ) 
    


# In[61]:


2nd lab

for line in range(3):
     for i in range(0,10):
        print('*' , end ='')
     print( '\n' ) 
    
print('Welcome in Home\n')

for line in range(2):
     for i in range(0,10):
        print('*' , end ='')
     print( '\n' ) 


# In[68]:


printstar(4,9)
print('Welcome in Home\n')
printstar(2,4)


# In[78]:


printstar(row=5, clo=3)
print('Welcome in Home\n')
printstar(2)


# In[84]:


#3rd lab

def max2(num1,num2):
    if num1 > num2:
        return(num1)
    else:
        return(num2)
    
def max3(num1,num2,num3):
    m= max2(num1,num2)
    fin = max2(m,num3)
    return(fin)

num1= input('please enter No1 : ')
num2= input('please enter No2 : ')
num3= input('please enter No3 : ')
rest= max3(num1,num2,num3)
print('max=', rest)


# In[92]:


#4th lab

def unique(unq):
    res=[]
    for n in unq:
        if n not in res :
            res.append(n)
    return(res)
    
numbers =[1,2,2,3,4,4,5,6,9,7]
m = unique(numbers)
print(m)


# In[ ]:


class dog:
    numofdog=0
    def__int__(self):
        dog.numofdog += 1
        

