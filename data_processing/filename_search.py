
# coding: utf-8

# In[2]:


import os
result=[]
def search(path=".", name=""):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            search(item_path, name)
        elif os.path.isfile(item_path):
            if name in item:
                global result
                result.append(item_path + ";")
                print (item_path + ";"+"\n", end="")

search(path=r"C:\Users\张寅\Desktop\文件\4.30", name="1025")


# In[ ]:




