import tkinter as tk
from tkinter import ttk 
import json
import time


#Características:
#Complejidad Temporal:** O(n) - en el peor caso
#Complejidad Espacial:** O(1) - espacio constante
#No requiere datos ordenados**
#Algoritmo estable**

### Pseudocódigo:

'''FUNCIÓN búsqueda_lineal(lista, elemento_buscado):
    PARA i = 0 HASTA longitud(lista) - 1:
        SI lista[i] == elemento_buscado:
            RETORNAR i
    RETORNAR -1  // No encontrado'''


#CONTEXTO DEL PROBLEMA

#Sistema de Tienda de Electrónica "TechStore"

#Necesitamos implementar un sistema de gestión para una tienda de electrónica que permita:

#1.Búsqueda de productos** por nombre, marca o categoría
#2. Búsqueda de empleados** por nombre, ID o departamento
#3. Búsqueda de disponibilidad** de productos por stock
#4. Gestión de inventario** básica

#Estructuras de Datos a Utilizar:


# Estructura de un producto
producto = {
    'id': int,
    'nombre': str,
    'marca': str,
    'categoria': str,
    'precio': float,
    'stock': int,
    'disponible': bool
}

# Estructura de un empleado
empleado = {
    'id': int,
    'nombre': str,
    'apellido': str,
    'departamento': str,
    'salario': float,
    'activo': bool
}









#___________________________________________________________________________________________________________________________
#EJERCICIOS PRÁCTICOS

#EJERCICIO 1:Implementación Básica de Búsqueda Lineal
#Objetivo: Implementar la función básica de búsqueda lineal

#Instrucciones:
#1. Crear una función `busqueda_lineal_simple(lista, elemento)` que busque un elemento en una lista de números

