import numpy as np
import math

array = [25, 1, 25, 50, 100, 1000, 10000]

npArray = np.array(array)
np_logArray = np.log(npArray)
reg_logArray = math.log(array[0])

