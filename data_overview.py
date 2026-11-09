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
def plot_bar(approx_duration=None, approx_weight=None, approx_height=None, approx_age=None, column_to_compare="Duration"):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))
    male_data, female_data = seperating_data(approx_duration, approx_weight, approx_height, approx_age)
    column_to_compare = "Duration"
    sns.barplot(
        data=male_data, 
        x=column_to_compare, 
        y="Calories",
        errorbar=None,
        ax=axes[0]
        )

    axes[0].set_title(f"Male - Calories vs {column_to_compare}")
    axes[0].set_xlabel(column_to_compare)
    axes[0].set_ylabel("Calories")

    axes[0].tick_params(axis="x", rotation=45)


    sns.barplot(
        data=female_data, 
        x=column_to_compare, 
        y="Calories",
        errorbar=None,
        ax=axes[1]
        )

    axes[1].tick_params(axis="x", rotation=45)

    axes[1].set_title(f"Female - Calories vs {column_to_compare}")
    axes[1].set_xlabel(column_to_compare)
    axes[1].set_ylabel("Calories")
    plt.show()


# Trying to imagine data on a scatterplot
def plot_scatter(approx_duration=None, approx_weight=None, approx_height=None, approx_age=None, column_to_compare="Duration"):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 10))
    male_data, female_data = seperating_data(
        approx_duration, approx_weight, approx_height, approx_age
    )

    # Male Scatter Plot
    sns.scatterplot(
        data=male_data,
        x=column_to_compare,
        y="Calories",
        alpha=0.6,
        ax=axes[0],
    )
    axes[0].set_title(f"Male - Calories vs {column_to_compare}")
    axes[0].set_xlabel(column_to_compare)
    axes[0].set_ylabel("Calories")

    axes[0].tick_params(axis="x", rotation=45)

    # Female Scatter Plot
    sns.scatterplot(
        data=female_data,
        x=column_to_compare,
        y="Calories",
        alpha=0.6,
        ax=axes[1],
    )
    
    axes[1].tick_params(axis="x", rotation=45)

    axes[1].set_title(f"Female - Calories vs {column_to_compare}")
    axes[1].set_xlabel(column_to_compare)
    axes[1].set_ylabel("Calories")

    plt.show()



if __name__ == "__main__":
    print(df.head())
    plot_bar(approx_age=20, approx_height=180)

