# import numpy as np
# x=0
# set1=np.array(0)
# set2=np.array(0)
# for i in range(0,10):
#   x=x+1
#   y=16/x
#   c=x+y
#   set1=np.append(set1, x)
#   set2=np.append(set2, c)

# import matplotlib.pyplot as plt
# plt.plot(set1, set2)

import random
set1 = []
set2 = []
no = 0
for i in range(-50,50+1):
  set1.append(i)
  set2.append(i*i*i)

import numpy as np

numbers = np.array(set1)
squares = np.array(set2)

import matplotlib.pyplot as plt
plt.plot(numbers, squares)
plt.bar(numbers, squares)