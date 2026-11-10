# Athlete-calorie-counter

### Project Overview
This AI project uses some basic parameters of body build and exercise and diet routine to predict how much calorie an athlete would burn during their workout session. It uses linear regression to predict calorie expense based on different physical and exercise related parameters.

### Languages and library used
- Python
- Pandas
- Numpy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Pathlib

### Dataset
> This project uses initial 500 rows of calories.csv, the link for the same is

https://www.kaggle.com/datasets/ruchikakumbhar/calories-burnt-prediction

Parameters provided in the data are:
- Gender
- Age
- Height
- Weight
- Exercise Duration
- Heart Rate
- Body Temperature

Target value is:
Calories

### Machine learning algorithm and workflow
This project uses linear regression to train the model and predict the calories burnt on various parameters.

1. Load the dataset.
2. Explore and understand the data.
3. Handle missing values and duplicate records.
4. Encode categorical features.
5. Split the dataset into training and testing sets.
6. Train the Linear Regression model.
7. Evaluate model performance.
8. Save the trained model using Joblib.
9. Predict calories for new user inputs.
10. Visualize model performance and dataset patterns.

### Installation
Install the required libraries put in requirements.txt by running this in terminal:

`python3 -m pip install -r requirements.txt`

### How to Run
To explore the dataset:

`python3 data_overview.py`

First, train the model:

`python3 model.py`

Then run the prediction interface:

`python3 main.py`

To generate visualizations (only after predictions):

`python3 visualization.py`


### Model Evaluation
The model is evaluated using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Output
The project predicts the estimated calories burned based on the user's exercise information and displays visualizations to understand the dataset and model performance.


### Contributions of members:
1. _Piyush Tiwari_:

   Documentation Lead, created the readme file and handled exploration of dataset before preprocessing in the file data_overview.py
2. _Jagdeesh Sunnam_:

   Video Lead, Creating a video,  handled the preprocessing part in the file preprocessing.py
3. _Devansh_:

   Execution Lead, made sure that the file is working properly and gave instructions for this and handled the creation of model in model.py
4. _Avinash_:

   PPT Lead, created presentation of the project and handled the visualization of data post prediction in visualization.py

### Disclosing Uses of AI:
 