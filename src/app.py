from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS
import database as db
import os


class CarritoCompras:
    def __init__(self):
        self.db = db.database.cursor()

    def get_carrito_compras(self, id_carrito_compras):
        query = "SELECT * FROM carrito_compras WHERE id_carrito_compras = %s"
        self.db.execute(query, (id_carrito_compras,))
        result = self.db.fetchone()
        if result:
            id_carrito_compras, id_usuario, fecha_creacion = result
            return {
                "id_carrito_compras": id_carrito_compras,
                "id_usuario": id_usuario,
                "fecha_creacion": fecha_creacion
            }
        return None

    def create_carrito_compras(self, id_usuario, fecha_creacion):
        query = "INSERT INTO carrito_compras (id_usuario, fecha_creacion) VALUES (%s, %s)"
        self.db.execute(query, (id_usuario, fecha_creacion))
        db.database.commit()
        return True

    def update_carrito_compras(self, id_carrito_compras, id_usuario, fecha_creacion):
        query = "UPDATE carrito_compras SET id_usuario = %s, fecha_creacion = %s WHERE id_carrito_compras = %s"
        self.db.execute(query, (id_usuario, fecha_creacion, id_carrito_compras))
        db.database.commit()
        return True

    def delete_carrito_compras(self, id_carrito_compras):
        query = "DELETE FROM carrito_compras WHERE id_carrito_compras = %s"
        self.db.execute(query, (id_carrito_compras,))
        db.database.commit()
        return True

class Pedido:
    def __init__(self):
        self.db = db.database.cursor()

    def get_pedido(self, id_pedido):
        query = "SELECT * FROM pedidos WHERE id_pedido = %s"
        self.db.execute(query, (id_pedido,))
        result = self.db.fetchone()
        if result:
            id_pedido, id_usuario, fecha_pedido = result
            return {
                "id_pedido": id_pedido,
                "id_usuario": id_usuario,
                "fecha_pedido": fecha_pedido
            }
        return None

    def create_pedido(self, id_usuario, fecha_pedido):
        query = "INSERT INTO pedidos (id_usuario, fecha_pedido) VALUES (%s, %s)"
        self.db.execute(query, (id_usuario, fecha_pedido))
        db.database.commit()
        return True

    def update_pedido(self, id_pedido, id_usuario, fecha_pedido):
        query = "UPDATE pedidos SET id_usuario = %s, fecha_pedido = %s WHERE id_pedido = %s"
        self.db.execute(query, (id_usuario, fecha_pedido, id_pedido))
        db.database.commit()
        return True

    def delete_pedido(self, id_pedido):
        query = "DELETE FROM pedidos WHERE id_pedido = %s"
        self.db.execute(query, (id_pedido,))
        db.database.commit()
        return True
    
class Categoria:
    def __init__(self):
        self.db = db.database.cursor()

    def get_categorias(self):
        query = "SELECT * FROM categorias"
        self.db.execute(query)
        result = self.db.fetchall()
        if result:
            categories = []
            columnNames = [column[0] for column in self.db.description]
            for record in result:
                categories.append(dict(zip(columnNames,record)))
            self.db.close()
            return categories
        else:
            return None

    def get_categoria(self, id_categoria=None):
        if id_categoria == None:
            query = "SELECT * FROM categorias"
            self.db.execute(query)
            result = self.db.fetchall()
        else:
            query = "SELECT * FROM categorias WHERE id_categoria = %s"
            self.db.execute(query, (id_categoria,))
            result = self.db.fetchone()
            self.db.close()
            return result
        if result:
            categorias = []
            columnNames = [column[0] for column in self.db.description]
            for record in result:
                categorias.append(dict(zip(columnNames,record)))
            self.db.close()
            return categorias
        else:
            return None

    def create_categoria(self, nombre_categoria):
        query = "INSERT INTO categorias (nombre_categoria) VALUES (%s)"
        self.db.execute(query, (nombre_categoria,))
        db.database.commit()
        return True

    def update_categoria(self, id_categoria, nombre_categoria):
        query = "UPDATE categorias SET nombre_categoria = %s WHERE id_categoria = %s"
        self.db.execute(query, (nombre_categoria, id_categoria))
        db.database.commit()
        return True

    def delete_categoria(self, id_categoria):
        query = "DELETE FROM categorias WHERE id_categoria = %s"
        self.db.execute(query, (id_categoria,))
        db.database.commit()
        return True

