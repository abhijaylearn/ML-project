import numpy as np
import pickle

def run_prediction():
    try:
        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)
    except FileNotFoundError:
        print("Error: model.pkl not found. Run train.py first.")
        return

    print("--- Real-time Customer Prediction ---")
    age = float(input('Enter Customer Age: '))
    time = float(input('Enter Time spent on website: '))
    cart = int(input('Enter 1 if added to Cart, else 0: '))

    user_input = np.array([[age, time, cart]])
    
    prediction = model.predict(user_input)
    
    result = "LIKELY to purchase" if prediction[0] == 1 else "UNLIKELY to purchase"
    print(f"\nPrediction: {result}")

if __name__ == "__main__":
    run_prediction()
