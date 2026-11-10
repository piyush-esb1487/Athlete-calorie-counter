
# Importing libraries

import pandas as pd
import joblib
from pathlib import Path


# Loading trained model

model_path = Path(__file__).with_name("trained_model.pkl")

if not model_path.exists():
    print("Trained model not found!")
    print("Please run model.py first.")
    exit()

model = joblib.load(model_path)

print("\n================================")
print("   ATHLETE CALORIE PREDICTION")
print("================================")


# Taking input from user

gender = input("Enter Gender (Male/Female): ")

age = float(input("Enter Age: "))

height = float(input("Enter Height (cm): "))

weight = float(input("Enter Weight (kg): "))

duration = float(input("Enter Exercise Duration (minutes): "))

heart_rate = float(input("Enter Heart Rate: "))

body_temp = float(input("Enter Body Temperature: "))


# Creating input dataframe

user_data = pd.DataFrame({
    "Gender": [gender],
    "Age": [age],
    "Height": [height],
    "Weight": [weight],
    "Duration": [duration],
    "Heart_Rate": [heart_rate],
    "Body_Temp": [body_temp]
})


# Making prediction

predicted_calories = model.predict(user_data)


# Displaying result

print("\n========== PREDICTION RESULT ==========")

print("Predicted Calories Burned:",
      round(abs(predicted_calories[0]), 2))

print("=======================================")


