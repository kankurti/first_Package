#By using the numpy package
import numpy as np
def creat_array(l1):
    arr = np.array(l1)
    print(arr)
    print(type(arr))


#By using the pandas package
import pandas as pd
def Make_series(d,i):
    Data =d
    #s = pd.Series(Data)
    Index =i
    si = pd.Series(Data, Index)
    print(si)
