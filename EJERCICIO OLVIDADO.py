nombre = input("Escribe tu nombre")
sexo = input("Escribe tu sexo")

if (sexo.lower() == "femenino" and nombre.lower() < "m") + (sexo.lower() == "masculino" and nombre.lower() > "n"):
    print("Perteneces a la casa Gryffindor")

else:
    print("Perteneces a la casa de Slytherin")