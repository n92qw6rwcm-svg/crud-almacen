'''
Utiles: variados
'''


def entrada(etiqueta='Ingresar dato'):
    '''
    solicita entrada al usuario
    '''
    return input(f'{etiqueta}:\n').strip()


def es_letras(dato):
    '''
    valida entradas con varias palabras y
    devuelve True si el argumento son letras
    '''
    return dato.replace(' ', '').isalpha()


def continuar():
    '''
    estética
    '''
    return input('Ingrese enter para continuar')
