from Crucero import Crucero  # Importo la Clase Crucero
import requests

cruceros = []

def inicializar_cruceros():                 # Método para inicializar cruceros
    global cruceros
    api_response = requests.get('https://saman-caribbean.vercel.app/api/cruise-ships')
    '''
    api_response = [
        {
            "name": "El Dios de los Mares",
            "route": [
                "Fort Lauderdale",
                "Bahamas",
                "St. Thomas",
                "Islas Vírgenes",
                "Fort Lauderdale"
            ],
            "departure": "2020-12-20T00:00:00.000Z",
            "cost": {
                "simple": 69.99,
                "premium": 89.99,
                "vip": 129.99
            },
            "rooms": {
                "simple": [
                    4,
                    10
                ],
                "premium": [
                    3,
                    9
                ],
                "vip": [
                    1,
                    6
                ]
            },
            "capacity": {
                "simple": 2,
                "premium": 4,
                "vip": 8
            },
            "sells": [
                {
                    "name": "Coca Cola",
                    "price": 3.99,
                    "amount": 500
                },
                {
                    "name": "Pizza",
                    "price": 11.99,
                    "amount": 230
                },
                {
                    "name": "Hamburguesa",
                    "price": 25.99,
                    "amount": 250
                },
                {
                    "name": "Hamburguesa & Refresco",
                    "price": 19.99,
                    "amount": 250
                },
                {
                    "name": "Ron",
                    "price": 6.99,
                    "amount": 300
                }
            ]
        },
        {
            "name": "La Reina Isabel",
            "route": [
                "Barbados",
                "Bahamas",
                "Aruba",
                "Curaçao",
                "Santa Lucia",
                "Barbados"
            ],
            "departure": "2020-12-21T00:00:00.000Z",
            "cost": {
                "simple": 59.99,
                "premium": 99.99,
                "vip": 119.99
            },
            "rooms": {
                "simple": [
                    6,
                    10
                ],
                "premium": [
                    4,
                    8
                ],
                "vip": [
                    2,
                    4
                ]
            },
            "capacity": {
                "simple": 2,
                "premium": 4,
                "vip": 8
            },
            "sells": [
                {
                    "name": "Coca Cola",
                    "price": 5.99,
                    "amount": 100
                },
                {
                    "name": "Pasta",
                    "price": 12.99,
                    "amount": 150
                },
                {
                    "name": "Hamburguesa",
                    "price": 13.99,
                    "amount": 230
                },
                {
                    "name": "Donas",
                    "price": 2.99,
                    "amount": 110
                },
                {
                    "name": "Ron",
                    "price": 11.99,
                    "amount": 250
                }
            ]
        },
        {
            "name": "El Libertador del Océano",
            "route": [
                "Miami",
                "Bahamas",
                "Puerto Rico",
                "Haití",
                "República Dominicana",
                "Miami"
            ],
            "departure": "2020-12-17T00:00:00.000Z",
            "cost": {
                "simple": 49.99,
                "premium": 89.99,
                "vip": 139.99
            },
            "rooms": {
                "simple": [
                    6,
                    8
                ],
                "premium": [
                    4,
                    6
                ],
                "vip": [
                    4,
                    2
                ]
            },
            "capacity": {
                "simple": 3,
                "premium": 5,
                "vip": 12
            },
            "sells": [
                {
                    "name": "Coca Cola",
                    "price": 2.99,
                    "amount": 150
                },
                {
                    "name": "Pizza",
                    "price": 11.99,
                    "amount": 230
                },
                {
                    "name": "Hamburguesa",
                    "price": 16.99,
                    "amount": 200
                },
                {
                    "name": "Cerveza",
                    "price": 3.99,
                    "amount": 180
                },
                {
                    "name": "Cofuta & Refresco",
                    "price": 11.99,
                    "amount": 150
                }
            ]
        },
        {
            "name": "Sabas Nieves",
            "route": [
                "Galveston",
                "Cozumel",
                "Haití",
                "Jamaica",
                "Panamá",
                "Galveston"
            ],
            "departure": "2020-12-19T00:00:00.000Z",
            "cost": {
                "simple": 59.99,
                "premium": 99.99,
                "vip": 119.99
            },
            "rooms": {
                "simple": [
                    4,
                    12
                ],
                "premium": [
                    3,
                    7
                ],
                "vip": [
                    2,
                    4
                ]
            },
            "capacity": {
                "simple": 3,
                "premium": 5,
                "vip": 10
            },
            "sells": [
                {
                    "name": "Coca Cola",
                    "price": 5.99,
                    "amount": 100
                },
                {
                    "name": "Pizza",
                    "price": 12.99,
                    "amount": 130
                },
                {
                    "name": "Hamburguesa",
                    "price": 15.99,
                    "amount": 260
                },
                {
                    "name": "Cofuta",
                    "price": 6.99,
                    "amount": 150
                },
                {
                    "name": "Cofuta & Refresco",
                    "price": 12.99,
                    "amount": 350
                }
            ]
        }
    ]'''
    lista = api_response.json()
    for elemento in lista:
        cruceros.append(Crucero(elemento))
    
    #cruceros = api_response.json()


