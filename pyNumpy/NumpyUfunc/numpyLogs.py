# Find log at base 2 of all elements of following array:
# import numpy as np
# arr = np.arange(1, 10)
# print(np.log2(arr)) 

# Find log at base 10 of all elements of following array:
# import numpy as np
# arr = np.arange(1, 10)
# print(np.log10(arr)) 

# Find log at base e of all elements of following array:
# import numpy as np
# arr = np.arange(1, 10)
# print(np.log(arr)) 

# Log at Any Base
# from math import log
# import numpy as np
# nplog = np.frompyfunc(log, 2, 1)
# print(nplog(100, 15)) 

from math import log
import numpy as np
nplog = np.frompyfunc(log, 2, 1)
print(nplog(50, 10))