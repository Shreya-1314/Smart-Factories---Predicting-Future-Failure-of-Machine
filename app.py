
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

        # data = request.get_json()
        # prediction = np.array2string(model.predict(data))
        # return jsonify(prediction)
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        output = prediction[0]
        return render_template('index.html', prediction_text='Machine Failure: {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)




if __name__ == "__main__":
    app.run(debug=True)