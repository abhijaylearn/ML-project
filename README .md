# E-commerce Customer Purchase Prediction

## Overview
This project predicts whether a customer will purchase a high-value product based on their browsing behavior and demographics. 

The prediction is based on three key features:
- **Age**: The customer's age.
- **Time spent on website**: Total duration (in minutes) spent browsing.
- **Added to cart status**: Binary status (1 if added to cart, 0 if not).

## Project Structure
The project has been modularized into the following files for better organization:
- `customer_data.csv`: The dataset containing historical customer behavior.
- `train.py`: The script that loads the dataset, trains the model, and saves it.
- `main.py`: The user-facing script that loads the trained model and makes real-time predictions based on user input.
- `model.pkl`: The serialized trained machine learning model (generated after running `train.py`).

## Technologies Used
- **Python**: Core programming language.
- **Pandas**: For loading and manipulating the CSV dataset.
- **NumPy**: For numerical array processing.
- **Scikit-learn**: For the machine learning model and data splitting.

## Model Used
**Logistic Regression** is used for binary classification to determine the probability of a purchase.

## How to Run

### 1. Install dependencies
First, ensure you have the necessary libraries installed:

    pip install pandas numpy scikit-learn


### 2. Train the Model
You must train the model to generate the `model.pkl` file before making predictions:

    python train.py


### 3. Run Predictions
Execute the main script to enter customer data and receive a prediction:

    python main.py


## Output
Based on the inputs provided, the model predicts:
- **Likely to purchase**
- **Unlikely to purchase**

## Notes
This is a basic demo utilizing a small dataset. In real-world scenarios, using larger and more diverse datasets will significantly improve the model's accuracy and reliability.