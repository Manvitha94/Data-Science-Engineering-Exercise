from flask import Flask, request, jsonify
import joblib
from lightgbm.sklearn import LGBMRegressor

app = Flask(__name__)

# Function to retrieve the trained model
def retrieve_model(path):
    return joblib.load(path)

# Load the trained model
lgbr_cars = retrieve_model("lgbr_cars.model")

# Function to make predictions
def make_prediction(trained_model, single_input):
    return (trained_model.predict(single_input))[0]

# Route for making predictions
@app.route('/predictCarPrice', methods=['GET'])
def predict_car_price():
    
    # Getting input data from the query parameters
    input_data = [
    int(request.args.get('vehicleType', default_value_for_vehicleType)),
    int(request.args.get('gearbox', default_value_for_gearbox)),
    int(request.args.get('powerPS', default_value_for_powerPS)),
    int(request.args.get('model', default_value_for_model)),
    int(request.args.get('kilometer', default_value_for_kilometer)),
    int(request.args.get('monthOfRegistration', default_value_for_monthOfRegistration)),
    int(request.args.get('fuelType', default_value_for_fuelType)),
    int(request.args.get('brand', default_value_for_brand))
    ]

    # Making prediction
    prediction = make_prediction(lgbr_cars, input_data)

    # Returning the prediction 
    return "Predicted price = "+str(round(predicted_price,2))
    
if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=8080)

