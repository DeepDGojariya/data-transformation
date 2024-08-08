# DATA TRANSFORMATION

## Description
This is an python application created with the help of Flask which fetches user dataand transforms it.

## Steps To Set up The Code Base

  1. Cloning the Repository. Open a Terminal and paste the following
        
    git clone https://github.com/DeepDGojariya/data-transformation.git .

  2. After Cloning the Repository open the folder in any Code editor of your choice I'd prefer VSCode. Create virtual environment and ctivate it

    a. Install virtualenv package
       pip install virtualenv
    
    b. Create virtual environment
       virtualenv venv
    
    c. Activate virtual enviroment
       venv\Scripts\activate


  3. Now we can install the dependencies.

    pip install -r requirements.txt

  4. Let's Boot the Project up.
    
    python main.py


## Save/Load Data
You can test the data ingestion endpoint in Postman or Thunder Client

METHOD: POST

REQUEST URL: http://127.0.0.1:5000/api/v1/users/transform

## FETCH Transformed Data
You can test the data fetch endpoint in Postman or Thunder Client

METHOD: GET

REQUEST URL: http://127.0.0.1:5000/api/v1/users/transformed