#solución punto 1
def busqueda_lineal_simple(lista, elemento):
    """
    Busca un elemento en una lista usando búsqueda lineal
    
    Args:
        lista: Lista de elementos
        elemento: Elemento a buscar
    
    Returns:
        int: Índice del elemento si se encuentra, -1 si no
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1


#2. La función debe retornar el índice del elemento si lo encuentra, o -1 si no lo encuentra

#como podemos ver en la función anterior ya se cumple este requisito.

#3. Probar la función con diferentes casos

#probando la función
numeros = [3, 15, 25, 42, 7, 8, 19]
print(busqueda_lineal_simple(numeros, 25))  # Output: debe ser 2
print(busqueda_lineal_simple(numeros, 3))   # Output: debe ser 0
print(busqueda_lineal_simple(numeros, 19))  # Output: debe ser 6


#___________________________________________________________________________________________________________________________






#Código base:
def busqueda_lineal_simple(lista, elemento):
    """
    Busca un elemento en una lista usando búsqueda lineal

    Args:
        lista: Lista de elementos
        elemento: Elemento a buscar

    Returns:
        int: Índice del elemento si se encuentra, -1 si no
    """
    # todo: Implementar aquí (esta versión es la implementación funcional)
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1



#EJERCICIO 2: Búsqueda en Lista de Productos

#Objetivo: Implementar búsqueda lineal en una lista de diccionarios

#Instrucciones:
#1.Crear una lista de productos de ejemplo
#2.Implementar función para buscar producto por nombre
#3.Implementar función para buscar producto por ID
#4.Implementar función para buscar productos por categoría

#Datos de ejemplo:

productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]


#solución punto 2:
def buscar_producto_por_nombre(productos, nombre):
    """
    Busca un producto por nombre en una lista de productos

    Args:
        productos: Lista de diccionarios de productos
        nombre: Nombre del producto a buscar

    Returns:
        dict: Producto encontrado o None si no se encuentra
    """
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            return producto
    return None
#probando la función
print(buscar_producto_por_nombre(productos, 'MacBook Air M3'))  # Output
# debe ser el diccionario del MacBook Air M3

#solución punto 3 del ejercicio buscar por ID:
def buscar_producto_por_id(productos, id_producto):
    """
    Busca un producto por ID en una lista de productos

    Args:
        productos: Lista de diccionarios de productos
        id_producto: ID del producto a buscar

    Returns:
        dict: Producto encontrado o None si no se encuentra
    """
    for producto in productos:
        if producto['id'] == id_producto:
            return producto
    return None
#probando la función
print(buscar_producto_por_id(productos, 4))  # Output
# debe ser el diccionario del Dell XPS 13


#solucion punto 3 del ejercicio buscar por categoría:
def buscar_productos_por_categoria(productos, categoria):
    """
    Busca productos por categoría en una lista de productos

    Args:
        productos: Lista de diccionarios de productos
        categoria: Categoría de los productos a buscar

    Returns:
        list: Lista de productos encontrados en la categoría
    """
    encontrados = []
    for producto in productos:
        if producto['categoria'].lower() == categoria.lower():
            encontrados.append(producto)
    return encontrados
#probando la función
print(buscar_productos_por_categoria(productos, 'Laptop'))  # Output
# debe ser una lista con los diccionarios de MacBook Air M3 y Dell XPS 13







#___________________________________________________________________________________________________________________________

#EJERCICIO 3: Búsqueda de Empleados

#Objetivo: Implementar búsqueda en lista de empleados

#Instrucciones del ejercicio 3:
#1. Crear lista de empleados
#2. Implementar búsqueda por nombre completo
#3. Implementar búsqueda por departamento
#4. Implementar búsqueda de empleados activos

#Datos de ejemplo:

empleados = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True}
]

#solución punto 3 implementar búsqueda por nombre completo:
def buscar_empleado_por_nombre_completo(empleados, nombre_completo):
    """
    Busca un empleado por nombre completo en una lista de empleados

    Args:
        empleados: Lista de diccionarios de empleados
        nombre_completo: Nombre completo del empleado a buscar

    Returns:
        dict: Empleado encontrado o None si no se encuentra
    """
    for empleado in empleados:
        nombre_completo_empleado = f"{empleado['nombre']} {empleado['apellido']}"
        if nombre_completo_empleado.lower() == nombre_completo.lower():
            return empleado
    return None
#probando la función
print(buscar_empleado_por_nombre_completo(empleados, 'Carlos López'))  # Output
# debe ser el diccionario del empleado Carlos López


# solución punto 4 implementar búsqueda por departamento:
def buscar_empleados_por_departamento(empleados, departamento):
    """
    Busca empleados por departamento en una lista de empleados

    Args:
        empleados: Lista de diccionarios de empleados
        departamento: Departamento de los empleados a buscar

    Returns:
        list: Lista de empleados encontrados en el departamento
    """
    encontrados = []
    for empleado in empleados:
        if empleado['departamento'].lower() == departamento.lower():
            encontrados.append(empleado)
    return encontrados
#probando la función
print(buscar_empleados_por_departamento(empleados, 'Ventas'))  # Output
# debe ser una lista con los diccionarios de Ana García y María Rodríguez

#solución punto 4 implementar búsqueda de empleados activos:
def buscar_empleados_activos(empleados):
    """
    Busca empleados activos en una lista de empleados

    Args:
        empleados: Lista de diccionarios de empleados

    Returns:
        list: Lista de empleados activos
    """
    activos = []
    for empleado in empleados:
        if empleado['activo']:
            activos.append(empleado)
    return activos
#probando la función
print(buscar_empleados_activos(empleados))  # Output
# debe ser una lista con los empleados que tienen 'activo': True




#___________________________________________________________________________________________________________________________

#EJERCICIO 4: Búsqueda por Disponibilidad

#Objetivo: Implementar búsquedas condicionales

#Instrucciones del ejercicio 4:
#1. Buscar productos disponibles (stock > 0)
#2. Buscar productos por rango de precios
#3. Buscar productos de una marca específica
#4. Contar productos en una categoría

#solución punto 4 buscar productos disponibles (stock > 0):
def buscar_productos_disponibles(productos):
    """
    Busca productos disponibles (stock > 0) en una lista de productos

    Args:
        productos: Lista de diccionarios de productos

    Returns:
        list: Lista de productos disponibles
    """
    disponibles = []
    for producto in productos:
        if producto['stock'] > 0:
            disponibles.append(producto)
    return disponibles
#probando la función
print(buscar_productos_disponibles(productos))  # Output
# debe ser una lista con los productos que tienen stock > 0

#solución punto 4 buscar productos por rango de precios:
def buscar_productos_por_rango_precios(productos, precio_min, precio_max):
    """
    Busca productos por rango de precios en una lista de productos

    Args:
        productos: Lista de diccionarios de productos
        precio_min: Precio mínimo
        precio_max: Precio máximo

    Returns:
        list: Lista de productos dentro del rango de precios
    """
    encontrados = []
    for producto in productos:
        if precio_min <= producto['precio'] <= precio_max:
            encontrados.append(producto)
    return encontrados
#probando la función    
print(buscar_productos_por_rango_precios(productos, 500, 1000))  # Output
# debe ser una lista con los productos cuyo precio está entre 500 y 1000


#solución punto 4 buscar productos de una marca específica:
def buscar_productos_por_marca(productos, marca):
    """
    Busca productos por marca en una lista de productos

    Args:
        productos: Lista de diccionarios de productos
        marca: Marca de los productos a buscar

    Returns:
        list: Lista de productos de la marca especificada
    """
    encontrados = []
    for producto in productos:
        if producto['marca'].lower() == marca.lower():
            encontrados.append(producto)
    return encontrados
#probando la función
print(buscar_productos_por_marca(productos, 'Apple'))  # Output
# debe ser una lista con los productos de la marca Apple

#solución punto 4 contar productos en una categoría:
def contar_productos_en_categoria(productos, categoria):
    """
    Cuenta productos en una categoría en una lista de productos

    Args:
        productos: Lista de diccionarios de productos
        categoria: Categoría de los productos a contar

    Returns:
        int: Número de productos en la categoría especificada
    """
    contador = 0
    for producto in productos:
        if producto['categoria'].lower() == categoria.lower():
            contador += 1
    return contador
#probando la función
print(contar_productos_en_categoria(productos, 'Smartphone'))  # Output
# debe ser 2 ya que hay 2 productos en la categoría Smartphone



#___________________________________________________________________________________________________________________________


#EJERCICIO 5: Sistema Integrado


#Objetivo: Crear un menú interactivo que integre todas las funciones

#Funcionalidades requeridas del ejercicio 5:
#1. Menú principal con opciones
#2. Submenús para cada tipo de búsqueda
#3. Validación de entrada del usuario
#4. Manejo de errores básico
#5. Opción de salir del programa

#solución punto 5 crear menú interactivo con submenus para cada tipo de búsqueda y opción de salir del programa:
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
            resultado = buscar_producto_por_nombre(productos, nombre)
            print("Resultado:", resultado)

        elif opcion == '2':
            id_producto = int(input("Ingrese el ID del producto: "))
            resultado = buscar_producto_por_id(productos, id_producto)
            print("Resultado:", resultado)

        elif opcion == '3':
            categoria = input("Ingrese la categoría del producto: ")
            resultado = buscar_productos_por_categoria(productos, categoria)
            print("Resultado:", resultado)

        elif opcion == '4':
            nombre_completo = input("Ingrese el nombre completo del empleado: ")
            resultado = buscar_empleado_por_nombre_completo(empleados, nombre_completo)
            print("Resultado:", resultado)

        elif opcion == '5':
            departamento = input("Ingrese el departamento: ")
            resultado = buscar_empleados_por_departamento(empleados, departamento)
            print("Resultado:", resultado)

        elif opcion == '6':
            resultado = buscar_empleados_activos(empleados)
            print("Resultado:", resultado)

        elif opcion == '7':
            resultado = buscar_productos_disponibles(productos)
            print("Resultado:", resultado)

        elif opcion == '8':
            precio_min = float(input("Ingrese el precio mínimo: "))
            precio_max = float(input("Ingrese el precio máximo: "))
            resultado = buscar_productos_por_rango_precios(productos, precio_min, precio_max)
            print("Resultado:", resultado)

        elif opcion == '9':
            marca = input("Ingrese la marca del producto: ")
            resultado = buscar_productos_por_marca(productos, marca)
            print("Resultado:", resultado)
        elif opcion == '10':
            categoria = input("Ingrese la categoría del producto: ")
            resultado = contar_productos_en_categoria(productos, categoria)
            print("Número de productos en la categoría:", resultado)
        elif opcion == '11':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
# Iniciar el menú principal
menu_principal()

 
#ACTIVIDADES ADICIONALES DEL EJERCICIO

#Actividad 1: Análisis de Complejidad
#____________________________________________________________
#¿Cuál es la complejidad temporal de cada función implementada?
#rpta: La complejidad temporal de cada función implementada es O(n) en el peor caso,
# donde n es el número de elementos en la lista que se está buscando. 
# Esto se debe a que en el peor caso, la función puede tener que recorrer toda 
# la lista para encontrar el elemento buscado o determinar que no está presente.
#____________________________________________________________


#____________________________________________________________
#¿En qué casos la búsqueda lineal es eficiente?
#rpta: La búsqueda lineal es eficiente en listas pequeñas o cuando los elementos
# están distribuidos de manera uniforme y no hay un orden específico.
#____________________________________________________________


#____________________________________________________________
#¿Cuándo sería mejor usar otro algoritmo de búsqueda?
#rpta: Sería mejor usar otro algoritmo de búsqueda, como la búsqueda binaria,
# cuando la lista está ordenada, ya que la búsqueda binaria tiene una complejidad
# temporal de O(log n), lo que la hace mucho más eficiente para listas grandes.
#____________________________________________________________



#___________________________________________________________________________________________________________________________
#Actividad 2: Optimizaciones
#Implementar búsqueda que pare cuando encuentre el primer resultado
def busqueda_lineal_optimizada(lista, elemento):
    """
    Busca un elemento en una lista usando búsqueda lineal optimizada

    Args:
        lista: Lista de elementos
        elemento: Elemento a buscar

    Returns:
        int: Índice del elemento si se encuentra, -1 si no
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # Retorna inmediatamente al encontrar el primer resultado
    return -1

