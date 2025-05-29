# Pandas is a Python library.
# Pandas is used to analyze data.
# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.
# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" 
# and was created by Wes McKinney in 2008.


# Load a CSV file into a Pandas DataFrame:
# import pandas as pd
# df = pd.read_csv('DatasetTasks.csv')
# print(df.to_string()) 

# import pandas
# import pandas
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myvar = pandas.DataFrame(mydataset)
# print(myvar) 

# import pandas as pd
import pandas as pd
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
print(pd.__version__) 