from flask import Flask

app = Flask(__name__)

modelPath = "model.pkl"

def load_model_or_use_model():
    import pickle
    global model
    with open(modelPath, "rb") as f:
        model = pickle.load(modelPath)

def train_model():
    from sklearn.tree import DecisionTreeClassifier
    t = DecisionTreeClassifier()
    return t

def save_model():
    import pickle
    with open(modelPath, "wb") as f:
        pickle.dump(model, f)


@app.route('/')
def hello_world():
    print("what")
    return 'Hello World!'

print(2)
model = None
model = train_model()
#save_model()
print(model)

if __name__ == '__main__':
    print("starting app")
    app.run(port = 5002)

