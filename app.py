from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')



@app.route('/proceso', methods=['POST'])
def proceso():
    nombre=request.form.get("nombre")
    email=request.form.get("email")
    mensaje=request.form.get("mensaje")
    return render_template("salida.html",nombre=nombre,email=email,mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)


