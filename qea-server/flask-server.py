from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Example route for another page
@app.route('/transitscore', methods=['POST'])
def about():
    input = request.get_json()['data']
    print(input)
    
    address = input['address']
    print(address)

    data = {
        'address': address,
        'quality': {'result':39, 'details':{}},
        'equity': {'result':65,'details':{}},
        'access': {'result':94,'details':{}},
        'cumulative': 64,
        
    }

    print(f'completing POST request for address: {address}')
    print(data)


    return jsonify(data)




def calculate_quality():
    pass

def calculate_access():
    pass

def calculate_equity():
    pass




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
    print("server started successfully :)")
