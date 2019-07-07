
# coding: utf-8

# In[3]:


import numpy as np
import os
import sys
def find(str,ch):
     for i, ltr in enumerate(str):
        if ltr == ch:
            yield i
file=os.listdir("D:\Dr.Gans\S2")
print (file)
size=len(file)
print (size)
file_index=(file[0])
print(file[0])
r=(file[0]).find('-')
print(r)
result=list(find((file_index),"-"))
print (result)
print(result[0])
file_name=(file_index[1:(result[0])])
start_time=(file_index[(result[0])+2:(result[0])+10])
print (file_name)
print(start_time)
print(size)
print(file_index[0])
print (file_name)
print(start_time)

note="actual code"
print(note)
for x in range(0,(size),1):
    file_index1=(file[x])
    odd_even=list(find((file_index1),"-"))
    #print (odd_even)
    file_index1=(file[x])
    print(file_index1)
    check=(file_index1[(odd_even[3]+1):(odd_even[3]+6)])
    #print(check)
    #type (check)
    check1=int(check)
    #print(check1)
    #if(((check1)%2)==0):
        #end_time=(file_index1[(odd_even[0])+2:(odd_even[0])+10])
        #final="End time: "
        #print (final+ (end_time))
    #else:
            #start_time=(file_index1[(odd_even[0])+2:(odd_even[0])+10])
            #final1="start time: "
            #print(final1+ (start_time))
    if(((check1)%2)!=0):
        start_time=(file_index1[(odd_even[0])+2:(odd_even[0])+10])
        final="Start time: "
        print (final+ (start_time))
    else:
        end_time=(file_index1[(odd_even[0])+2:(odd_even[0])+10])
        final1="end time: "
        print(final1+ (end_time))
            





    



