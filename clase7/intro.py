"""
mensaje = "Hola"

def saludar():
    print(mensaje)

saludar()


def saludar():
    nombre = "Carlos"
    print(nombre)

saludar()

print(nombre)


def mostrar_nombre():
    nombre = "Ana"
    print(nombre)

mostrar_nombre()


def mostrar_nombre():
    nombre = "Ana"

mostrar_nombre()

print(nombre)


pais = "Colombia" # alcance global

def mostrar_pais():
    print(pais)

mostrar_pais()



contador = 0

def aumentar():
    global contador
    contador += 1

aumentar()

print(contador)
"""

contador = 0

def aumentar(local):
    local += 1
    return local


contador = aumentar(contador)


print(contador)


