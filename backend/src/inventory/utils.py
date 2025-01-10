import pickle
import numpy as np

category = {'F&V': 1, 'Dairy': 2}
products = {"Milk":1, "Bread":2, "Eggs":3, "Apple":4, "Tomato":5, "Cucumber":6, "Chilli":7, "Cheese":8}

def predict(data: list, model_loc: str = 'src\ml_model\PolyStock1.pkl'):
    with open(model_loc, 'rb') as file:
        model = pickle.load(file)
        # data = [month, name, category, day, holiday]
        
        data[1] = products.get(data[1])
        data[2] = category.get(data[2])
        data[4] = 1 if data[3] > 5 else 0

        data = np.array(data)
        data = data.reshape(-1, 5)
        
        prediction = model.predict(data)
        prediction = list(prediction)
        return prediction