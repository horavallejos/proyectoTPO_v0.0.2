import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='peques',
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def execute_query(self, query, data=None):
        if data is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, data)
        self.connection.commit()
        return self.cursor

class CarritoCompras:
    def __init__(self):
        self.db = Database()

    def get_carrito_compras(self, id_carrito_compras):
        query = "SELECT * FROM carrito_compras WHERE id_carrito_compras = %s"
        self.db.execute_query(query, (id_carrito_compras,))
        result = self.db.cursor.fetchone()
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
        self.db.execute_query(query, (id_usuario, fecha_creacion))
        return True

    def update_carrito_compras(self, id_carrito_compras, id_usuario, fecha_creacion):
        query = "UPDATE carrito_compras SET id_usuario = %s, fecha_creacion = %s WHERE id_carrito_compras = %s"
        self.db.execute_query(query, (id_usuario, fecha_creacion, id_carrito_compras))
        return True

    def delete_carrito_compras(self, id_carrito_compras):
        query = "DELETE FROM carrito_compras WHERE id_carrito_compras = %s"
        self.db.execute_query(query, (id_carrito_compras,))
        return True

class Categoria:
    def __init__(self):
        self.db = Database()

    def get_categoria(self, id_categoria):
        query = "SELECT * FROM categorias WHERE id_categoria = %s"
        self.db.execute_query(query, (id_categoria,))
        result = self.db.cursor.fetchone()
        if result:
            id_categoria, nombre_categoria = result
            return {
                "id_categoria": id_categoria,
                "nombre_categoria": nombre_categoria
            }
        return None

    def create_categoria(self, nombre_categoria):
        query = "INSERT INTO categorias (nombre_categoria) VALUES (%s)"
        self.db.execute_query(query, (nombre_categoria,))
        return True

    def update_categoria(self, id_categoria, nombre_categoria):
        query = "UPDATE categorias SET nombre_categoria = %s WHERE id_categoria = %s"
        self.db.execute_query(query, (nombre_categoria, id_categoria))
        return True

    def delete_categoria(self, id_categoria):
        query = "DELETE FROM categorias WHERE id_categoria = %s"
        self.db.execute_query(query, (id_categoria,))
        return True

class Pedido:
    def __init__(self):
        self.db = Database()

    def get_pedido(self, id_pedido):
        query = "SELECT * FROM pedidos WHERE id_pedido = %s"
        self.db.execute_query(query, (id_pedido,))
        result = self.db.cursor.fetchone()
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
        self.db.execute_query(query, (id_usuario, fecha_pedido))
        return True

    def update_pedido(self, id_pedido, id_usuario, fecha_pedido):
        query = "UPDATE pedidos SET id_usuario = %s, fecha_pedido = %s WHERE id_pedido = %s"
        self.db.execute_query(query, (id_usuario, fecha_pedido, id_pedido))
        return True

    def delete_pedido(self, id_pedido):
        query = "DELETE FROM pedidos WHERE id_pedido = %s"
        self.db.execute_query(query, (id_pedido,))
        return True

class Producto:
    def __init__(self):
        self.db = Database()

    def get_producto(self, id_producto):
        query = "SELECT * FROM productos WHERE id_producto = %s"
        self.db.execute_query(query, (id_producto,))
        result = self.db.cursor.fetchone()
        if result:
            id_producto, nombre_producto, descripcion_producto, precio_producto, categoria_producto, url_img_prod, stock_producto = result
            return {
                "id_producto": id_producto,
                "nombre_producto": nombre_producto,
                "descripcion_producto": descripcion_producto,
                "precio_producto": precio_producto,
                "categoria_producto": categoria_producto,
                "url_img_prod": url_img_prod,
                "stock_producto": stock_producto
            }
        return None

    def create_producto(self, nombre_producto, descripcion_producto, precio_producto, categoria_producto, url_img_prod, stock_producto):
        query = "INSERT INTO productos (nombre_producto, descripcion_producto, precio_producto, categoria_producto, url_img_prod, stock_producto) VALUES (%s, %s, %s, %s, %s, %s)"
        self.db.execute_query(query, (nombre_producto, descripcion_producto, precio_producto, categoria_producto, url_img_prod, stock_producto))
        return True

    def update_producto(self, id_producto, nombre_producto, descripcion_producto, precio_producto, categoria_producto, url_img_prod, stock_producto):
        query = "UPDATE productos SET nombre_producto = %s, descripcion_producto = %s, precio_producto = %s, categoria_producto = %s, url_img_prod = %s, stock_producto = %s WHERE id_producto = %s"
        self.db.execute_query(query, (nombre_producto, descripcion_producto, precio_producto, categoria_producto, url_img_prod, stock_producto, id_producto))
        return True

    def delete_producto(self, id_producto):
        query = "DELETE FROM productos WHERE id_producto = %s"
        self.db.execute_query(query, (id_producto,))
        return True

class Usuario:
    def __init__(self):
        self.db = Database()

    def get_usuario(self, id_usuario):
        query = "SELECT * FROM usuarios WHERE id_usuario = %s"
        self.db.execute_query(query, (id_usuario,))
        result = self.db.cursor.fetchone()
        if result:
            id_usuario, nombre, apellido, correo_electronico, contrasena = result
            return {
                "id_usuario": id_usuario,
                "nombre": nombre,
                "apellido": apellido,
                "correo_electronico": correo_electronico,
                "contrasena": contrasena
            }
        return None

    def create_usuario(self, nombre, apellido, correo_electronico, contrasena):
        query = "INSERT INTO usuarios (nombre, apellido, correo_electronico, contrasena) VALUES (%s, %s, %s, %s)"
        self.db.execute_query(query, (nombre, apellido, correo_electronico, contrasena))
        return True

    def update_usuario(self, id_usuario, nombre, apellido, correo_electronico, contrasena):
        query = "UPDATE usuarios SET nombre = %s, apellido = %s, correo_electronico = %s, contrasena = %s WHERE id_usuario = %s"
        self.db.execute_query(query, (nombre, apellido, correo_electronico, contrasena, id_usuario))
        return True

    def delete_usuario(self, id_usuario):
        query = "DELETE FROM usuarios WHERE id_usuario = %s"
        self.db.execute_query(query, (id_usuario,))
        return True
    
