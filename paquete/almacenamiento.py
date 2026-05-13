'''
Módulo persitencia json
escribir/guardar
leer/cargar
'''


import json
import os


def escribir_json(nombre_archivo,
                  argumento):
    '''
    escribe (guarda) en el disco un archivo tipo json
    '''
    # se construye una ruta dinámica para que siempre apunte a la carpeta data

    try:
        ruta = os.path.join('data', f'{nombre_archivo}.json')
        with open(ruta, 'w', encoding='utf-8') as file:
            json.dump(argumento, file, ensure_ascii=False, indent=4)
            return True

    except FileNotFoundError:
        print('Error: la carpeta "data" no existe')
        return False


def leer_json(nombre_archivo):
    '''
    leer (carga) el archivo tipo json
    '''
    ruta = os.path.join('data', f'{nombre_archivo}.json')
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            contenido = json.load(file)

    except FileNotFoundError:
        print('El archivo o carpeta no existe')
        return []

    except json.JSONDecodeError as e:
        print(f'Error json --> {e} <---')
        return []

    return contenido


if __name__ == '__main__':
    escribir = escribir_json('nombres', ['max', 'arnold', 'jane', 'funcionó'])
    leer = leer_json('nombres')
    print(leer)
