#Calcular promedio de notas (con arreglos), con menú de opciones
notas=[]
opcion=0

while opcion!=3 :
    print("Ingrese una opción:")
    print("1. Ingresar Notas")
    print("2. Calcular Promedio")
    print("3. Salir")

    opcion=int(input()) 
    if opcion==1 :
        cantidad_notas = int(input("Ingrese la cantidad de notas: "))
        #Guardar notas de acuerdo a la cantidad en el arreglo "notas[]"
        for i in range(cantidad_notas):
            nota=float(input("Ingrese su nota: "))
            notas.append(nota)
        print("Sus notas han sidos guardadas correctamente...\n")
    elif opcion ==2 :
        #Calcular Promedio de las notas guardadas
        if len(notas) == 0 :
            print("Ingrese sus notas primero \n")
        else :
             promedio = sum(notas) / len(notas)
             print("Tu promedio es: ", promedio)
    elif opcion ==3 :
        #Salir
        print("Saliendo...")
    else:
        print("Ingrese una opción válida: \n")