class Producto:
    def __init__(self):
        self.db = db.database.cursor()

    def get_producto_id(self, id_producto=None):
        if id_producto == None:
            query = "SELECT * FROM productos"
            self.db.execute(query)
            result = self.db.fetchall()
        else:
            query = "SELECT * FROM productos WHERE id_producto = %s"
            self.db.execute(query, (id_producto,))
            result = self.db.fetchall()
        if result:
            insertProducts = []
            columnNames = [column[0] for column in self.db.description]
            for record in result:
                insertProducts.append(dict(zip(columnNames,record)))
            self.db.close()
            return insertProducts
        return None
    
    def get_producto_cat(self, categoria_producto=None):
        if categoria_producto == None:
            query = "SELECT * FROM productos"
            self.db.execute(query)
            result = self.db.fetchall()
        else:
            query = "SELECT * FROM productos WHERE categoria_producto = %s"
            self.db.execute(query, (categoria_producto,))
            result = self.db.fetchall()
            
        if not result:
            self.db.close()
            return None
        else:
            products = []
            columnNames = [column[0] for column in self.db.description]
            for record in result:
                products.append(dict(zip(columnNames,record)))
            self.db.close()
            return products
        
    def create_producto(self, nombre_producto, descripcion_producto, precio_producto, categoria_producto, url_img_prod, stock_producto):
        # self.db = db.database.cursor()
        query = "INSERT INTO productos (nombre_producto, descripcion_producto, precio_producto, categoria_producto, url_img_prod, stock_producto) VALUES (%s, %s, %s, %s, %s, %s)"
        self.db.execute(query, (nombre_producto, descripcion_producto, precio_producto, categoria_producto, url_img_prod, stock_producto))
        db.database.commit()
        return True

    def update_producto(self, id_producto, nombre_producto, descripcion_producto, precio_producto, categoria_producto, url_img_prod, stock_producto):
        query = "UPDATE productos SET nombre_producto = %s, descripcion_producto = %s, precio_producto = %s, categoria_producto = %s, url_img_prod = %s, stock_producto = %s WHERE id_producto = %s"
        self.db.execute(query, (nombre_producto, descripcion_producto, precio_producto, categoria_producto, url_img_prod, stock_producto, id_producto))
        db.database.commit()
        return True

    def delete_producto(self, id_producto):
        query = "DELETE FROM productos WHERE id_producto = %s"
        self.db.execute(query, (id_producto,))
        db.database.commit()
        return True

class Usuario:
    def __init__(self):
        self.db = db.database.cursor()

    def get_usuario(self, id_usuario=None):
        if id_usuario == None:
            query = "SELECT * FROM usuarios"
            self.db.execute(query)
            result = self.db.fetchall()
        else:
            query = "SELECT * FROM usuarios WHERE id_usuario = %s"
            self.db.execute(query, (id_usuario,))
            result = self.db.fetchone()
            self.db.close()
            return result
        if result:
            usuarios = []
            columnNames = [column[0] for column in self.db.description]
            for record in result:
                usuarios.append(dict(zip(columnNames,record)))
            self.db.close()
            return usuarios
        else:
            return None
        

    def create_usuario(self, nombre, apellido, correo_electronico, contrasena):
        query = "INSERT INTO usuarios (nombre, apellido, correo_electronico, contrasena) VALUES (%s, %s, %s, %s)"
        self.db.execute(query, (nombre, apellido, correo_electronico, contrasena))
        db.database.commit()
        return True

    def update_usuario(self, id_usuario, nombre, apellido, correo_electronico, contrasena):
        query = "UPDATE usuarios SET nombre = %s, apellido = %s, correo_electronico = %s, contrasena = %s WHERE id_usuario = %s"
        self.db.execute(query, (nombre, apellido, correo_electronico, contrasena, id_usuario))
        db.database.commit()
        return True

    def delete_usuario(self, id_usuario):
        query = "DELETE FROM usuarios WHERE id_usuario = %s"
        self.db.execute(query, (id_usuario,))
        db.database.commit()
        return True

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir,'src','templates')

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), './static/img')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__,template_folder=template_dir)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

# Ruta inicial
@app.route('/')
def home():
    return render_template('Inicio.html')

# Ruta CRUD
@app.route('/crud')
def crud():
    return render_template('index.html')

# Traigo de la DB los datos para pasar al template users.html
@app.route('/crud_users')
def crud_users():
    usuarios = Usuario().get_usuario()
    # return render_template('users.html',data=usuarios)
    return render_template('users.html',data=usuarios)

# Traigo de la DB los datos para pasar al template prods.html
@app.route('/crud_prods')
def crud_prods():
    productos = Producto().get_producto_id()
    categorias = Categoria().get_categorias()
    return render_template('prods.html',data=productos,categories=categorias)

