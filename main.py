#Importando Framework WEB
from flask import Flask, render_template
from flask_socketio import SocketIO, send

#Renominando o Flask
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)


#Criando rota homepage
@app.route("/")
def homepage():
    return render_template("homepage.html")


#iniciar o app
socketio.run(app, host="lucaszap.onrender.com", port=80)
