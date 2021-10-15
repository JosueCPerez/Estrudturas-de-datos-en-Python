from flask import Flask, request,jsonify
from flask_cors import CORS
from EDD import grafo

app=Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

grafo1= grafo()

@app.route('/insertar', methods=['POST'])
def insertar():
    if request.method == 'POST':
        valor = request.json['dato']
        grafo1.insertar(valor)
        response = jsonify({'response': 'se agrego el '+valor})
        print("metodo post")
        return response

@app.route('/agregar', methods=['POST'])
def agregar():
    if request.method == 'POST':
        valor = request.json['dato']
        ad = request.json['ad']
        grafo1.agregar_adyasente(valor,ad)
        response = jsonify({'response': 'se agrego: -'+valor+' -> '+ad})
        print("metodo post")
        return response
    
@app.route('/graficar', methods=['GET'])
def prueba():
    grafo1.graficar()
    response = jsonify({'response': 'se grafico '})
    return response

if __name__ == '__main__':
    app.run(port=3000, debug=True)