#Implementar búsqueda que retorne todos los resultados que coincidan
def busqueda_lineal_todos_resultados(lista, elemento):
    """
    Busca todos los elementos que coincidan en una lista usando búsqueda lineal

    Args:
        lista: Lista de elementos
        elemento: Elemento a buscar

    Returns:
        list: Lista de índices de los elementos encontrados
    """
    resultados = []
    for i in range(len(lista)):
        if lista[i] == elemento:
            resultados.append(i)
    return resultados

#Agregar contador de comparaciones realizadas
def busqueda_lineal_con_contador(lista, elemento):
    """
    Busca un elemento en una lista usando búsqueda lineal con contador de comparaciones

    Args:
        lista: Lista de elementos
        elemento: Elemento a buscar

    Returns:
        tuple: (Índice del elemento si se encuentra, -1 si no, número de comparaciones realizadas)
    """
    contador_comparaciones = 0
    for i in range(len(lista)):
        contador_comparaciones += 1
        if lista[i] == elemento:
            return (i, contador_comparaciones)
    return (-1, contador_comparaciones)
#____________________________________________________________________________________________________________________________



#___________________________________________________________________________________________________________________________
#Actividad 3: Casos Especiales

#¿Qué pasa si la lista está vacía?
#La función retornará -1 indicando que el elemento no se encuentra.

