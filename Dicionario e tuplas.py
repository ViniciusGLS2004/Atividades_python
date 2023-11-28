senai_coordenadas = (-12.230911723020084, -38.96932495887464)

print(type(senai_coordenadas))
print(senai_coordenadas)

ids = id(senai_coordenadas)
print("ID da tuple:\n ", ids)

senai_coordenadas += (-5,)
print(senai_coordenadas)

senai_coordenadas[0] += 1
print(senai_coordenadas)

emails_gerentes = {
    "iguatemi": "iguatemi@gmail.com",
    "plaza": "plaza@gmail.com",
    "Barra": "barra@gmail.com"
}

email = emails_gerentes['Barra']
print(email)

