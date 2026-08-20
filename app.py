from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "O OpsTrack API está funcionando :)!"

@app.route("/status")
def status():
    return {"status": "funcionamento ok"}

if __name__ == "__main__":
    app.run(debug=True)