#¿Cómo manejar búsquedas con mayúsculas/minúsculas?
#Se puede convertir tanto el elemento buscado como los elementos de la lista a minúsculas

#¿Cómo buscar texto parcial en nombres?
#Se puede usar el operador "in" para verificar si el texto parcial está contenido en el nombre.
#____________________________________________________________________________________________________________________________













#____________________________________________________________________________________________________________________________
#CHECKLIST DE ENTREGA

#Archivos a Entregar:
#[ ] `sistema_tienda.py` - Código principal del sistema
#[ ] `funciones_busqueda.py` - Funciones de búsqueda implementadas
#[ ] `datos_ejemplo.py` - Datos de prueba
#[ ] `README.md` - Documentación del proyecto
#[ ] `informe_taller.pdf` - Análisis y conclusiones
#____________________________________________________________________________________________________________________________






#___________________________________________________________________________________________________________________________
#DESAFÍOS ADICIONALES

#Desafío 1: Búsqueda Avanzada

#Implementar búsqueda que permita:
#Búsqueda por múltiples criterios simultáneamente
#Búsqueda con operadores lógicos (AND, OR)
#Búsqueda aproximada (tolerancia a errores de escritura)

#solucion del desafío 1:
def busqueda_avanzada_productos(productos, criterios):
    """
    Busca productos por múltiples criterios simultáneamente

    Args:
        productos: Lista de diccionarios de productos
        criterios: Diccionario con criterios de búsqueda (puede incluir 'nombre', 'marca', 'categoria', 'precio_min', 'precio_max')

    Returns:
        list: Lista de productos que cumplen con todos los criterios
    """
    encontrados = []
    for producto in productos:
        cumple_criterios = True
        if 'nombre' in criterios and criterios['nombre'].lower() not in producto['nombre'].lower():
            cumple_criterios = False
        if 'marca' in criterios and criterios['marca'].lower() != producto['marca'].lower():
            cumple_criterios = False
        if 'categoria' in criterios and criterios['categoria'].lower() != producto['categoria'].lower():
            cumple_criterios = False
        if 'precio_min' in criterios and producto['precio'] < criterios['precio_min']:
            cumple_criterios = False
        if 'precio_max' in criterios and producto['precio'] > criterios['precio_max']:
            cumple_criterios = False
        if cumple_criterios:
            encontrados.append(producto)
    return encontrados


