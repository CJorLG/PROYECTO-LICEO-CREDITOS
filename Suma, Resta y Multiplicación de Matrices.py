#The functions that allow show an arrays graphic representation
def array_A():
    print("Matriz A")
    print("--------------")
    print(a[0])
    print(a[1])
    print(a[2])
    print("\n")   
def array_B():
    print("Matriz B")
    print("--------------")
    print(b[0])
    print(b[1])
    print(b[2])
    print("\n")
def array_C():
    print("--------------")
    print(c[0])
    print(c[1])
    print(c[2])
    print("\n")
#The function that checks if the dimensions of the arrays are compatible
def len_Check():
    if len(a[0]) == len(b[0]):
        print("Se pueden operar las matrices, continua!")
    else:
        print("No se pueden operar estras matrices")
        iteration += 2
#The functions that are responsible for managing arrays operations
def array_addition():
    c[0][0] = a[0][0] + b[0][0]
    c[0][1] = a[0][1] + b[0][1]
    c[0][2] = a[0][2] + b[0][2]
    
    c[1][0] = a[1][0] + b[1][0]
    c[1][1] = a[1][1] + b[1][1]
    c[1][2] = a[1][2] + b[1][2]
    
    c[2][0] = a[2][0] + b[2][0]
    c[2][1] = a[2][1] + b[2][1]
    c[2][2] = a[2][2] + b[2][2]
def array_subtraction():
    
    b[0][0] = b[0][0] * -1
    b[0][1] = b[0][1] * -1
    b[0][2] = b[0][2] * -1
    
    b[1][0] = b[1][0] * -1
    b[1][1] = b[1][1] * -1
    b[1][2] = b[1][2] * -1
    
    b[2][0] = b[2][0] * -1
    b[2][1] = b[2][1] * -1
    b[2][2] = b[2][2] * -1
    
    c[0][0] = a[0][0] + b[0][0]
    c[0][1] = a[0][1] + b[0][1]
    c[0][2] = a[0][2] + b[0][2]
    
    c[1][0] = a[1][0] + b[1][0]
    c[1][1] = a[1][1] + b[1][1]
    c[1][2] = a[1][2] + b[1][2]
    
    c[2][0] = a[2][0] + b[2][0]
    c[2][1] = a[2][1] + b[2][1]
    c[2][2] = a[2][2] + b[2][2]
def array_multiplication():
    c[0][0] = (a[0][0] * b[0][0]) + (a[1][0] * b[0][1]) + (a[2][0] * b[0][2])
    c[0][1] = (a[0][0] * b[1][0]) + (a[1][0] * b[1][1]) + (a[2][0] * b[1][2])
    c[0][2] = (a[0][0] * b[2][0]) + (a[1][0] * b[2][1]) + (a[2][0] * b[2][2])
    
    c[1][0] = (a[0][1] * b[0][0]) + (a[1][1] * b[0][1]) + (a[2][1] * b[0][2])
    c[1][1] = (a[0][1] * b[1][0]) + (a[1][1] * b[1][1]) + (a[2][1] * b[1][2])
    c[1][2] = (a[0][1] * b[2][0]) + (a[1][1] * b[2][1]) + (a[2][1] * b[2][2])
    
    c[2][0] = (a[0][2] * b[0][0]) + (a[1][2] * b[0][1]) + (a[2][2] * b[0][2])
    c[2][1] = (a[0][2] * b[1][0]) + (a[1][2] * b[1][1]) + (a[2][2] * b[1][2])
    c[2][2] = (a[0][2] * b[2][0]) + (a[1][2] * b[2][1]) + (a[2][2] * b[2][2])

#Declaring an arrays
a = [[4, 2, 6], [5, 3, 7], [6, 4, 8]]
b = [[-3, -7, 3], [1, 6, -9], [4, 2, 7]]
c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
iteration = 0
while iteration < 1:
    try:
        array_A()
        array_B()
        len_Check()
        
        option = str(input("|| SUMAR (+) || RESTA (-) || MULTIPLICACIÓN (*) || \n"))
        if option == "+":
            array_addition()
            print("Matriz A+B")
            array_C()
            iteration += 2
        elif option == "-":
            array_subtraction()
            print("Matriz A-B")
            array_C()
            iteration += 2
        elif option == "*":
            array_multiplication()
            print("Matriz AxB")
            array_C()
            iteration += 2
            
    except ValueError:
        print("Ingresaste un dato inválido, vuelve a intentarlo")
    except ZeroDivisionError:
        print("Math Error")