# Athlete-calorie-counter

### Project Overview
This AI project uses some basic parameters of body build and exercise and diet routine to predict how much calorie an athlete would burn during their workout session. It uses linear regression to predict calorie expense based on different physical and exercise related parameters.

### Members:
| Name | Entry No. | Role |
| ---- | --------- | ---- |
| _Piyush Tiwari_ | 2026ESB1487 | Documentation Lead |
| _Devansh Singh Vardhan_ | 2026EEB1342 | Execution Lead |
| _Avinash_ | 2026AIB1025 | PPT Lead |
| _Sunnam Jagadeesh_ | 2026MCB1575 | Video Lead |

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
<img width="818" height="545" alt="image" src="https://github.com/user-attachments/assets/3c9f6cd5-c407-47b8-ba2a-2f10debfc41e" />

### Link to PPT and Video

### Disclosing Uses of AI:
 
