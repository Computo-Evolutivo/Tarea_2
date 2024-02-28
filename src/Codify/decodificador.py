#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import sys
# x representa el número que se va a decodificar, puede ser en el siguiente formato:
# 10
# [10]
# [1,0]
#nBits es el número de bits 
#vmin es a, extremo inferior del intervalo
#vmax es b, extremo superior del intervalo

def decodificador(x, nBits, vmin, vmax):
    try:
        x=(int(x))
    except:
           Xnp = np.array(x)
           x= ''.join(map(str, Xnp))      
    finally:
        if len(str(x))>nBits:
            print("El número introducido y el número de bits no concuerda")
        #Si se introducen menos bits que el número de bits seleccionado, 
        #se asume que los bits restantes son 0s a la izquierda
        else:
            return vmin + (int(f"{x}", base=2)) * ((vmax-vmin)/(2**nBits-1))


# In[5]:


if __name__ == 'decodificador':
    val = codificador(float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]) )
    print(val)


# In[ ]:




