# define simple flask app
from flask import Flask,render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name="World!")

@app.route('/answer', methods=['post'])
def answer():
    name = request.args.get('name')
    return render_template('answer.html', answer="42",name=name)

if __name__ == "__main__":
    app.run(debug=True)
