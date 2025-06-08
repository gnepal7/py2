# Hierarchical Clustering
# Hierarchical clustering is an unsupervised learning method for clustering data 
# points. The algorithm builds clusters by measuring the dissimilarities between data

# Start by visualizing some data points:
# import numpy as np
# import matplotlib.pyplot as plt
# x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# plt.scatter(x, y)
# plt.show()

# Now we compute the ward linkage using euclidean distance, and visualize it 
# using a dendrogram:

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.cluster.hierarchy import dendrogram, linkage
# x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# data = list(zip(x, y))
# linkage_data = linkage(data, method='ward', metric='euclidean')
# dendrogram(linkage_data)
# plt.show()


# Here, we do the same thing with Python's scikit-learn library. 
# Then, visualize on a 2-dimensional plot:

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
data = list(zip(x, y))
# Use only the linkage argument if your version of sklearn requires it
hierarchical_cluster = AgglomerativeClustering(n_clusters=2, linkage='ward')
labels = hierarchical_cluster.fit_predict(data)
plt.scatter(x, y, c=labels)
plt.show()