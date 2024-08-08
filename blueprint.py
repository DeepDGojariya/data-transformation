from flask import Blueprint, jsonify, request
import controller

# Create a Blueprint for the API
api_v1 = Blueprint('api_v1', __name__)


# Dictionary to store transformed data
transformed_data = {}

# Endpoint to transform users data
@api_v1.route('/users/transform', methods=['POST'])
def transform_users():
    return controller.transform_users()
    

# Endpoint to retrieve transformed users data
@api_v1.route('/users/transformed', methods=['GET'])
def get_transformed_users():
    return controller.fetch_transformed_data()
    

