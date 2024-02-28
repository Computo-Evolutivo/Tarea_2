#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import sys
def codificador(x, nBits, vmin, vmax):
    if x>vmax:
        print("el número a códificar no puede ser mayor al máximo")
    else:
        precision= ( vmax - vmin) / (2**nBits-1)
        index= int( (x - vmin) / precision)
        binario = [int(bit) for bit in format(index, f"0{nBits}b")]
        return binario


# In[16]:


if __name__ == '__main__':
    val = codificador(float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]) )
    print(val)


# In[ ]:




