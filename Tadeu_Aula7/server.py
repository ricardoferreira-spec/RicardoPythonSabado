
from flask import Flask, jsonify, request

#criando aplicação em Flask

app = Flask(__name__)

#get = buscar algo

@app.route("/helloworld", methods=['GET'])
def helloworld():
    return jsonify({
        "msg":"ola mundo, como voces estao?"
    })
    
#Iniciar o srvidor
if __name__ == '__main__':
    app.run(debug=True)
    
    
    