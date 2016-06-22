#inplace and not in place
import numpy as np

array1 = np.array([1,2,3,4,5])
sub_array = array1[:3]
print ("sub_array",sub_array)
print ("array1",array1)
sub_array[2] = 40
print ("sub_array",sub_array)
print ("array1",array1)
#notice that array1 also gets modified
#because sub_array refers to the same memory as array1 does. it is not a replicate and slice..
sub_array2 = np.array([])
sub_array2 = array1[:3]
print ("sub_array2",sub_array2)
sub_array2[1] = 60
print ("sub_array",sub_array)
print ("sub_array2",sub_array2)
print ("array1",array1)