#en el ejercicio anterior se implementa la búsqueda por múltiples criterios simultáneamente.
#también se puede implementar la búsqueda con operadores lógicos (AND, OR) y búsqueda aproximada
#tolerancia a errores de escritura usando bibliotecas como difflib para comparar cadenas.
#ya que la implementación puede variar según los requisitos específicos.
#se puede utilizar la función get_close_matches de difflib para sugerir correcciones.

#probando la función
criterios_busqueda = {
    'nombre': 'iPhone',
    'marca': 'Apple',
    'precio_min': 500,
    'precio_max': 1500
}
resultados_avanzados = busqueda_avanzada_productos(productos, criterios_busqueda)
print("Resultados de búsqueda avanzada:", resultados_avanzados)




#___________________________________________________________________________________________________________________________


#Desafío 2: Interfaz Gráfica
#Crear una interfaz gráfica simple usando tkinter que permita:
#Visualizar resultados en una tabla
#Búsqueda en tiempo real mientras se escribe
#Filtros dinámicos

#solución del desafío 2:



def interfaz_grafica_busqueda(productos):
    def buscar():
        termino = entrada_busqueda.get().lower()
        resultados = [p for p in productos if termino in p['nombre'].lower()]
        actualizar_tabla(resultados)

    def actualizar_tabla(resultados):
        for fila in tabla.get_children():
            tabla.delete(fila)
        for producto in resultados:
            tabla.insert('', 'end', values=(producto['id'], producto['nombre'], producto['marca'], producto['categoria'], producto['precio'], producto['stock']))

    ventana = tk.Tk()
    ventana.title("Búsqueda de Productos")

    etiqueta = tk.Label(ventana, text="Buscar Producto:")
    etiqueta.pack()

    entrada_busqueda = tk.Entry(ventana)
    entrada_busqueda.pack()
    entrada_busqueda.bind('<KeyRelease>', lambda event: buscar())

    tabla = ttk.Treeview(ventana, columns=('ID', 'Nombre', 'Marca', 'Categoría', 'Precio', 'Stock'), show='headings')
    for col in tabla['columns']:
        tabla.heading(col, text=col)
    tabla.pack()

    ventana.mainloop()
