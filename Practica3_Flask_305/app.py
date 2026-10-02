from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    # Mejor que te mande directo al cuadrado
    return render_template('cuadrado.html', area=None, perimetro=None, lado="")

@app.route('/cuadrado', methods=['GET', 'POST'])
def cuadrado():
    area = None
    perimetro = None
    lado_val = ""
    error = None

    if request.method == 'POST':
        lado_val = request.form.get('lado', '')
        try:
            lado = float(lado_val)
            if lado <= 0:
                error = "El lado debe ser mayor que 0"
            else:
                area = lado * lado
                perimetro = 4 * lado
        except ValueError:
            error = "Por favor ingresa un número válido"

    return render_template(
        'cuadrado.html',
        area=area,
        perimetro=perimetro,
        lado=lado_val,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True)