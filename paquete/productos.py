'''
crud
'''


def agregar(base_datos, producto):
    '''
    agrega a la base de datos
    '''
    base_datos.append(producto)


def listar(base_datos):
    '''
    incluir en una lista o bien registar en lista
    '''
    return base_datos


def actualizar(base_datos, nombre, nuevos_datos):
    '''
    actualiza datos
    '''
    for p in base_datos:
        if p.get('producto') == nombre:
            p.update(nuevos_datos)
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
