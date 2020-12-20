import numpy as np 

my_list=[1,2,3]
my_matrix=[my_list,my_list]

#create numpy array
arr=np.array(my_list)
print(arr)

arr_matrix=np.array(my_matrix)

np.zeros((3,3))
print(np.ones((3,3)))



#Return evenly spaced numbers over a specified interval.
np.linspace(0,10,3)


print(np.eye(4)) #creates identity matrix


np.random.rand(5,5)

arr_matrix.reshape(3,2)

arr.max() #maxvalue
arr.argmax() #index

arr.min()
arr.argmin()

arr.shape

slice_of_arr=arr[0:3]

slice_of_arr=50

#Data is not copied, it's a view of the original array! This avoids memory problems!

arr_copy=arr.copy()


#row,col
arr_matrix[1][2]


slicemat=arr_matrix[:2,1:]

#conditional selection
bool_arr=arr>4 #gives array of true and false

print(bool_arr)


arr[bool_arr]
arr[arr>4]

arr+arr
arr*arr

## Warning on division by zero, but not an error!
# Just replaced with nan
arr/arr

# Also warning, but not an error instead infinity
1/arr

arr**3 #potenz

#alot of functions
np.sqrt(arr)