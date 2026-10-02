from flask import flask
app = Flask(__name__)
@app.route('/')
def inicio():
   return 'Hola Flask, mi primera aplicación web'
if __name__ == '__main__':
app.run(debug=True)