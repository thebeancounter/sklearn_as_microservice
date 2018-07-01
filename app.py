from flask import Flask

app = Flask(__name__)

modelPath = "model.pkl"

def create_random_training_data():
    import numpy as np
    data = np.random.rand(1000, 10)
    tags = np.random.randint(0, 2, 1000)
    return data, tags

def load_model_or_use_model():
    import pickle
    global model
    with open(modelPath, "rb") as f:
        model = pickle.load(modelPath)

def train_model():
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    t = RandomForestClassifier()
    data, tags = create_random_training_data()
    t.fit(data, tags)
    return t

def save_model():
    import pickle
    with open(modelPath, "wb") as f:
        pickle.dump(model, f)


@app.route('/')
def hello_world():
    print("what")
    return 'Hello World!'


@app.route('/train')
def train():
    global model
    from flask import jsonify
    model = train_model()
    data, tags = create_random_training_data()
    return jsonify({"prediction": model.predict_proba(data).tolist()})
    return "trained"


@app.route('/checkmodel')
def check():
    from flask import jsonify
    return jsonify(model.__str__())


@app.route('/predict', methods = ['POST'])
def predict_using_model():
    import json
    from flask import request
    from flask import jsonify

    if not model:
        print(model)
        return "no model"

    try:
        data = request.data
        data_dict = json.loads(data)
        return model.predict_proba(data_dict["input"])

    except Exception as inst:
        return "error predicting"


model = None
print(model)

if __name__ == '__main__':
    print("starting app")
    app.run(port=5002, host="0.0.0.0", debug=True)

