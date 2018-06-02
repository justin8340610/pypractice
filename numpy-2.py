import numpy as np
import matplotlib.pyplot as plt
arr = np.arange(10)
print(arr)
print(arr.ndim)
print(arr.shape)

arr2_x = np.arange(5,100,1)
arr2_y = arr2_x **2 + 1
#print(arr2)
#print(arr2_1)

arr3_x = np.range(10, 50, 3)
arr3_y = arr3_x * 2 + 5 

arr4_x = np.linspace(0, 10, 21)
arr4_y1 = arr_x +2 
arr4_y2 = arr_x +3

plt.plot(arr4_x, arr4_y1, arr4_x,'rv', arr4_y2, '--bo')
plt.show()

