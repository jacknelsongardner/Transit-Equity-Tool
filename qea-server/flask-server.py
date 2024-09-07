from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
from access import access_by_address
from equity import equity_by_address

app = Flask(__name__, static_folder='build', static_url_path='')
CORS(app)  # Enable CORS for all routes

# Routing user to main page
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


# Example route for another page
@app.route('/transitscore', methods=['POST'])
def about():
    input = request.get_json()['data']
    print(input)
    
    address = input['address']
    print(address)

    access_result = access_by_address(address)
    equity_result = equity_by_address(address)

    print(access_result)
    print(equity_result)

    total_access = access_result['total']
    total_equity = equity_result['total']

    equity_weight = .5
    access_weight = .5

    total = round(access_weight * total_access + (equity_weight * (100 - total_equity)), 0)

    data = {
        'address': address,
        'equity': {'result':total_equity,'details':equity_result},
        'access': {'result':total_access,'details':access_result},
        'cumulative': total,
        
    }

    print(f'completing POST request for address: {address}')
    print(data)


    return jsonify(data)







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
    print("server started successfully :)")
