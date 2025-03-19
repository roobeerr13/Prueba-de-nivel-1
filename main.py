from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta
from lanzador import lanzador_main, catalogar


def mostrar_menu():
    """Muestra el menú de opciones."""
    print("Seleccione el tipo de vehículo:")
    print("1. Coche ")
    print("2. Bicicleta")
    print("3. Camioneta")
    print("4. Motocicleta")
    print("5. Ordenar por tipo de ruedas")
    print("6. Salir")

def obtener_datos_vehiculo(tipo):
    """Solicita datos del usuario y crea un vehículo según el tipo elegido."""
    if tipo == 1:
        # Datos para Coche
        color = input("Ingrese el color del coche: ")
        ruedas = int(input("Ingrese el número de ruedas del coche: "))
        velocidad = int(input("Ingrese la velocidad del coche (km/h): "))
        cilindrada = int(input("Ingrese la cilindrada del coche (cc): "))
        return Coche(color, ruedas, velocidad, cilindrada)
    elif tipo == 2:
        # Datos para Bicicleta
        color = input("Ingrese el color de la bicicleta: ")
        ruedas = int(input("Ingrese el número de ruedas de la bicicleta: "))
        marca = input("Ingrese la marca de la bicicleta: ")
        modelo = input("Ingrese el modelo de la bicicleta: ")
        tipo = input("Ingrese el tipo de la bicicleta (urbana/deportiva): ")
        return Bicicleta(color, ruedas, marca, modelo, tipo)
    elif tipo == 3:
        # Datos para Camioneta
        color = input("Ingrese el color de la camioneta: ")
        ruedas = int(input("Ingrese el número de ruedas de la camioneta: "))
        velocidad = int(input("Ingrese la velocidad de la camioneta (km/h): "))
        cilindrada = int(input("Ingrese la cilindrada de la camioneta (cc): "))
        marca = input("Ingrese la marca de la camioneta: ")
        modelo = input("Ingrese el modelo de la camioneta: ")
        carga = int(input("Ingrese la carga máxima de la camioneta (kg): "))
        return Camioneta(color, ruedas, velocidad, cilindrada, marca, modelo, carga)
    elif tipo == 4:
        # Datos para Motocicleta
        color = input("Ingrese el color de la motocicleta: ")
        ruedas = int(input("Ingrese el número de ruedas de la motocicleta: "))
        marca = input("Ingrese la marca de la motocicleta: ")
        modelo = input("Ingrese el modelo de la motocicleta: ")
        tipo = input("Ingrese el tipo de la motocicleta: ")
        velocidad = int(input("Ingrese la velocidad de la motocicleta (km/h): "))
        cilindrada = int(input("Ingrese la cilindrada de la motocicleta (cc): "))
        return Motocicleta(color, ruedas, marca, modelo, tipo, velocidad, cilindrada)
    elif tipo == 5:
        # Filtrar vehículos por número de ruedas
        ruedas = int(input("Ingrese el número de ruedas para filtrar: "))
        catalogar(vehiculos=[], ruedas=ruedas)
        return None
    else:
        return None


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 6:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        vehiculo = obtener_datos_vehiculo(opcion)
        if vehiculo:
            print(f"\nVehículo creado: {vehiculo}")
        else:
            print("\nOpción no válida o función finalizada. Intente de nuevo.\n")
    # Llama al lanzador principal al final del programa
    lanzador_main()
