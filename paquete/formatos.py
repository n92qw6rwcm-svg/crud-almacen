'''
Formatos validados
'''
from paquete.utils import entrada, es_letras


def f_nombre_producto():
    '''
    Devuelve la solicitud de nombre formateada
    '''
    while True:
        solicitud_nombre_producto = entrada('Ingrese nombre de producto')

        if solicitud_nombre_producto.lower() == 'salir':
            print('Saliendo...')
            return 's'

        if not solicitud_nombre_producto:
            print('Entrada vacía')
            continue

        if not es_letras(solicitud_nombre_producto):
            print('Solo letras')
            continue

        return solicitud_nombre_producto


def f_cantidad_producto():
    '''
    Devuelve la solicitud formateada para usar
    '''
    while True:
        solicitud_cantidad_producto = entrada('Ingrese cantidad')

        if solicitud_cantidad_producto.lower() == 'salir':
            return 's'

        try:
            solicitud_cantidad_producto = int(solicitud_cantidad_producto)

        except ValueError:
            print('Error: Solo se aceptan número')
            continue

        return solicitud_cantidad_producto


def f_producto(producto, cantidad):
    '''
    devuelve el formato del producto
    '''
    return {'producto': producto.lower(), 'cantidad': cantidad}


if __name__ == '__main__':
    a = f_cantidad_producto()
    print(a)
