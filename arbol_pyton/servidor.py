from flask import Flask, request

from arbol import arbol


#definir la aplicacion
app = Flask(__name__)

#EDD's
nueva_arbol = arbol()

#rutas
@app.route('/')
def inicio():
    return "hola mundo"

@app.route("/agregar",methods=['post'])
def agregar():
    if request.method == "POST":
        json_entrada = request.get_json()
        dato=json_entrada['valor']
        print(dato)
        try:
            nueva_arbol.insertar(dato)
            return {
                "estado":200,
                 "message": "se inserto el dato"
                 }
        except :
             return {
                "estado":404,
                 "message": "error a intentar insertar"
                 }
       
        
@app.route("/graficar")
def graficar():
    nueva_arbol.graficar()
    return "grafica realizada"

#iniciar el servidor
app.run(host='0.0.0.0', port=3000, debug=True)