# Traigo de la DB los datos para pasar al template categ.html
@app.route('/crud_categ')
def crud_categ():
    categorias = Categoria().get_categorias()
    return render_template('categ.html',data=categorias)

# Ruta escolar
@app.route('/escolar')
def escolar():
    productos = Producto().get_producto_cat(2)
    categories= Categoria().get_categorias()
    return render_template('escolar.html',data=productos,categories=categories)

# Ruta oficina
@app.route('/oficina')
def oficina():
    productos = Producto().get_producto_cat(3)
    if not productos:
        productos = Producto().get_producto_cat(1)
    categories= Categoria().get_categorias()
    return render_template('oficina.html',data=productos,categories=categories)

# Ruta arte
@app.route('/arte')
def arte():
    productos = Producto().get_producto_cat(4)
    if not productos:
        productos = Producto().get_producto_cat(1)
    categories= Categoria().get_categorias()
    return render_template('arte.html',data=productos,categories=categories)

# ==========================================================

@app.route('/producto')
def obtener_productos():
    productos = Producto().get_producto_id()
    return productos

@app.route('/producto/<int:id_producto>')
def obtener_producto(id_producto):
    producto = Producto().get_producto_id(id_producto)
    if producto:
        return jsonify(producto)
    else:
        return jsonify({'error': 'Producto no encontrado'}), 404

@app.route('/producto/cat')
def obtener_productos_cat():
    productos = Producto().get_producto_id()
    return jsonify(productos)

@app.route('/producto/cat/<int:categoria_producto>')
def obtener_producto_cat(categoria_producto):
    producto = Producto().get_producto_cat(categoria_producto)
    if producto:
        return jsonify(producto)
    else:
        return jsonify({'error': 'Producto no encontrado'}), 404

@app.route('/producto', methods=['POST'])
def crear_producto():
    nombre_producto = request.form['nombre_producto']
    descripcion_producto = request.form['descripcion_producto']
    precio_producto = request.form['precio_producto']
    categoria_producto = request.form['categoria_producto']
    url_img_prod = request.files['url_img_prod']
    filename = url_img_prod.filename
    stock_producto = request.form['stock_producto']
    if nombre_producto and precio_producto and categoria_producto and url_img_prod:
        Producto().create_producto(nombre_producto, descripcion_producto, precio_producto, categoria_producto, filename, stock_producto)
    url_img_prod.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    productos = Producto().get_producto_id()
    categorias = Categoria().get_categorias()
    return render_template('prods.html',data=productos,categories=categorias)
    
@app.route('/producto/<int:id_producto>', methods=['POST'])
def actualizar_producto(id_producto):
    nombre_producto = request.form['nombre_producto']
    descripcion_producto = request.form['descripcion_producto']
    precio_producto = request.form['precio_producto']
    categoria_producto = request.form['categoria_producto']
    url_img_prod = request.files['url_img_prod']
    filename = url_img_prod.filename
    stock_producto = request.form['stock_producto']
    Producto().update_producto(id_producto, nombre_producto, descripcion_producto, precio_producto, categoria_producto, filename, stock_producto)
    url_img_prod.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    productos = Producto().get_producto_id()
    categorias = Categoria().get_categorias()
    return render_template('prods.html',data=productos,categories=categorias)

@app.route('/producto_/<string:id_producto>')
def eliminar_producto(id_producto):
    Producto().delete_producto(id_producto)
    productos = Producto().get_producto_id()
    categorias = Categoria().get_categorias()
    return render_template('prods.html',data=productos,categories=categorias)

# Rutas y funciones para las otras clases (CarritoCompras, Categoria, Pedido, Usuario) siguiendo el mismo patrón.
@app.route('/usuarios')
def obtener_usuarios():
    usuarios = Usuario().get_usuario()
    return jsonify(usuarios)

@app.route('/usuarios/<int:id_usuario>')
def obtener_usuario(id_usuario):
    usuario = Usuario().get_usuario(id_usuario)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo_electronico = request.form['email']
    contrasena  = request.form['password']
    Usuario().create_usuario(nombre, apellido, correo_electronico, contrasena)
    usuarios = Usuario().get_usuario()
    return render_template('users.html',data=usuarios)

@app.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo_electronico = request.form['email']
    contrasena  = request.form['password']
    Usuario().update_usuario(id_usuario, nombre, apellido, correo_electronico, contrasena)
    usuarios = Usuario().get_usuario()
    return render_template('users.html',data=usuarios)

@app.route('/usuarios_del/<int:id_usuario>')
def eliminar_usuario(id_usuario):
    Usuario().delete_usuario(id_usuario)
    usuarios = Usuario().get_usuario()
    return render_template('users.html',data=usuarios)

