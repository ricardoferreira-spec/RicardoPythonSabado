from flask import Flask, jsonify, request, render_template

# Criando aplicação em Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# GET > Buscar algo
@app.route("/helloworld", methods=['GET'])
def helloworld():
    return jsonify({
        "msg": "Ola mundo como estao voces"
    })

# Lista de tarefas
tarefas = [
    {"id": 1, "titulo": "Estudar Python", "feito": False},
    {"id": 2, "titulo": "Ler a doc", "feito": True}
]

@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify(tarefas)



# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)

# rodar o programa no terminal
# entrar no google e colar link abaixo na pesquisa
# http://localhost:5000/helloworld


