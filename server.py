from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "llave super duper secreta" #Establecemos una llave secreta para dar mas seguridad a los datos almacenados

#Ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')

#Necesitamos una ruta q vincule con action- Esta url es solo para procesar, luego lo redirigimos a otra url (exito)
@app.route('/proceso', methods=['POST']) #La accion del formulario,, aqui vamos a procesar la info q recibimos del form
def proceso():
    print(request.form)

    #GUARDAMOS EN SESION
    session['nombre'] = request.form['nombre']
    session['apellido'] = request.form['apellido']
    session['email'] = request.form['email']
    session['tipo_usuario'] = request.form['tipo_usuario']

    #return "Procesando información"
    return redirect('/exito') #redirect nos lleva a la nueva URL (exito)



@app.route('/exito')
def exito():
    return render_template('exito.html')


if __name__== "__main__":
    app.run(debug=True)
