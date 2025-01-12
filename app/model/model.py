import pickle

def load_model():
    model = pickle.load(open('model.pkl', 'rb'))
    return model

def prediction_model(data):
    model = load_model()
    if data[1].lower() == 'male':
        data[1] = 0
    else:
        data[1] = 1

    if data[3].lower() == 's' :
        data[3] = 0
    elif data[3].lower() == 'c':
        data[3] = 1
    else:
        data[3] = 2
    result = model.predict([data])  
    return result[0]
  










