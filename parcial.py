#Fecha: 09/10
#Alumno: Leonel Maximiliano Gadea
#Division: 115

def perfil_pacientes():
    """

    |Funcion que carga los datos de los prticipantes
    |Le solicita al usuario que ingrese la cantidad de pacientes que quiera registrar
    Despues dentro de un bucle que se limita en la cantidad de pacientes ingresados pide estos datos:
    - Numero de historia clinica (int)
    - Nombre del paciente (str)
    - Edad del paciente (int)
    - Diagnostico del paciente (str)
    - Dias de internacion del paciente (int)
    |La informacion de los pacientes se guarda en una lista (pacientes) la cual retorna
    
    """
    pacientes = []
    cantidad_pacientes = int(input("Ingrese la cantidad de pacientes: "))
    for _ in range(cantidad_pacientes):
        historia_clinica = int(input("Ingrese el número de historia clínica: "))
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        diagnostico = input("Ingrese el diagnóstico del paciente: ")
        dias_internacion = int(input("Ingrese los días de internación del paciente: "))
        pacientes.append([historia_clinica, nombre, edad, diagnostico, dias_internacion])
    return pacientes

def mostrar_pacientes(pacientes):
    """

    |Funcion que nos muestra la lista de los pacientes ingresados
    |Si esta lista esta vacia muestra el mensaje indicando que no hay pacientes registrados
    |Si hay listas guardadas, muestra los datos dentro de esa lista

    Argumentos:
    pacientes (list) : lista de pacientes
    
    """
    if not pacientes:
        print("No hay pacientes registrados")
        return
    print("Lista de pacientes:")
    for paciente in pacientes:
        print(f"Historia Clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Días de internación: {paciente[4]}")

def buscar_paciente(pacientes, historia_clinica):
    """

    |Funcion para buscar a los pacientes por su historia clinica
    |Este recibe el numero de la historia clinica y recorre la lista de paciente para encontrarlo, si lo encuentra imprime los datos del paciente, de lo contrario no retorna ningun valor

    Argumentos:
    pacientes (list): lista de pacientes
    historia_clinica (int): numero de historia clinica que se busca

    """
    for paciente in pacientes:
        if paciente[0] == historia_clinica:
            print(f"Paciente encontrado: Historia Clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Días de internación: {paciente[4]}")
            return paciente
    return None

def ordenar_pacientes(pacientes):
    """

    |Funcion que ordena los pacientes por numero de historia clinica de menor a mayor
    |Utiliza un algoritmo que ordena la lista de pacientes en funcion del numero de historia clinica

    Argumentos: 
    pacientes(list): lista de pacientes
    
    retorno:
    list: Lista de pacientes ordenada por el numero de l ahistoria clinica
    
    """
    for i in range(len(pacientes)):
        for j in range(0, len(pacientes) - i - 1):
            if pacientes[j][0] > pacientes[j + 1][0]:
                pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]
    print("Pacientes ordenados por número de Historia Clínica: ")
    for paciente in pacientes:
        print(f"Historia Clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Días de internación: {paciente[4]}")
    return pacientes

def paciente_menor_dia_internacion(pacientes):
    """

    |Funcion que encuentra al paciente con menor cantidad de dias de internacion
    |Recorre la lista de pacientes comparando los dias de internacion, si encuentra al paciente con menos dias de internacion, actualiza el valor minimo.

    Argumentos:
    pacientes (list): Lista de pacientes
    
    """
    if not pacientes:
        print("No hay pacientes registrados")
        return
    paciente_menor_dia_internacion = pacientes[0]
    for paciente in pacientes:
        if paciente[4] < paciente_menor_dia_internacion[4]:
            paciente_menor_dia_internacion = paciente
    print(f"El paciente con menos dias de internacion es: Historia Clínica: {paciente_menor_dia_internacion[0]}, Nombre: {paciente_menor_dia_internacion[1]},Edad: {paciente_menor_dia_internacion[2]}, Diagnóstico: {paciente_menor_dia_internacion[3]} Días de internación: {paciente_menor_dia_internacion[4]}")

def paciente_mayor_dia_internacion(pacientes):
    """
    
    |Funcion que encuentra al paciente con mayor cantidad de dias de internacion
    |Recorre la lista de pacientes comparando los dias de internacion, si encuentra al paciente con mayor dias de internacion, actualiza el valor maximo.

    Argumentos:
    pacientes (list): Lista de pacientes
    
    """
    if not pacientes:
        print("No hay pacientes registrados")
        return
    paciente_mayor_dia_internacion = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > paciente_mayor_dia_internacion[4]:
            paciente_mayor_dia_internacion = paciente
    print(f"El paciente con mas dias de internacion es: Historia Clínica: {paciente_mayor_dia_internacion[0]}, Nombre: {paciente_mayor_dia_internacion[1]},Edad: {paciente_mayor_dia_internacion[2]}, Diagnóstico: {paciente_mayor_dia_internacion[3]} Días de internación: {paciente_mayor_dia_internacion[4]}")

def cantidad_pacientes_mas_5_dias (pacientes):
    """
    
    |Funcion para contar cuantos pacientes tienen mas de 5 dias de internacion 
    |Recorre la lista de pacientes , registrando en el contador cuantos tienen mas de 5 dias de internacion

    Argumentos:
    pacientes(list): Lista de pacientes
    
    """
    if not pacientes:
        print("No hay pacientes registrados")
        return
    contador = 0

    for paciente in pacientes:
        if paciente[4] > 5:
            contador += 1
    print (f"Cantidad de pacientes con mas de 5 dias de internacion: {contador}")

def promedio_dias_internacion(pacientes):
    """

    |Funcion que calcula el promedio de dias de internacion de todos los pacientes registrados
    |Suma los dias de internacion de los participantes y calcula el promedio representado en entero

    Argumentos:
    pacientes (list): Lista de pacientes
    
    """
    if not pacientes:
        print ("No hay pacientes registrados")
        return
    total_dias = 0
    cantidad_pacientes = len(pacientes)
    for paciente in pacientes:
        total_dias +=paciente[4]
    promedio = int (total_dias / cantidad_pacientes)
    print (f"El promedio de dias de internacion es: {promedio}")

def menu():
    salir = ""

    while salir != "salir":
        print("\nClinica 'La fuerza'")
        print("1. Cargar pacientes")
        print("2. Mostrar todos los pacientes")
        print("3. Buscar pacientes por numero de Historia Clinica")
        print("4. Ordenar pacientes por numero de historia clinica ")
        print("5. Mostrar paciente con mas dias de internacion")
        print("6. Mostrar paciente con menos dias de internacion")
        print("7. Cantidad de pacientes con mas de 5 dias de internacion")
        print("8. Promedios de dias de internacion de todos los pacientes")
        print("9. Salir")
        opcion = input("Seleccione una opcion: ")
    
    
        if opcion == "1":
            pacientes = perfil_pacientes()
        elif opcion == "2":
            mostrar_pacientes(pacientes)
        elif opcion == "3":
            historia_clinica = int(input("Ingrese el número de Historia Clínica: "))
            buscar_paciente(pacientes, historia_clinica)
        elif opcion == "4":
            ordenar_pacientes(pacientes)
        elif opcion == "5":
            paciente_mayor_dia_internacion(pacientes)
        elif opcion == "6":
            paciente_menor_dia_internacion(pacientes)
        elif opcion == "7":
            cantidad_pacientes_mas_5_dias(pacientes)
        elif opcion == "8":
            promedio_dias_internacion(pacientes)
        elif opcion == "9":
            print("Saliste del menu de la clinica, Gracias por su atencion y elegirnos!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()