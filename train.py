import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def train_model():
    try:
        df = pd.read_csv('customer_data.csv')
    except FileNotFoundError:
        print("Error: customer_data.csv not found.")
        return

    X = df.drop('purchased', axis=1)
    y = df['purchased']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f"Model trained with accuracy: {accuracy}")

    with open('model.pkl', 'wb') as file:
        pickle.dump(model, file)
    print("Model saved successfully as model.pkl")

if __name__ == "__main__":
    train_model()
