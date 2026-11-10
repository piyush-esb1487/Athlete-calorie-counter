
# Importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os



from pathlib import Path
from preprocessing import preprocess_data

output_dir = Path(__file__).resolve().parent / "Graphs"
output_dir.mkdir(exist_ok=True)


# Loading trained model

model_path = Path(__file__).with_name("trained_model.pkl")

if not model_path.exists():
    print("Trained model not found! Run model.py first.")
    exit()

model = joblib.load(model_path)


# Getting test data

X_train, X_test, y_train, y_test, preprocessor = preprocess_data()


# Making predictions

y_pred = model.predict(X_test)


# Calculating residuals

residuals = y_test - y_pred


# Loading dataset

df = pd.read_csv("calories.csv")


# Graph 1: Actual vs Predicted Calories


plt.figure(figsize=(8, 5))

plt.scatter(y_test, y_pred, alpha=0.5)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)

plt.xlabel("Actual Calories")
plt.ylabel("Predicted Calories")
plt.title("Actual vs Predicted Calories")

plt.savefig(output_dir / "Actual vs Predicted Calories" )

plt.tight_layout()
plt.show()



# Graph 2: Residual Plot

plt.figure(figsize=(8, 5))

plt.scatter(y_pred, residuals, alpha=0.5)

plt.axhline(y=0, linestyle="--")

plt.xlabel("Predicted Calories")
plt.ylabel("Residuals")
plt.title("Residual Plot")

plt.savefig(output_dir / "Residual Plot" )

plt.tight_layout()
plt.show()


# Graph 3: Calories Distribution

plt.figure(figsize=(8, 5))

sns.histplot(df["Calories"], kde=True)

plt.xlabel("Calories Burned")
plt.ylabel("Frequency")
plt.title("Distribution of Calories")
plt.savefig(output_dir / "Calories Distribution" )

plt.tight_layout()
plt.show()


# Graph 4: Correlation Heatmap

plt.figure(figsize=(9, 6))

numeric_df = df.select_dtypes(include=np.number)

correlation = numeric_df.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Feature Correlation Heatmap")
plt.savefig(output_dir / "Correlation Heatmap" )

plt.tight_layout()
plt.show()


print("All visualizations completed successfully!")
