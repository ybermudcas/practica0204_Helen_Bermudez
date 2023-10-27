contraseña = "contraseñahb21"
preguntacontraseña = input("Escribe una contraseña")

if preguntacontraseña.lower() != contraseña.lower():
    print("Contraseña incorrecta, inténtalo nuevamente")

else: 
    print("La contraseña es correcta")