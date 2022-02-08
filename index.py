""" Importamos flask """
from flask import Flask, render_template, request


""" instanciamos un objeto app """
app = Flask(__name__)


""" creamos ruta inicial """
@app.route('/')
def home():
    return render_template("inicio.html")



""" creamos ruta buscador """
@app.route('/buscador', methods=["POST"])
def buscador():
    palabra = request.form.get("palabra")
    
    if (palabra.count('cion') or palabra.count('sion') or palabra.count('xion')):
        return render_template("cion.html", palabra=palabra)
    
    elif (palabra.count('ción') or palabra.count('sión') or palabra.count('xión')):
        return render_template("correcto.html", palabra=palabra)
    
    elif ( palabra.count('vr') or palabra.count('vl')):
        return render_template("usoB.html", palabra=palabra)
    
    elif ( palabra.count('br') or palabra.count('bl')):
        return render_template("correcto.html", palabra=palabra)
    
    return render_template("inicio.html", palabra=palabra)


""" creamos otra ruta para palabras terminadas en sion - cion - xion"""
@app.route('/cion')
def cion():
    return render_template('cion.html')


""" creamos otra ruta para el contacto"""
@app.route('/contacto')
def about():
    return render_template('contacto.html')


""" creamos otra ruta uso de las b"""
@app.route('/byv')
def usoB():
    return render_template('usoB.html')


""" creamos otra ruta regla de zcs"""
@app.route('/zcs')
def zcs():
    return render_template('zcs.html')


""" creamos otra ruta Agudas - Graves - Esdrujulas """
@app.route('/ages')
def ages():
    return render_template('ages.html')


""" creamos otra ruta Agudas - Graves - Esdrujulas """
@app.route('/yei')
def yei():
    return render_template('yei.html')


""" creamos otra ruta Agudas - Graves - Esdrujulas """
@app.route('/gyj')
def gyj():
    return render_template('gyj.html')


if __name__ == '__main__':
    app.run(debug=True)