# Iniciar la interfaz gráfica
interfaz_grafica_busqueda(productos)
#___________________________________________________________________________________________________________________________



#Desafío 3: Persistencia de Datos
#Implementar:
#Guardar y cargar datos desde archivos JSON
#Historial de búsquedas realizadas
#Estadísticas de uso del sistema


import json
import time
from typing import Any, Dict, List, Union

# ---------- Utilidades base de JSON ----------

def _guardar_json(datos: Union[dict, list], archivo: str) -> None:
    """
    Guarda 'datos' en un archivo JSON con formato y UTF-8.
    """
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)


def _cargar_json(archivo: str, por_defecto: Union[dict, list]) -> Union[dict, list]:
    """
    Carga JSON desde 'archivo'. Si no existe o está corrupto, retorna 'por_defecto'.
    """
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Validación suave de tipo esperado (dict/list)
            if isinstance(por_defecto, dict) and not isinstance(data, dict):
                return por_defecto
            if isinstance(por_defecto, list) and not isinstance(data, list):
                return por_defecto
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return por_defecto


# ---------- Persistencia de productos (lista) ----------

def guardar_productos(productos: List[Dict[str, Any]], archivo: str = 'productos.json') -> None:
    """
    Guarda la lista de productos en JSON.
    """
    if not isinstance(productos, list):
        raise TypeError("productos debe ser una lista de diccionarios.")
    _guardar_json(productos, archivo)


def cargar_productos(archivo: str = 'productos.json') -> List[Dict[str, Any]]:
    """
    Carga la lista de productos desde JSON. Si no existe o está vacío/dañado, retorna lista vacía.
    """
    return _cargar_json(archivo, por_defecto=[])


# ---------- Historial de búsquedas (lista de registros) ----------

def guardar_historial(registro: Dict[str, Any], archivo: str = 'historial.json') -> None:
    """
    Agrega un registro de búsqueda al historial (archivo JSON tipo lista).
    Estructura sugerida de 'registro':
    {
        'timestamp': 'YYYY-MM-DD HH:MM:SS',
        'tipo': 'producto_por_nombre' | 'producto_por_categoria' | ...,
        'criterio': 'nombre' | 'categoria' | ...,
        'valor': 'iPhone 15',
        'resultados': 3
    }
    """
    if not isinstance(registro, dict):
        raise TypeError("registro debe ser un diccionario.")
    historial = _cargar_json(archivo, por_defecto=[])
    historial.append(registro)
    _guardar_json(historial, archivo)


def log_busqueda(tipo: str, criterio: str, valor: Any, encontrados: Union[List[Any], Any],
                 archivo_historial: str = 'historial.json') -> None:
    """
    Crea y guarda un registro de búsqueda estandarizado.
    - 'encontrados' puede ser lista, objeto único o None; se contabiliza con seguridad.
    """
    if isinstance(encontrados, list):
        num = len(encontrados)
    else:
        num = 1 if encontrados else 0

    registro = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'tipo': tipo,
        'criterio': criterio,
        'valor': valor,
        'resultados': num
    }
    guardar_historial(registro, archivo=archivo_historial)


