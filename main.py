class Pez:
    def _init_(self, pez_boca, dientes, vive_rio, hembra, macho, orden_individuo, individuo_familia, familia_caracteristica, tipo_color, pez_tamaño):
        self.pez_boca = pez_boca
        self.dientes = dientes
        self.vive_rio = vive_rio
        self.hembra = hembra
        self.macho = machoeffffff
        self.orden_individuo = orden_individuo
        self.individuo_familia = individuo_familia
        self.familia_caracteristica = familia_caracteristica
        self.tipo_color = tipo_color
        self.pez_tamaño = pez_tamaño

def infer_fish_type(pez):
    #Regla 1
    if pez.pez_boca == "pequeña" and pez.dientes == "puntiagudos" and pez.vive_rio == "mundo":
        return "Ciprinodontiforme"
    
    #Regla 2
    if pez.orden_individuo == "Ciprinodontiforme" and pez.vive_rio == "America del Sur" and pez.macho == True:
        return "Poecilidos, la hembra es 3cm más grande que el macho"

    #Regla 3
    if pez.orden_individuo == "Ciprinodontiforme" and pez.vive_rio == "America del Sur" and pez.hembra == True:
        return "Poecílidos, el macho es 3cm mas pequeño que la hembra"

    #Regla 4
    if pez.individuo_familia == "poecílidos" and pez.familia_caracteristica == "manchas":
        return "Gambusia Affinis"

    #Regla 5
    if pez.individuo_familia == "poecílidos" and pez.tipo_color == "gris" and pez.familia_caracteristica == "rayas verdes":
        return "Gambusia Puntacta"

    #Regla 6
    if pez.pez_tamaño == "medio" and pez.dientes == "puntiagudos" and pez.vive_rio == "mundo" and pez.familia_caracteristica == "canales":
        return "Anabatidos"

    #Regla 7
    if pez.orden_individuo == "Anabatidos" and pez.tipo_color == "azul" and pez.familia_caracteristica == "rayas rojas" and pez.vive_rio == "Asia":
        return "Luchadores de Sian"

    #Regla 8
    if pez.orden_individuo == "Anabatidos" and pez.pez_tamaño == 25 and pez.familia_caracteristica == "sin rayas":
        return "Perca Trepadora"

    #Regla 9
    if pez.pez_boca == "pequeña" and pez.vive_rio == "mundo" and pez.familia_caracteristica == "cola redondeada":
        return "Ciclidos"

    #Regla 10
    if pez.orden_individuo == "Ciclidos" and pez.vive_rio == "Africa" and pez.tipo_color == "rojo" and pez.familia_caracteristica == "manchas negras":
        return "Pez Joya"

    return "No se pudo clasificar"

# Ejemplo de uso 1
pez_seleccion = Pez(pez_boca = "pequeña", dientes = "puntiagudos", vive_rio = "mundo", hembra = "", macho = "", orden_individuo = "", individuo_familia = "", familia_caracteristica = "", tipo_color = "", pez_tamaño = "")
print("El pez pertenece al orden de los: ", infer_fish_type(pez_seleccion))

# Ejemplo de uso 2
pez_seleccion = Pez(pez_boca = "pequeña", dientes = "puntiagudos", vive_rio = "America del Sur", hembra = "", macho = True, orden_individuo = "Ciprinodontiforme", individuo_familia = "", familia_caracteristica = "", tipo_color = "", pez_tamaño = "")
print("El pez pertenece a la familia de los: ", infer_fish_type(pez_seleccion))

# Ejemplo de uso 3
pez_seleccion = Pez(pez_boca = "pequeña", dientes = "puntiagudos", vive_rio = "America del Sur", hembra = True, macho = "", orden_individuo = "Ciprinodontiforme", individuo_familia = "", familia_caracteristica = "", tipo_color = "", pez_tamaño = "")
print("El pez pertenece a la familia de los: ", infer_fish_type(pez_seleccion))

# Ejemplo de uso 4
pez_seleccion = Pez(pez_boca = "", dientes = "", vive_rio = "", hembra = "", macho = "", orden_individuo = "", individuo_familia = "poecílidos", familia_caracteristica = "manchas", tipo_color = "", pez_tamaño = "")
print("La raza del pez es: ", infer_fish_type(pez_seleccion))

# Ejemplo de uso 5
pez_seleccion = Pez(pez_boca = "", dientes = "", vive_rio = "", hembra = "", macho = "", orden_individuo = "", individuo_familia = "poecílidos", familia_caracteristica = "rayas verdes", tipo_color = "gris", pez_tamaño = "")
print("La raza del pez es: ", infer_fish_type(pez_seleccion))

# Ejemplo de uso 6
pez_seleccion = Pez(pez_boca = "", dientes = "puntiagudos", vive_rio = "mundo", hembra = "", macho="", orden_individuo="", individuo_familia="", familia_caracteristica="canales", tipo_color="", pez_tamaño = "medio")
print("El pez pertenece al orden de los: ", infer_fish_type(pez_seleccion))

# Ejemplo de uso 7
pez_seleccion = Pez(pez_boca = "", dientes = "", vive_rio = "Asia", hembra = "", macho = "", orden_individuo = "Anabatidos", individuo_familia = "", familia_caracteristica = "rayas rojas", tipo_color = "azul", pez_tamaño = "")
print("El pez pertenece a la raza: ", infer_fish_type(pez_seleccion))

# Ejemplo de uso 8
pez_seleccion = Pez(pez_boca = "", dientes = "", vive_rio = "", hembra = "", macho = "", orden_individuo = "Anabatidos", individuo_familia = "", familia_caracteristica = "sin rayas", tipo_color = "", pez_tamaño = 25)
print("El pez pertenece a la raza: ", infer_fish_type(pez_seleccion))

# Ejemplo de uso 9
pez_seleccion = Pez(pez_boca = "pequeña", dientes = "", vive_rio = "mundo", hembra = "", macho = "", orden_individuo = "", individuo_familia = "", familia_caracteristica = "cola redondeada", tipo_color = "", pez_tamaño = "")
print("El pez pertenece al orden de los: ", infer_fish_type(pez_seleccion))

# Ejemplo de uso 10
pez_seleccion = Pez(pez_boca = "", dientes = "", vive_rio = "Africa", hembra = "", macho = "", orden_individuo = "Ciclidos", individuo_familia = "", familia_caracteristica = "manchas negras", tipo_color = "rojo", pez_tamaño = "")
print("La especie del pez es: ", infer_fish_type(pez_seleccion))