# Rutas y funciones para las otras clases (CarritoCompras, Categoria, Pedido, Producto) siguiendo el mismo patrón.
@app.route('/carrito_compras')
def obtener_carrito_compras():
    carrito_compras = CarritoCompras().get_carrito_compras()
    return jsonify(carrito_compras)

@app.route('/carrito_compras/<int:id_carrito_compras>')
def obtener_carrito_compra(id_carrito_compras):
    carrito_compra = CarritoCompras().get_carrito_compras(id_carrito_compras)
    if carrito_compra:
        return jsonify(carrito_compra)
    else:
        return jsonify({'error': 'Carrito de compras no encontrado'}), 404

@app.route('/carrito_compras', methods=['POST'])
def crear_carrito_compra():
    id_usuario = request.json.get('id_usuario')
    fecha_creacion = request.json.get('fecha_creacion')
    CarritoCompras().create_carrito_compras(id_usuario, fecha_creacion)
    return jsonify({'mensaje': 'Carrito de compras creado exitosamente'})

@app.route('/carrito_compras/<int:id_carrito_compras>', methods=['PUT'])
def actualizar_carrito_compra(id_carrito_compras):
    id_usuario = request.json.get('id_usuario')
    fecha_creacion = request.json.get('fecha_creacion')
    CarritoCompras().update_carrito_compras(id_carrito_compras, id_usuario, fecha_creacion)
    return jsonify({'mensaje': 'Carrito de compras actualizado exitosamente'})

@app.route('/carrito_compras/<int:id_carrito_compras>', methods=['DELETE'])
def eliminar_carrito_compra(id_carrito_compras):
    CarritoCompras().delete_carrito_compras(id_carrito_compras)
    return jsonify({'mensaje': 'Carrito de compras eliminado exitosamente'})

@app.route('/categorias')
def obtener_categorias():
    categorias = Categoria().get_categorias()
    return categorias

@app.route('/categorias/<int:id_categoria>')
def obtener_categoria(id_categoria):
    categoria = Categoria().get_categoria(id_categoria)
    if categoria:
        return jsonify(categoria)
    else:
        return jsonify({'error': 'Categoría no encontrada'}), 404

@app.route('/categorias', methods=['POST'])
def crear_categoria():
    nombre_categoria = request.form['nombre_categoria']
    Categoria().create_categoria(nombre_categoria)
    categorias = Categoria().get_categorias()
    return render_template('categ.html',data=categorias)

@app.route('/categorias_up/<string:id_categoria>', methods=['POST'])
def categorias_up(id_categoria):
    nombre_categoria = request.form['nombre_categoria']
    Categoria().update_categoria(id_categoria, nombre_categoria)
    categorias = Categoria().get_categorias()
    return render_template('categ.html',data=categorias)

@app.route('/categorias_del/<string:id_categoria>', methods=['GET'])
def eliminar_categoria(id_categoria):
    Categoria().delete_categoria(id_categoria)
    categorias = Categoria().get_categorias()
    return render_template('categ.html',data=categorias)

@app.route('/pedidos')
def obtener_pedidos():
    pedidos = Pedido().get_pedido()
    return jsonify(pedidos)

@app.route('/pedidos/<int:id_pedido>')
def obtener_pedido(id_pedido):
    pedido = Pedido().get_pedido(id_pedido)
    if pedido:
        return jsonify(pedido)
    else:
        return jsonify({'error': 'Pedido no encontrado'}), 404

@app.route('/pedidos', methods=['POST'])
def crear_pedido():
    id_usuario = request.json.get('id_usuario')
    fecha_pedido = request.json.get('fecha_pedido')
    Pedido().create_pedido(id_usuario, fecha_pedido)
    return jsonify({'mensaje': 'Pedido creado exitosamente'})

@app.route('/pedidos/<int:id_pedido>', methods=['PUT'])
def actualizar_pedido(id_pedido):
    id_usuario = request.json.get('id_usuario')
    fecha_pedido = request.json.get('fecha_pedido')
    Pedido().update_pedido(id_pedido, id_usuario, fecha_pedido)
    return jsonify({'mensaje': 'Pedido actualizado exitosamente'})

@app.route('/pedidos/<int:id_pedido>', methods=['DELETE'])
def eliminar_pedido(id_pedido):
    Pedido().delete_pedido(id_pedido)
    return jsonify({'mensaje': 'Pedido eliminado exitosamente'})

@app.route('/prods')
def prod():
    productos = Producto().get_producto_id()
    categories= Categoria().get_categorias()
    return render_template('prods.html',data=productos,categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
