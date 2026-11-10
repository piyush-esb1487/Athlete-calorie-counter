
# Importing libraries

import numpy as np
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from preprocessing import preprocess_data


# Getting preprocessed data

X_train, X_test, y_train, y_test, preprocessor = preprocess_data()

print("\nData received successfully!")


# Creating Linear Regression model

model = LinearRegression()


# Creating complete pipeline

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", model)
])


# Training the model

print("\nTraining started...")

pipeline.fit(X_train, y_train)

print("Model training completed!")


# Making predictions

y_pred = pipeline.predict(X_test)


# Evaluating the model

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)


# Displaying results

print("\n========== MODEL PERFORMANCE ==========")

print("Mean Absolute Error (MAE):", round(mae, 2))

print("Mean Squared Error (MSE):", round(mse, 2))

print("Root Mean Squared Error (RMSE):", round(rmse, 2))

print("R2 Score:", round(r2, 4))

print("R2 Score (%):", round(r2 * 100, 2), "%")


# Actual vs Predicted values

print("\n========== ACTUAL VS PREDICTED ==========")

for actual, predicted in zip(y_test.head(10), y_pred[:10]):

    print(
        "Actual:", round(actual, 2),
        "| Predicted:", round(predicted, 2)
    )


# Saving the trained model

joblib.dump(pipeline, "trained_model.pkl")

print("\nTrained model saved successfully!")

print("\nModel execution completed!")
