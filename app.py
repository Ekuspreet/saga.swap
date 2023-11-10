from flask import Flask,render_template as rt

app = Flask(__name__)


@app.route('/')
def landing():
    return "Initiated a flask app."
@app.route('/assets')
def assets():
    return rt('assets.html')
if __name__ == "main":
    app.run(debug=True, port='8000')