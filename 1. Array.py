class empresa:
    def __init__(self):
        self.lista_proveedores = []

    def agregar_proveedor(self):
        self.lista_proveedores.append(proveedores())

    def quitar_proveedor(self):
        self.lista_proveedores.pop(int(input("Ingresar el número del proveedor que desea eliminar: ")) - 1)


class proveedores:
    def __init__(self):
        self.nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        self.ciudad_proveedor = input("Ingrese la ciudad del proveedor: ")
        self.articulos = []

    def cambiar_nombre(self):
        self.nombre_proveedor = input("Nuevo nombre del proveedor: ")

    def cambiar_ciudad(self):
        self.ciudad_proveedor = input("Nueva ciudad del proveedor: ")

    def agregar_articulos(self):
        self.articulos.append(
            articulos(len(self.articulos), input("Nombre del artículo: "), int(input("Valor del artículo: ")), int(input("Cantidad de artículos: "))))

    def quitar_articulos(self):
        self.articulos.pop(int(input("ID artículo: ")))


class articulos:
    def __init__(self, Id, Nombre, Valor, Cantidad):
        self.Id = Id
        self.nombre = Nombre
        self.valor = Valor
        self.cantidad = Cantidad


empresa1 = empresa()
empresa1.agregar_proveedor()
empresa1.lista_proveedores[0].cambiar_nombre()
empresa1.lista_proveedores[0].cambiar_ciudad()
empresa1.lista_proveedores[0].agregar_articulos()
print("ID solicitado: ", empresa1.lista_proveedores[0].articulos[len(empresa1.lista_proveedores[0].articulos) - 1].Id)
empresa1.lista_proveedores[0].quitar_articulos()
empresa1.quitar_proveedor()
