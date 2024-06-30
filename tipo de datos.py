# Programa conversor de unidades
# Este programa permite convertir entre kilómetros y millas.

def convertir_km_a_millas(kilometros: float) -> float:
    """
    Convierte kilómetros a millas.

    :param kilometros: La distancia en kilómetros (float).
    :return: La distancia en millas (float).
    """
    millas = kilometros * 0.621371
    return millas


def convertir_millas_a_km(millas: float) -> float:
    """
    Convierte millas a kilómetros.

    :param millas: La distancia en millas (float).
    :return: La distancia en kilómetros (float).
    """
    kilometros = millas / 0.621371
    return kilometros


def main():
    while True:
        print("Conversor de unidades")
        print("1. Convertir kilómetros a millas")
        print("2. Convertir millas a kilómetros")
        print("3. Salir")

        # Solicitar la opción del usuario
        opcion = input("Seleccione una opción (1, 2, 3): ")

        if opcion == '1':
            km_input = input("Ingrese la distancia en kilómetros: ")
            try:
                kilometros = float(km_input)
                millas = convertir_km_a_millas(kilometros)
                print(f"{kilometros} kilómetros son {millas:.2f} millas.")
            except ValueError:
                print("Por favor, ingrese un número válido para la distancia en kilómetros.")

        elif opcion == '2':
            millas_input = input("Ingrese la distancia en millas: ")
            try:
                millas = float(millas_input)
                kilometros = convertir_millas_a_km(millas)
                print(f"{millas} millas son {kilometros:.2f} kilómetros.")
            except ValueError:
                print("Por favor, ingrese un número válido para la distancia en millas.")

        elif opcion == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor seleccione 1, 2 o 3.")


# Ejecución del programa principal
if "_main_":
    main()
