from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin


app=Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route('/insertar', methods=['POST'])
def insertar():
    if request.method == 'POST':
        valor = request.json['dato']
        response = jsonify({'response': 'se agrego el '+valor})
        print("metodo post")
        return response
    
@app.route('/insertar', methods=['GET'])
def prueba():
    response = jsonify({'response': 'se agrego el valor'})
    return response

if __name__ == '__main__':
    app.run(port=3000, debug=True)