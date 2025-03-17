#Crear diccionario para el perfil
perfil = {
    "Nombre" : "Santiago",
    "Edad" : 18,
    "Ciudad" : "Pivijay",
    "Amigos" : [{"Nombre" : "Yesid", "Tiempoamistad" : "6"}, {"Nombre" : "Mateo", "Tiempoamistad" : "4"},
                {"Nombre" : "Camilo", "Tiempoamistad" : "12"}],
    "Post" : [{"Contenido" : "Me gusta la salchipapa", "Likes" : "700", "Comentarios": "A mi tambien me gusta"}]
}

#Agregar nuevo post
nuevo_post = {
    "Comentarios": [{"Contenido" : "Me gusta el futbol", "Likes" : "200", "Comentarios" : "A mi no"}]
}
perfil["Post"].append(nuevo_post)

#Modificar la ciudad
perfil["Ciudad"] = "Canada"

#Eliminar a un amigo
del perfil["Amigos"][1]

#Mostrar datos en pantalla
print("Perfil")
print(f"Nombre:", perfil["Nombre"])
print(f"Edad:", perfil["Edad"])
print(f"Ciudad:", perfil["Ciudad"])
print(f"Amigos {perfil['Amigos']}")
print(f"Post: {perfil['Post']}")