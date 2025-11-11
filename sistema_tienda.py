# Autor: Mao Ying Gómez Uribe
# Materia: Análisis y Diseño de Algoritmos
# Fecha: 10 de noviembre de 2025
# Archivo: sistema_tienda.py
# Descripción: Programa principal con menú interactivo para búsquedas en sistema de tienda electrónica

from funciones_busqueda import *
from datos_ejemplo import productos, empleados

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Buscar Producto por Nombre")
        print("2. Buscar Producto por ID")
        print("3. Buscar Productos por Categoría")
        print("4. Buscar Empleado por Nombre Completo")
        print("5. Buscar Empleados por Departamento")
        print("6. Buscar Empleados Activos")
        print("7. Buscar Productos Disponibles")
        print("8. Buscar Productos por Rango de Precios")
        print("9. Buscar Productos por Marca")
        print("10. Contar Productos en una Categoría")
        print("11. Salir")

        opcion = input("Seleccione una opción (1-11): ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            print(buscar_producto_por_nombre(productos, nombre))

        elif opcion == '2':
            id_producto = int(input("Ingrese el ID del producto: "))
            print(buscar_producto_por_id(productos, id_producto))

        elif opcion == '3':
            categoria = input("Ingrese la categoría: ")
            print(buscar_productos_por_categoria(productos, categoria))

        elif opcion == '4':
            nombre_completo = input("Ingrese el nombre completo del empleado: ")
            print(buscar_empleado_por_nombre_completo(empleados, nombre_completo))

        elif opcion == '5':
            departamento = input("Ingrese el departamento: ")
            print(buscar_empleados_por_departamento(empleados, departamento))

        elif opcion == '6':
            print(buscar_empleados_activos(empleados))

        elif opcion == '7':
            print(buscar_productos_disponibles(productos))

        elif opcion == '8':
            precio_min = float(input("Ingrese precio mínimo: "))
            precio_max = float(input("Ingrese precio máximo: "))
            print(buscar_productos_por_rango_precios(productos, precio_min, precio_max))

        elif opcion == '9':
            marca = input("Ingrese la marca: ")
            print(buscar_productos_por_marca(productos, marca))

        elif opcion == '10':
            categoria = input("Ingrese la categoría: ")
            print("Total productos:", contar_productos_en_categoria(productos, categoria))

        elif opcion == '11':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
