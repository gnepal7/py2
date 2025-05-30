# SciPy Sparse Data
# Sparse data is data that has mostly unused elements 
# (elements that don't carry any information ).

# Sparse Data: is a data set where most of the item values are zero.
# Dense Array: is the opposite of a sparse array: most of the values are not zero.

# CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
# CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products

# Create a CSR matrix from an array:
# import numpy as np
# from scipy.sparse import csr_matrix
# arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
# print(csr_matrix(arr))


# parse Matrix Methods
# Viewing stored data (not the zero items) with the data property:

# import numpy as np
# from scipy.sparse import csr_matrix
# arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
# print(csr_matrix(arr).data)

# Counting nonzeros with the count_nonzero() method:
# import numpy as np
# from scipy.sparse import csr_matrix
# arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
# print(csr_matrix(arr).count_nonzero())

# Removing zero-entries from the matrix with the eliminate_zeros() method:
# import numpy as np
# from scipy.sparse import csr_matrix
# arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
# mat = csr_matrix(arr)
# mat.eliminate_zeros()
# print(mat) 

# Eliminating duplicate entries with the sum_duplicates() method:
# import numpy as np
# from scipy.sparse import csr_matrix
# arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
# mat = csr_matrix(arr)
# mat.sum_duplicates()
# print(mat)

# Converting from csr to csc with the tocsc() method:
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
newarr = csr_matrix(arr).tocsc()
print(newarr)