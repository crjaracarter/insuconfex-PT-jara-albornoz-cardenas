class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto, cantidad):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio * cantidad,
                "cantidad": cantidad,
                "imagen": producto.imagen.url,
                "precio": producto.precio,
            }
        else:
            self.carrito[id]["cantidad"] += cantidad
            self.carrito[id]["acumulado"] += producto.precio * cantidad
        producto.stock -= cantidad  # Restar la cantidad especificada del stock
        producto.stock += cantidad   # Añadir la cantidad especificada al stock
        producto.save()
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            producto.stock += 1
            producto.save()
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def sumar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
            producto.stock -= 1
            producto.save()
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def get_productos(self):
        return self.carrito.values()
    
    