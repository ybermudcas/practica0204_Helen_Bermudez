edad = 16
ingreso = 1000
edad_usuario = int(input("¿Cuál es tú edad?"))
ingreso_usuario = float(input("¿Cuál es tu ingreso mensual?"))

if edad_usuario + ingreso_usuario >=  edad  +  ingreso:
    print("El usuario tiene que tributar")

else:
    print("El usuario no cumple los requisitos necesarios para tributar")    