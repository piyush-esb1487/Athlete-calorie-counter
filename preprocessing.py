# importing libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# dataset

import data_overview as d_ov
df = d_ov.df.copy()
print("Dataset loaded successfully!")
print("Initial dataset shape:", df.shape)
print("Available columns:")
print(df.columns.tolist())
print("First five rows:")
print(df.head())
print("Dataset information:")
df.info()
print("Missing values:")
print(df.isnull().sum())

# Targets and features

target_column = "Calories"

feature_columns = [
    "Gender",
    "Age",
    "Height",
    "Weight",
    "Duration",
    "Heart_Rate",
    "Body_Temp"
]

# Check required columns exist
missing_columns = [
    col for col in [target_column] + feature_columns
    if col not in df.columns
]
if missing_columns:
    raise ValueError(
        "These required columns are missing: "
        + str(missing_columns)
    )
print("Target column:", target_column)
print("Input features:", feature_columns)

#Clean duplicate rows

df = df.drop_duplicates().copy()
print("Shape after removing duplicates:")
print(df.shape)

model_df = df[feature_columns + [target_column]].copy()

# Convert target values into numeric
model_df[target_column] = pd.to_numeric(
    model_df[target_column],
    errors="coerce"
)

model_df = model_df.dropna(subset=[target_column])
X = model_df[feature_columns]
y = model_df[target_column]

print("Input shape:", X.shape)
print("Target shape:", y.shape)

# Identify numerical and categorical columns
numeric_features = X.select_dtypes(
    include=np.number
).columns.tolist()

categorical_features = X.select_dtypes(
    exclude=np.number
).columns.tolist()

print("Numeric features:", numeric_features)
print("Categorical features:", categorical_features)
# Fill missing numerical values using the median
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])
# Fill missing values using the most frequent value and convert into numbers

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("numeric", numeric_transformer, numeric_features),
    ("categorical", categorical_transformer, categorical_features)
])

print("Preprocessing steps created successfully!")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training examples:", len(X_train))
print("Testing examples:", len(X_test))

#final results Disply

print("========== FINAL DATASET DETAILS ==========")
print("Total rows available:", len(model_df))
print("Training features shape:", X_train.shape)
print("Testing features shape:", X_test.shape)
print("Training target shape:", y_train.shape)
print("Testing target shape:", y_test.shape)
print("Preprocessing and data splitting completed!")

#Function to share data with model.py

def preprocess_data():
    return X_train, X_test, y_train, y_test, preprocessor

if __name__ == "__main__":
    X_train, X_test, y_train, y_test, preprocessor = preprocess_data()