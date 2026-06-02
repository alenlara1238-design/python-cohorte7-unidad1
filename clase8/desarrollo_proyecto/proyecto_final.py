def mostar_menu():
    """
        Muestra las opciones disponibles para el juego
    """
    print("\n=====La Cueva del Tesoro Perdido======")
    print("1. Explorar la cueva")
    print("2. Buscar tesoro")
    print("3. Descansar")
    print("4. Ver estado del aventurero")
    print("5. Salir")

def explorar(vida, nivel):
    """
        El aventurero explora la vueva.

        Parámetros:
        vida (int): vida actual del jugador
        nivel (int): nivel actual del jugador

        retorna: 
            Dos valores que son vida y nuevo nivel (tupla)
    """
    vida -= 10
    nivel += 1

    return vida, nivel

def buscar_tesoro(vida, oro):
    """ 
        El aventurero busca tesoro.

        Parámetros:
            vida(int): vida actual del jugador
            oro(int): cantidad actual de oro
        
        Retorna:
                Nueva vida y nueva cantidad de oro.(tupla --> vida, oro
    """
    oro += 20
    vida -= 5
    return vida, oro


def descansar(vida):
    """
        Recupera 15 puntos de vida del juegador.

        Parámetros:
            vida (int): vida actual del jugador
        Retorna:
            int: nueva cantidad de vida (+15)
    """
    vida += 15
    if(vida > 100):
        vida = 100
    return vida

def mostrar_estado(nombre, vida, oro, nivel):
    """
        Muestra la información actual del jugador.

        Parámetros:
            nombre (str): nombre del jugador
            vida (int): vida actual
            oro (int): cantidad de oro
            nivel (int): nivel actual
    """
    print(f"Nombre: {nombre}")
    print(f"Vida: {vida}")
    print(f"Oro: {oro}")
    print(f"Nivel: {nivel}")


def main():
    """
        Función principal del programa.

        Aquí se crearán las variables iniciales, 
        se ejectará el menú y se coordinará toda
        la lógica del juego
    """
    nombre = input("Ingrese el nombre del aventurero: ")
    vida = 100
    oro = 0
    nivel = 1
    
    jugando = True

    while jugando and vida > 0:

        mostar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
           vida, nivel = explorar(vida, nivel)

        elif opcion == "2":
           vida, oro = buscar_tesoro(vida, oro)

        elif opcion == "3":
           vida = descansar(vida)

        elif opcion == "4":
            mostrar_estado(nombre, vida, oro, nivel)

        elif opcion == "5":
            print("\nGracias por jugar!")
            jugando = False

        else:
            print("\nopción inválida.")
    
    if vida <= 0: # si el ciclo se acabó, preguntar si fue por vidas <= 0, y entonces mostrar GAME OVER:
        print("\nGAME OVER: Has caído en una cueva")
        print("\n=====RESUMEN DE LA AVENTURA=======")
        print(f"Nivel alcanzado: {nivel}")
        print(f"oro obtenido: {oro}")
# punto de arranque de la aplicación
main()


"""
    mejoras:
    1) cambia if-elif por:
        match opcion:
            case "1":
                instrucciones
            case "2":
                instrucciones
            
            case _:
                print("Opcion no válida")

        2) agregar mas acciones (opciones) 

        3) mostrar mensajes tras cada opción culminada
            ejemplo: explorando... usted ha perdido dos vidas
            
    """