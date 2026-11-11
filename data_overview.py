import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("calories.csv", nrows=500)
age_avg = df["Age"].mean()
height_avg = df["Height"].mean()
weight_avg = df["Weight"].mean()
duration_avg = df["Duration"].mean()

# This function is to print basic stuff as and when required
def basic_info():
    print(df.head())
    print("Dataset dimensions:", df.shape)
    print("\nColumn names:")
    print(df.columns.tolist())

    print(df.info())
    print(df.describe())


def filter_data(data_f: pd.DataFrame, key, initial_val, tol=0):
    tol = initial_val * 0.1
    data_f = data_f[data_f[key].between(initial_val - tol, initial_val + tol)]
    return data_f

# This function gives 2 dataframes seperately for male and female where duration, weight, height and age are specified by the end user
def seperating_data(approx_duration=None, approx_weight=None, approx_height=None, approx_age=None):
    filtered = df.copy()
    if approx_duration is not None:
        filtered = filter_data(filtered, "Duration", approx_duration)
    if approx_weight is not None:
        filtered = filter_data(filtered, "Weight", approx_weight)

    if approx_height is not None:
        filtered = filter_data(filtered, "Height", approx_height)

    if approx_age is not None:
        filtered = filter_data(filtered, "Age", approx_age)

    male_data = filtered[filtered["Gender"] == "male"]
    female_data = filtered[filtered["Gender"] == "female"]
    return male_data, female_data
        

# Trying to imagine the data on a Bargraph


def plot_bar(approx_duration=None, approx_weight=None, approx_height=None, approx_age=None, column_to_compare="Duration", axes_to_use=None):
    male_data, female_data = seperating_data(approx_duration, approx_weight, approx_height, approx_age)

    # Male Bar Plot (Top-Left)
    sns.barplot(
        data=male_data,
        x=column_to_compare,
        y="Calories",
        errorbar=None,
        ax=axes_to_use[0],
    )
    axes_to_use[0].set_title(f"Male - Calories vs {column_to_compare}")
    axes_to_use[0].set_xlabel(column_to_compare)
    axes_to_use[0].set_ylabel("Calories")
    axes_to_use[0].tick_params(axis="x", rotation=45)

    # Female Bar Plot (Top-Right)
    sns.barplot(
        data=female_data,
        x=column_to_compare,
        y="Calories",
        errorbar=None,
        ax=axes_to_use[1],
    )
    axes_to_use[1].set_title(f"Female - Calories vs {column_to_compare}")
    axes_to_use[1].set_xlabel(column_to_compare)
    axes_to_use[1].set_ylabel("Calories")
    axes_to_use[1].tick_params(axis="x", rotation=45)


def plot_scatter(approx_duration=None, approx_weight=None, approx_height=None, approx_age=None, column_to_compare="Duration", axes_to_use=None):
    male_data, female_data = seperating_data(approx_duration, approx_weight, approx_height, approx_age)

    # Male Scatter Plot (Bottom-Left)
    sns.scatterplot(
        data=male_data,
        x=column_to_compare,
        y="Calories",
        alpha=0.6,
        ax=axes_to_use[0],
    )
    axes_to_use[0].set_title(f"Male - Calories vs {column_to_compare}")
    axes_to_use[0].set_xlabel(column_to_compare)
    axes_to_use[0].set_ylabel("Calories")
    axes_to_use[0].tick_params(axis="x", rotation=45)

    # Female Scatter Plot (Bottom-Right)
    sns.scatterplot(
        data=female_data,
        x=column_to_compare,
        y="Calories",
        alpha=0.6,
        ax=axes_to_use[1],
    )
    axes_to_use[1].set_title(f"Female - Calories vs {column_to_compare}")
    axes_to_use[1].set_xlabel(column_to_compare)
    axes_to_use[1].set_ylabel("Calories")
    axes_to_use[1].tick_params(axis="x", rotation=45)


def set_input(msg: str):
    take_input = input(msg).strip()
    return float(take_input) if take_input and take_input != "0" else None


if __name__ == "__main__":

    # --- This part is for taking all the required inputs
    age = set_input("Enter age(Put 0 to view data for all ages): ")
    height = set_input("Enter Height in cm(Put 0 to view data for all Heights): ")
    weight = set_input("Enter Weight in kg(Put 0 to view data for all Weights): ")
    duration = set_input("Enter Duration in seconds(Put 0 to view data for all Durations): ")
    default_column_compare = input("Enter default column to compare (Age, Height, Weight, Duration): ").title()
    # ----------

    # 1. Create 1 single window with 2 rows and 2 columns
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

    # TO show what parameters have been given as fixed inputs
    params = ""
        
    for k, v in [("Age", age), ("Height in cm", height), ("Weight in kg", weight), ("Duration in s", duration)]:
        if v is not None:
            params += f"{k} ~ {v} "

    fig.suptitle(params)
    plot_bar(duration,weight,height,age,column_to_compare=default_column_compare,axes_to_use=axes[0])
    plot_scatter(duration,weight,height,age,column_to_compare=default_column_compare,axes_to_use=axes[1])

    plt.tight_layout()
    plt.show()
