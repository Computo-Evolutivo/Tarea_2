#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import sys
import codificador 

def codificador_vectores (nBits, vmin, vmax, x):
    lista=[]
    for i in range(len(x)):
        lista.append(codificador.codificador(int(x[i]), nBits, vmin, vmax))
    return lista


# In[8]:


if __name__ == '__main__':
    val = codificador_vectores(int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), (sys.argv[4:]) )
    print(val)


# In[ ]:




