#retiro de cajero

usuario = list()

usuario.append("Jose Alejandro")
usuario.append("0485")
usuario.append("1000")

recibolista = list()
recibolista.append(["123",500])
recibolista.append(["456",100])

acciones = list()   
acciones.append("1. Retirar")

usuario2 = list()
usuario2.append("Juan Carlos")
usuario2.append("1234")
usuario2.append("500")

def registro():
    lista = list()
    user = input("Ingrese su nombre: ")
    PassWord = input("Ingrese su contraseña: ")

    lista.append(user)
    lista.append(PassWord)

    if usuario[0] == user and usuario[1] == PassWord:
        print("Bienvenido", usuario[0])
        return lista
    
    else:
        print("Usuario o contraseña incorrectos")
def oportunidad(registro):
    intentos = 0
    while intentos < 3:
        if registro() == usuario:
            return True
        else:
            intentos += 1
            print("Intentos restantes: ", 3 - intentos)
            esValido = registro()
            if esValido:
                return esValido
            else:
                intentos += 1

def operacion():
    seleccion = list()
    cantidadOperaciones = ""
    print("Seleccione la operación que desea realizar: ")
    print("1. Retirar")
    print("2.regresar")

    seleccion.append(input("Ingrese el número de la operación: "))

    if seleccion[0] == "1":
        print("Retiro")
        cantidadOperaciones = input("Ingrese la cantidad a retirar: ")
        seleccion.append(cantidadOperaciones)

    elif seleccion[0] == "2":
        print("Regresar")
        return registro()
    
    else:
        print("Opción no válida")
        return seleccion()
    
    return seleccion
def retiro(operacion):
    saldo = operacion()
    if(saldo[1] <= usuario[2]):
        usuario[2] = int(usuario[2]) - int(saldo[1])
        print("Retiro exitoso")
        print("Saldo restante: ", usuario[2])
        return True
    else:
        print("Saldo insuficiente")
        return False



