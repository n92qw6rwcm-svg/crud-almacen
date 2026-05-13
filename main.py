'''
Lógica del CRUD
'''


from paquete import menu_crud, productos, almacenamiento, utils, formatos as formatos


nombre_archivo = utils.entrada('Ingrese nombre archivo')
bd = almacenamiento.leer_json(nombre_archivo)
contador = 0

while True:

    menu_crud.mostrar_menu()
    menu_eleccion = utils.entrada('Digite elección')

    if menu_eleccion not in ['1', '2', '3', '4', '5']:
        contador += 1
        print('Opción no disponible')
        if contador == 3:
            print('Adíos')
            break

    if menu_eleccion == '1':

        nombre_producto_agregar = formatos.f_nombre_producto()
        if nombre_producto_agregar == 's':
            break

        cantidad_producto_agregar = formatos.f_cantidad_producto()
        if cantidad_producto_agregar == 's':
            break

        productos.agregar(bd, formatos.f_producto(
            nombre_producto_agregar, cantidad_producto_agregar))

        if not almacenamiento.escribir_json(nombre_archivo, bd):
            print('Error: no se pudo guardar')

    if menu_eleccion == '2':
        if not bd:
            print('Vacío')
            utils.continuar()
            continue

        for e, i in enumerate(bd, start=1):
            print(f'{e}. {i}')

        utils.continuar()

    if menu_eleccion == '3':
        nombre_producto_actualizar = formatos.f_nombre_producto()
        cantidad_producto_actualizar = formatos.f_cantidad_producto()

        actualizar_producto = productos.actualizar(bd,
                                                   nombre_producto_actualizar, formatos.f_producto(nombre_producto_actualizar,     cantidad_producto_actualizar))
        if not actualizar_producto:
            print('Producto no encontrado')
        utils.continuar()

        if not almacenamiento.escribir_json(nombre_archivo, bd):
            print('Error: no se pudo guardar')

    if menu_eleccion == '4':
        if not bd:
            print('Vacío')
            utils.continuar()
            continue

        nombre_producto_eliminar = formatos.f_nombre_producto()

        eliminar_producto = productos.eliminar(bd,
                                               nombre_producto_eliminar)
        utils.continuar()

        if not almacenamiento.escribir_json(nombre_archivo, bd):
            print('Error: no se pudo guardar')

    if menu_eleccion == '5':
        print('Programa finalizado')
        break


if not bd:
    print('Vacío')
else:
    for e, i in enumerate(bd, start=1):
        print(f'{e}. {i}')
