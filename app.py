from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "O OpsTrack API está funcionando :)!"

@app.route("/status")
def status():
    return {"status": "funcionamento ok"}

@app.route("/tickets")
def tickets():
    return [
        {"id": 1, "titulo": "Computador não liga"},
        {"id": 2, "titulo": "Erro de acesso ao sistema"}
    ]

if __name__ == "__main__":
    app.run(debug=True)
