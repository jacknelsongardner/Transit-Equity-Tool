from flask import Flask, request, jsonify

app = Flask(__name__)


# Example route for another page
@app.route('/get-data', methods=['POST'])
def about():
    input = request.get_json()
    address = input['address']

    data = {
        'address': address,
        'quality': {'result':39,},
        'equity': {'result':39,},
        'access': {'result':39,},
        'cumulative': 39,
        
    }
    return jsonify(data)




def calculate_quality():
    pass

def calculate_access():
    pass

def calculate_equity():
    pass




if __name__ == '__main__':
    app.run(debug=True)
