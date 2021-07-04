def division(num1,num2):
    return num1/num2
def areadeltriangulo(base,altura):
    return base*altura/2
def areadelcuadrado(lado):
    return lado*lado

def menu():
    print("*********")
    print("*        MENU         *")
    print("1. Divison de dos numero")
    print("*2. Area del triangulo  *")
    print("*3. Area del cuadrado *")
    print("*4.      Salir        *")
    print("*********")
    
    opcion = int(input("Escoja la opcion: "))
    return opcion

opcion = menu()
while opcion != 4:
    if opcion == 1:
        print("Division entre dos numeros")
        num1 = int(input("ingrese el numero1: " ) )
        num2 = int(input("ingrese el numero 2: "))
        division = division(num1,num2)
        print("la diviom es: " + str(division) + "\n")
    elif opcion == 2:
        print("Calculo del area de un Triangulo")
        base = int(input("ingrese la base: " ) )
        altura = int(input("ingrese la altura: "))
        calculo = areadeltriangulo(base,altura)
        print("Area del triangulo: " + str(calculo) + "\n")
   
    elif opcion == 3:
       print("Calculo del area de un Cuadrado")
       lado = int(input("ingrese uno de los Lados: " ) )
       CalculoC = areadelcuadrado(lado)
       print("Area del Cuadrado es: " + str(CalculoC) + "\n")
    else:
        print("Opcion no valida\n")
    opcion = menu()