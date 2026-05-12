'''
lógica del crud
'''


def agregar_producto(coleccion, producto):
    '''
    devuelve el producto
    '''
    coleccion.append(producto)


def mostrar_producto(producto):
    '''
    Imprime el argumento
    '''
    print(producto)


def actualiza_producto(coleccion, nombre_producto, nuevo_dato):
    '''
    actualiza el dato por el argumento pasado
    '''
    for p in coleccion:
        if p.get('producto') == nombre_producto:
            p.update(nuevo_dato)
            return True
    return False


def eliminar(base_datos, nombre):
    '''
    elimina elementos de la base de datos
    '''
    for i, p in enumerate(base_datos):
        if p.get('producto') == nombre:
            del base_datos[i]
            return True

    return False