def cargar_historial(archivo: str = 'historial.json') -> List[Dict[str, Any]]:
    """
    Retorna la lista de registros del historial (vacía si no existe).
    """
    return _cargar_json(archivo, por_defecto=[])


# ---------- Estadísticas de uso (diccionario acumulativo) ----------

def actualizar_estadisticas(evento: str, archivo: str = 'estadisticas.json') -> None:
    """
    Incrementa el contador de 'evento' en las estadísticas de uso.
    Eventos sugeridos: 'busquedas', 'productos_guardados', 'errores', etc.
    """
    if not isinstance(evento, str) or not evento:
        raise ValueError("evento debe ser un string no vacío.")

    stats = _cargar_json(archivo, por_defecto={})
    if not isinstance(stats, dict):
        stats = {}

    stats[evento] = int(stats.get(evento, 0)) + 1
    _guardar_json(stats, archivo)


def obtener_estadisticas(archivo: str = 'estadisticas.json') -> Dict[str, int]:
    """
    Retorna el diccionario de estadísticas (vacío si no existe).
    """
    data = _cargar_json(archivo, por_defecto={})
    # Normaliza valores a int
    if isinstance(data, dict):
        return {k: int(v) for k, v in data.items() if _es_entero(v)}
    return {}


def _es_entero(x: Any) -> bool:
    try:
        int(x)
        return True
    except (TypeError, ValueError):
        return False


# ---------- Hooks simples para integrar en tu menú / GUI ----------

def hook_busqueda(tipo: str, criterio: str, valor: Any, resultados: Union[List[Any], Any]) -> None:
    """
    Llama a este hook DESPUÉS de realizar cualquier búsqueda en tu sistema.
    Registra historial + suma estadística de 'busquedas'.
    Ejemplo:
        resultados = buscar_producto_por_nombre(productos, nombre)
        hook_busqueda('producto_por_nombre', 'nombre', nombre, resultados)
    """
    log_busqueda(tipo=tipo, criterio=criterio, valor=valor, encontrados=resultados)
    actualizar_estadisticas('busquedas')


def hook_guardado_productos(productos: List[Dict[str, Any]], archivo: str = 'productos.json') -> None:
    """
    Llama a este hook cuando el usuario elija guardar productos.
    Guarda JSON + suma estadística de 'productos_guardados'.
    """
    guardar_productos(productos, archivo=archivo)
    actualizar_estadisticas('productos_guardados')




if __name__ == '__main__':
    # Datos de ejemplo mínimos:
    productos = [
        {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Celulares', 'precio': 5000.0, 'stock': 3, 'disponible': True},
        {'id': 2, 'nombre': 'Galaxy S23', 'marca': 'Samsung', 'categoria': 'Celulares', 'precio': 4200.0, 'stock': 5, 'disponible': True},
        {'id': 3, 'nombre': 'ThinkPad E14', 'marca': 'Lenovo', 'categoria': 'Laptops', 'precio': 3800.0, 'stock': 2, 'disponible': True},
    ]

    # Guardar productos (persistencia):
    hook_guardado_productos(productos, archivo='productos.json')

    # Simular una búsqueda por nombre:
    nombre = 'Galaxy S23'
    encontrados = [p for p in productos if p['nombre'].lower() == nombre.lower()]
    hook_busqueda('producto_por_nombre', 'nombre', nombre, encontrados)

    # Simular otra búsqueda por categoría:
    categoria = 'Celulares'
    encontrados2 = [p for p in productos if p['categoria'].lower() == categoria.lower()]
    hook_busqueda('producto_por_categoria', 'categoria', categoria, encontrados2)

    # Mostrar historial y estadísticas:
    print("Historial (últimos registros):")
    for r in cargar_historial()[-5:]:
        print(r)

    print("\nEstadísticas:")
    print(obtener_estadisticas())






