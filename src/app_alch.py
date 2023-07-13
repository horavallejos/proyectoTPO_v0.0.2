from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/peques'
app.config['SECRET_KEY'] = 'shhh'  # Clave secreta para proteger las sesiones
db = SQLAlchemy(app)

# class Usuario(db.Model):
#     id_usuario = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(50))
#     apellido = db.Column(db.String(50))
#     correo_electronico = db.Column(db.String(100))
#     contrasena = db.Column(db.String(100))
#     hierarchy = db.Column(db.String(20))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = Usuario.query.filter_by(username=username).first()

#         if user and user.contrasena == password:
#             session['user_id'] = user.id_usuario

#             if user.hierarchy == 'administrador':
#                 return redirect('/crud')
#             elif user.hierarchy == 'usuario':
#                 return redirect('/datos_personales')
#         else:
#             error = 'Nombre de usuario o contraseña incorrectos'
#             return render_template('login.html', error=error)
#     else:
#         return render_template('login.html')

# @app.route('/crud')
# def crud():
#     if 'user_id' in session:
#         user = Usuario.query.get(session['user_id'])
#         if user.hierarchy == 'administrador':
#             return render_template('index.html', user=user)
#         else:
#             return redirect('/login')
#     else:
#         return redirect('/login')

# @app.route('/datos_personales')
# def datos_personales():
#     if 'user_id' in session:
#         user = Usuario.query.get(session['user_id'])
#         if user.hierarchy == 'usuario':
#             # Renderizar la plantilla de datos personales
#             return render_template('datos_personales.html', user=user)
#         else:
#             return redirect('/login')
#     else:
#         return redirect('/login')



class usuarios(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    correo_electronico = db.Column(db.String(100))
    contrasena = db.Column(db.String(100))
    hierarchy = db.Column(db.String(20))

    @staticmethod
    def get_usuario(id_usuario=None):
        if id_usuario is None:
            return usuarios.query.all()
        else:
            return usuarios.query.get(id_usuario)
        
    def create_usuario(self, nombre, apellido, correo_electronico, contrasena, hierarchy):
        usuario = usuarios(nombre=nombre, apellido=apellido, correo_electronico=correo_electronico, contrasena=contrasena, hierarchy=hierarchy)
        db.session.add(usuario)
        db.session.commit()
        return True

    def update_usuario(self, id_usuario, nombre, apellido, correo_electronico, contrasena, hierarchy):
        usuario = usuarios.query.get(id_usuario)
        if usuario:
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.correo_electronico = correo_electronico
            usuario.contrasena = contrasena
            usuario.hierarchy = hierarchy
            db.session.commit()
            return True
        else:
            return False

    def delete_usuario(self, id_usuario):
        usuario = usuarios.query.get(id_usuario)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return True
        else:
            return False
        
@app.route('/')
def index():
    usuarios = usuarios.query.all()
    return render_template('./usuarios.html', usuarios=usuarios)

@app.route('/crear_usuario', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo_electronico = request.form['correo_electronico']
        contrasena = request.form['contrasena']
        hierarchy = request.form['hierarchy']

        usuario = usuarios(nombre=nombre, apellido=apellido, correo_electronico=correo_electronico, contrasena=contrasena, hierarchy=hierarchy)
        db.session.add(usuario)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('index.html')

@app.route('/editar_usuario/<int:id_usuario>', methods=['GET', 'POST'])
def editar_usuario(id_usuario):
    usuario = usuarios.query.get(id_usuario)
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.apellido = request.form['apellido']
        usuario.correo_electronico = request.form['correo_electronico']
        usuario.contrasena = request.form['contrasena']
        usuario.hierarchy = request.form['hierarchy']

        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('editar_usuario.html', usuario=usuario)

@app.route('/eliminar_usuario/<int:id_usuario>', methods=['POST'])
def eliminar_usuario(id_usuario):
    usuario = usuarios.query.get(id_usuario)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
