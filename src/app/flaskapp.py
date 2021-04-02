from flask import Flask, request
import pickle
from numpy import array2string
from flasgger import Swagger
import numpy as np

# define the path to the pickled model
model_path = "../models/irisdatamodel.pkl"

# unpickle the random forest model
with open(model_path, "rb") as file:
    model = pickle.load(file)

# define the app
app = Flask(__name__)
swagger = Swagger(app)


# use decorator to define the /score input method and define the predict function
@app.route("/score", methods=["POST", "GET"])
def predict_species():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    responses:
      200:
        description: Index of predicted class 
    """
    s_length = float(request.args.get("s_length"))
    s_width = float(request.args.get("s_width"))
    p_length = float(request.args.get("p_length"))
    p_width = float(request.args.get("p_width"))
    
    print("Predicting!")

    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    print("Returning Prediction")
    return str(prediction)

# run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5001")