from flask import request, jsonify
from constants import mock_data


transformed_data = {}

def transform_users():
    """Function to Transform the User Data"""
    try:
        global transformed_data

        # Simulate data fetching
        data = mock_data

        # Transform the data (e.g., calculating age in months)
        transformed_data = {
            item['id']: {
                'name': item['name'],
                'age_in_months': item['age'] * 12
            }
            for item in data
        }

        return jsonify({"message": "Users data transformed and saved"}), 200
    
    except Exception as e:
        print("An Exception occured while transforming user data: ", e)
        return jsonify({"message": "Internal Server Error"}), 500



def fetch_transformed_data():
    """Function to Fetch the transformed data"""
    try:
        if not transformed_data:
            return jsonify({"message": "No transformed data found"}), 404

        return jsonify({"message": "Transformed user data fetched successfully", "data": transformed_data}), 200
    
    except Exception as e:
        print("An Exception occured while fetching transformed user data: ", e)
        return jsonify({"message": "Internal Server Error"}), 500
    
    