#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import sys
import decodificador 

def decodificador_vectores (nBits, vmin, vmax, x):
    lista=[]
    for i in range(len(x)):
        lista.append(decodificador.decodificador(int(x[i]), nBits, vmin, vmax))
    return lista


# In[ ]:


if __name__ == '__main__':
    val = decodificador_vectores(int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), (sys.argv[4:]) )
    print(val)


# In[ ]:




