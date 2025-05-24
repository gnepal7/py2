# Access Array Elements

# Get the first element from the following array
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr[0]) 
# Get the second element from the following array
# print(arr[1])
# Get third and fourth elements from the following array and add them
# print(arr[2] + arr[3])

# Access 2-D Arrays
# import numpy as np
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st row: ', arr[0, 1]) 

# Access the element on the 2nd row, 5th column
# import numpy as np
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('5th element on 2nd row: ', arr[0, 4]) 

# Access 3-D Arrays
# Access the third element of the second array of the first array
# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[1, 1, 1]) 

# Negative Indexing
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -2]) 

