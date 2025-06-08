# A Decision Tree is a Flow Chart, and can help you make decisions 
# based on previous experience.

# import pandas
# df = pandas.read_csv("uk-data.csv")
# print(df) 

# Create and display a Decision Tree:
# import pandas
# from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt

# df = pandas.read_csv("uk-data.csv")
# d = {'UK': 0, 'USA': 1, 'N': 2}
# df['Nationality'] = df['Nationality'].map(d)
# d = {'YES': 1, 'NO': 0}
# df['Go'] = df['Go'].map(d)

# features = ['Age', 'Experience', 'Rank', 'Nationality']
# X = df[features]
# y = df['Go']

# dtree = DecisionTreeClassifier()
# dtree = dtree.fit(X, y)
# tree.plot_tree(dtree, feature_names=features) 

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.tree import DecisionTreeRegressor, plot_tree
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error

# # STEP 1: Load the CSV file
# df = pd.read_csv("data.csv")  # Make sure this path is correct!

# # STEP 2: Select features and target
# X = df[["Volume", "Weight"]]
# y = df["CO2"]

# # STEP 3: Split into train/test
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # STEP 4: Create & train the model
# model = DecisionTreeRegressor()
# model.fit(X_train, y_train)

# # STEP 5: Predict and evaluate
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# print(f"Mean Squared Error: {mse:.2f}")

# # STEP 6: Visualize the tree
# plt.figure(figsize=(12, 6))
# plot_tree(model, feature_names=["Volume", "Weight"], filled=True, rounded=True)
# plt.title("Decision Tree for Predicting CO2 Emissions")
# plt.show()




import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Step 1: Define the data
data = {
    "Age": [36, 42, 23, 52, 43, 44, 66, 35, 52, 35, 24, 18, 45],
    "Experience": [10, 12, 4, 4, 21, 14, 3, 14, 13, 5, 3, 3, 9],
    "Rank": [9, 4, 6, 4, 8, 5, 7, 9, 7, 9, 5, 7, 9],
    "Nationality": ["UK", "USA", "N", "USA", "USA", "UK", "N", "UK", "N", "N", "USA", "UK", "UK"],
    "Go": ["NO", "NO", "NO", "NO", "YES", "NO", "YES", "YES", "YES", "YES", "NO", "YES", "YES"]
}

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Encode categorical variables
df_encoded = pd.get_dummies(df, columns=["Nationality"], drop_first=True)
df_encoded["Go"] = df_encoded["Go"].map({"NO": 0, "YES": 1})  # Encode target

# Step 4: Features & Target
X = df_encoded.drop("Go", axis=1)
y = df_encoded["Go"]

# Step 5: Train Decision Tree
model = DecisionTreeClassifier()
model.fit(X, y)

# Step 6: Visualize the tree
plt.figure(figsize=(14, 7))
plot_tree(model, feature_names=X.columns, class_names=["NO", "YES"], filled=True, rounded=True)
plt.title("Decision Tree to Predict 'Go'")
plt.show()