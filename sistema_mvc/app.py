from flask import Flask
from flask_mysqldb import MySQL # biblioteca mysql flask
import config

app = Flask(__name__)           # instanciar o flask
app.config.from_object(config)  # Configurando variáveis

mysql = MySQL(app)

# passa a conexão para os controllers
app.mysql = mysql

#Rodar o app
if __name__ == '__main__':
    app.run(debug=True)

    