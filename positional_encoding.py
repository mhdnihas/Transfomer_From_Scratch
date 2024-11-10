import numpy as np
import math

def positional_encoding(pos,d_model=512):
    pe=np.zeros((1,d_model))

    for i in range(0,d_model,2):
        pe[0][i]=math.sin(pos/10000**(2*i/d_model))
        pe[0][i+1]=math.cos(pos/10000**(2*i/d_model))

    print(pe)
    return pe

positional_encoding(1)