def menu_principal():  # El menú principal de las acciones que se puede realizar dentro del crucero
    print("BIENVENIDOS A LA COMPAÑIA SAMÁN CARIBBEAN ")
    print("MENÚ PRINCIPAL")
    print('''
    1. Gestion de cruceros
    2. Gestión de habitaciones 
    3. Venta de tours
    4. Gestión de restaurante
    5. Estadísticas
    6. Salir ''')
    while True:
        opcion = int(input("Su opción es: "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Opción inválida")


def menu_habitaciones():  # Método del menú principal de las acciones que se puede realizar dentro del crucero

    print("\nGestion de habitaciones")
    print('''
    1. Mostrar habitaciones
    2. Vender habitación 
    3. Desocupar habitación
    4. Buscar habitación
    5. Guardar en archivo
    6. Volver al menu principal ''')
    while True:
        opcion = int(input("Su opción es: "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Opción inválida")


def gestion_cruceros():  # Método de Gestión de Cruceros
    for crucero in cruceros:
        print(crucero)


def mostar_habitaciones():          # Método para mostrar habitación
    opcion = seleccionar_crucero()
    cruceros[opcion].mostrar_habitaciones(0)
    cruceros[opcion].mostrar_habitaciones(1)
    cruceros[opcion].mostrar_habitaciones(2)

def seleccionar_crucero():          # Método para seleccionar crucero
    for indice in range(len(cruceros)):
        print(str(indice + 1) + "- " + cruceros[indice].info_menu())
    opcion = int(input("Seleccione el barco que desea ver: "))

    while not 1 <= opcion <= len(cruceros):
        print("Su opción es inválida")
        opcion = int(input("Seleccione el barco que desea ver: "))
    return opcion-1

def crucero_por_barco():        # Método de crucero por barco
    opcion = seleccionar_crucero()
    print(cruceros[opcion])


def crucero_por_destino():      # Método de crucero por destino
    destino = input("Ingrese el destino: ")
    for indice in range(len(cruceros)):
        if cruceros[indice].contiene_destino(destino):
            return indice


def vender_habitacion():    # Método para vender la habitación
    # Se pregunta si la compra es en base al barco o al destino
    print('''Seleccione
    1- Si desea buscar por barco
    2- Si desea buscar por destino
    0- Regresar''')
    opcion = int(input("Su opción: "))

    while not 0 <= opcion <= 2:
        print("Su opción es inválida")
        opcion = int(input("Su opción: "))
    indice = 0
    if opcion == 1:
        indice = seleccionar_crucero()
    else:
        indice = crucero_por_destino()

    cruceros[indice].vender_habitacion()


def desocupar_habitacion():             # Método para desocupar la habitación
    indice = seleccionar_crucero()
    habitacion = cruceros[indice].buscar_habitacion_nro()
    cruceros[indice].vaciar_habitacion(habitacion)


def buscar_habitacion():                 # Método para buscar la habitación
    indice = seleccionar_crucero()
    print('''Seleccione un filtro de búsqueda
    1- Tipo de habitacion
    2- Capacidad de habitación
    3- Tipo + Pasillo + Numero
    4- Cancelar''')
    opcion = int(input("Su opción: "))
    while not(1 <= opcion <= 4):
        print("Opción inválida")
        opcion = int(input("Su opción: "))
    if opcion == 1:
        piso = cruceros[indice].buscar_habitacion_tipo()
        piso.info_pasillos()
    elif opcion == 2:
        piso = cruceros[indice].buscar_habitacion_capacidad()
        piso.info_pasillos()
    elif opcion == 3:
        habitacion = cruceros[indice].buscar_habitacion_nro()
        print(habitacion.informacion())

def guardar_archivo():                  
    pass #todo guardar el archivo


def gestion_habitaciones():          # Método de gestión de habitación
    opcion = menu_habitaciones()
    while opcion != 6:
        if opcion == 1:
            mostar_habitaciones()
        elif opcion == 2:
            vender_habitacion()
        elif opcion == 3:
            desocupar_habitacion()
        elif opcion == 4:
            buscar_habitacion()
        elif opcion == 5:
            guardar_archivo()
        opcion = menu_habitaciones()


def ventas_tour():                       # Método de ventas tour
    indice = seleccionar_crucero()
    cruceros[indice].vender_tour()


def gestion_restaurante():               # Método de gestión restaurante
    indice = seleccionar_crucero()
    cruceros[indice].administrar_restaurante()


def gastos_clientes():                   # Método de los gastos de los clientes
    total = 0.0
    cantidad = 0
    for crucero in cruceros:
        promedio_crucero = crucero.promedio_gasto()
        total += promedio_crucero
        cantidad += len(crucero.clientes)
        if cantidad == 0:
            return 0
        else:
            return total/cantidad


def clientes_sin_tour():                 # Método de clientes sin tour
    clientes_tour = 0
    total_clientes=0
    for crucero in cruceros:
        clientes_tour += crucero.clientes_sin_tour()
        total_clientes += len(crucero.clientes)
        porcentaje = 0
        if total_clientes != 0:
            porcentaje = clientes_tour*100/total_clientes
    return porcentaje


def top_clientes():                      # Método de top clientes
    top = []
    for crucero in cruceros:
        top += crucero.top_clientes()

    ordenados = sorted(top, key=lambda cliente : cliente[1], reverse=True)
    return ordenados[0:3]


def top_cruceros():                      # Método de top cruceros
    top = []
    for crucero in cruceros:
        info = (crucero, len(crucero.ventas_cruceero))
        top.append(info)
    ordenados = sorted(top, key=lambda crucero : crucero[1], reverse=True)
    texto = ''
    for ord in ordenados[0:3]:
        texto += str(ord[0])
    return texto



def top_productos():                    # Método de top productos
    top = []
    for crucero in cruceros:
        top += crucero.top_productos()

    ordenados = sorted(top, key=lambda producto : producto[1], reverse=True)
    return ordenados[0:3]


def estadisticas():                 # Método de estadísticas
    print('''ESTADISTICAS
    Promedio de gastos de un cliente: {}
    Porcentaje de clientes que no compran tours: {}
    Top 3 clientes con mayor fidelidad: {}
    Top 3 cruceros con más ventas de tickets: {}
    Top 5 productos más vendidos: {}
    '''.format(gastos_clientes(), clientes_sin_tour(), top_clientes(),top_cruceros(),top_productos()))


def main():
    inicializar_cruceros()
    opcion = menu_principal()
    while opcion != 6:
        if opcion == 1:
            gestion_cruceros()
        elif opcion == 2:
            gestion_habitaciones()
        elif opcion == 3:
            ventas_tour()
        elif opcion == 4:
            gestion_restaurante()
        elif opcion == 5:
            estadisticas()
        opcion = menu_principal()
    print("HASTA LUEGO, MUCHAS GRACIAS")


main()
