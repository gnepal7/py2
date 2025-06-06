# Read JSON
# Big data sets are often stored, or extracted as JSON

# Load the JSON file into a DataFrame:
# import pandas as pd
# df = pd.read_json("weather.json") 
# pd.options.display.max_rows = 10
# df = pd.read_json("weather.json")
# print(df.to_string()) # Tip: use to_string() to print the entire DataFrame
# print(df)

# Dictionary as JSON
# Load a Python Dictionary into a DataFrame:
import pandas as pd
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.DataFrame(data)
print(df) 