# Autor: Mao Ying Gómez Uribe
# Materia: Análisis y Diseño de Algoritmos
# Fecha: 10 de noviembre de 2025
# Archivo: funciones_busqueda.py
# Descripción: Funciones de búsqueda lineal y utilidades del sistema de tienda

def busqueda_lineal_simple(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# ---------------------- BÚSQUEDA EN PRODUCTOS ----------------------

def buscar_producto_por_nombre(productos, nombre):
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            return producto
    return None

def buscar_producto_por_id(productos, id_producto):
    for producto in productos:
        if producto['id'] == id_producto:
            return producto
    return None

def buscar_productos_por_categoria(productos, categoria):
    return [p for p in productos if p['categoria'].lower() == categoria.lower()]

def buscar_productos_disponibles(productos):
    return [p for p in productos if p['stock'] > 0]

def buscar_productos_por_rango_precios(productos, precio_min, precio_max):
    return [p for p in productos if precio_min <= p['precio'] <= precio_max]

def buscar_productos_por_marca(productos, marca):
    return [p for p in productos if p['marca'].lower() == marca.lower()]

def contar_productos_en_categoria(productos, categoria):
    return sum(1 for p in productos if p['categoria'].lower() == categoria.lower())

# ---------------------- BÚSQUEDA EN EMPLEADOS ----------------------

def buscar_empleado_por_nombre_completo(empleados, nombre_completo):
    for empleado in empleados:
        nombre_comp = f"{empleado['nombre']} {empleado['apellido']}"
        if nombre_comp.lower() == nombre_completo.lower():
            return empleado
    return None

def buscar_empleados_por_departamento(empleados, departamento):
    return [e for e in empleados if e['departamento'].lower() == departamento.lower()]

def buscar_empleados_activos(empleados):
    return [e for e in empleados if e['activo']]
