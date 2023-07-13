from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir,'src','templates')
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), './static/img')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__,template_folder=template_dir)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# función busca categorías
def trae_categorias():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM categorias")
    myresult = cursor.fetchall()
    # convertir datos a diccionarios
    categorias = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        categorias.append(dict(zip(columnNames,record)))
    cursor.close()
    return categorias

# función busca todos los productos
def trae_productos(categoria_producto=None):
    cursor = db.database.cursor()
    if categoria_producto == None:
        sql = "SELECT * FROM productos"
        cursor.execute(sql)
        myresult = cursor.fetchall()
    else:
        sql = "SELECT * FROM productos WHERE categoria_producto=%s"
        data = (categoria_producto,)
        cursor.execute(sql,data)
        myresult = cursor.fetchall()
    # convertir datos a diccionarios
    insertProducts = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertProducts.append(dict(zip(columnNames,record)))
    cursor.close()
    return insertProducts

# ******************* FRONT *******************************

# Ruta inicial
@app.route('/')
def home():
    return render_template('Inicio.html')

# Ruta CRUD
@app.route('/crud')
def crud():
    return render_template('index.html')


# Ruta escolar
@app.route('/escolar')
def escolar():
    productos = trae_productos()
    categories=trae_categorias()
    return render_template('escolar.html',data=productos,categories=categories)

# Ruta oficina
@app.route('/oficina')
def oficina():
    productos = trae_productos()
    categories=trae_categorias()
    return render_template('oficina.html',data=productos,categories=categories)

# Ruta arte
@app.route('/arte')
def arte():
    productos = trae_productos()
    categories=trae_categorias()
    return render_template('arte.html',data=productos,categories=categories)

# *******************************************************
# -------------------------------------------------------
# ****************** CRUD *******************************

# ------------------------ #
# ----- USUARIOS  -------- #
# ------------------------ #

# Traigo de la DB los datos para pasar al template users.html
@app.route('/users')
def users():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM usuarios")
    myresult = cursor.fetchall()
    # convertir datos a diccionarios
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames,record)))
    cursor.close()
    return render_template('users.html',data=insertObject)

# Recibo los datos del form del template users.html dar de alta
@app.route('/user',methods=['POST'])
def user():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    password = request.form['password']
    if nombre and apellido and email and password:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuarios (nombre,apellido,correo_electronico,contrasena) VALUES (%s,%s,%s,%s)"
        data = (nombre, apellido, email, password)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('users'))

# ruta para borrar usuarios
@app.route('/delete/<string:id_usuario>')
def delete(id_usuario):
    cursor = db.database.cursor()
    sql = "DELETE FROM usuarios WHERE id_usuario=%s"
    data = (id_usuario,)
    cursor.execute(sql,data)
    db.database.commit()
    return redirect(url_for('users'))

# ruta para modificar usuarios
@app.route('/edit/<string:id_usuario>', methods=['POST'])
def edit(id_usuario):
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    password = request.form['password']
    if nombre and apellido and email and password:
        cursor = db.database.cursor()
        sql = "UPDATE usuarios SET nombre=%s,apellido=%s,correo_electronico=%s,contrasena=%s WHERE id_usuario=%s"
        data = (nombre, apellido, email, password,id_usuario)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('users'))

# ------------------------
# ----- PRODUCTOS --------
# ------------------------

@app.route('/prods')
def prod():
    productos = trae_productos()
    categories=trae_categorias()
    return render_template('prods.html',data=productos,categories=categories)

# ruta para guardar productos
@app.route('/add_prod', methods=['POST'])
def add_prod():
    nombre_producto = request.form['nombre_producto']
    descripcion_producto = request.form['descripcion_producto']
    categoria_producto = request.form['categoria_producto']
    precio_producto = request.form['precio_producto']
    url_img_prod = request.files['url_img_prod']
    filename = url_img_prod.filename
    # Guarda el nombre del archivo en la base de datos
    if nombre_producto and descripcion_producto and categoria_producto and precio_producto:
        cursor = db.database.cursor()
        sql = "INSERT INTO productos (categoria_producto,descripcion_producto,nombre_producto,precio_producto,url_img_prod) VALUES (%s,%s,%s,%s,%s)"
        data = (categoria_producto,descripcion_producto,nombre_producto,precio_producto,filename)
        cursor.execute(sql,data)
        db.database.commit()
    url_img_prod.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('prod'))

# ruta para borrar productos
@app.route('/del_prod/<string:id_producto>')
def del_prod(id_producto):
    cursor = db.database.cursor()
    sql = "DELETE FROM productos WHERE id_producto=%s"
    data = (id_producto,)
    cursor.execute(sql,data)
    db.database.commit()
    return redirect(url_for('prod'))

# ruta para modificar productos
@app.route('/edit_prod/<string:id_producto>', methods=['POST'])
def edit_prod(id_producto):
    nombre_producto = request.form['nombre_producto']
    descripcion_producto = request.form['descripcion_producto']
    categoria_producto = request.form['categoria_producto']
    precio_producto = request.form['precio_producto']
    if nombre_producto and descripcion_producto and categoria_producto and precio_producto:
        cursor = db.database.cursor()
        sql = "INSERT INTO productos (categoria_producto,descripcion_producto,nombre_producto,precio_producto) VALUES (%s,%s,%s,%s)"
        sql = "UPDATE productos SET categoria_producto=%s,descripcion_producto=%s,nombre_producto=%s,precio_producto=%s WHERE id_producto=%s"
        data = (categoria_producto,descripcion_producto,nombre_producto,precio_producto,id_producto)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('prod'))


# ---- EJECUTAMOS LA APLICACIÓN ------------

if __name__ == '__main__':
    app.run(debug=True,port=4000)

