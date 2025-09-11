import classLiga as CL
import classEquipo as CE
import classCopa as CC
import json
import os
import sys

# Para cargar datos del archivo
with open("equipos.json", "r") as listaEquipos:
    equiposCargados = json.load(listaEquipos)
    listaPrimera = [CE.Equipo(**equipo) for equipo in equiposCargados[0]]
    listaSegunda = [CE.Equipo(**equipo) for equipo in equiposCargados[1]]
    listaDeCampeones = [CE.Equipo(**equipo) for equipo in equiposCargados[2]]
    temporada = equiposCargados[3][0]
    del equiposCargados

exo = CL.Confederacion(
    listaPrimeraDiv = listaPrimera,
    listaSegundaDiv = listaSegunda
)

copaInternacional = CC.Copa(
    participantes = listaDeCampeones
)

# El programa
def guardar():
    global temporada
    listaPrimeraJ = [equipo.dict() for equipo in exo.participantesDeLigaPrimera()]
    listaSegundaJ = [equipo.dict() for equipo in exo.participantesDeLigaSegunda()]
    listaDeCampeonesJ = [equipo.dict() for equipo in campeonesSinEquiposDePrimera() + exo.getClasificadosInternacionales()]
    temporada += 1

    with open("equipos.json", "w") as listaEquipos:
        json.dump([listaPrimeraJ, listaSegundaJ, listaDeCampeonesJ, [temporada]], listaEquipos, indent = 4)

def registrarCampeones():
    with open("ligas/Campeones.txt", "a", encoding = "utf-8") as archivo:
        sys.stdout = archivo
        print(f"Temporada {temporada}:")
        print(f"🥇 - {exo.nombreDelCampeonLigaPrimera()}")
        print(f"🏆 - {exo.nombreDelCampeonCopaPrimera()}")
        print(f"🥈 - {exo.nombreDelCampeonLigaSegunda()}")
        print(f"🔔 - {exo.nombreDelCampeonCopaSegunda()}")
        print(f"⭐ - {copaInternacional.campeon().nombre()}")
        print("")
    sys.stdout = sys.__stdout__

def campeonesSinEquiposDePrimera():
    datosDeCampeones = set([equipo.nombre() for equipo in listaDeCampeones])
    datosListaPrimera = set([equipo.nombre() for equipo in exo.participantesDeLigaPrimera()])
    datosListaSegunda = set([equipo.nombre() for equipo in exo.participantesDeLigaSegunda()])
    campeonesSinEquiposDePrimera = (datosDeCampeones - datosListaPrimera) - datosListaSegunda
    return [CE.Equipo(nombre = equipo) for equipo in campeonesSinEquiposDePrimera]

def jugarGuardando():
    exo.jugarTodasLasCompeticionesGuardando(temporada)
    copaInternacional.jugarCopaGuardandoResultados("ligas/Copa_Internacional_Resultados.txt", temporada)
    registrarCampeones()
    guardar()

def main():
    opcion = ""
    print("Bienvenido a juegoLigas. Puedes guardar una simulación o solo imprimirla, ¿qué será?")
    while True:
        print("1: Jugar ligas y guardar")
        print("2: Jugar ligas pero solo imprimirlas")
        print("3: Salir y cerrar esta ventana")
        opcion = input("Ingrese el número de alguna de las opciones: ")
        if(opcion == "1"):
            jugarGuardando()
            os.startfile(r"ligas/")
            input("Simulación terminada, ingrese cualquier tecla para continuar: ")
            break
        elif(opcion == "2"):
            exo.jugarTodasLasCompeticionesImprimiendo(temporada)
            input("Simulación terminada, ingrese cualquier tecla para continuar: ")
        elif(opcion == "3"):
            break
        else: 
            print("La opción seleccionada no es válida. Por favor, ingrese alguna de las opciones:")
            print("")

main()

"""
Primero, qué es lo que que quiero hacer?

main
tengo que crear ubna liga asi puedo añladir equipos
    podes agregar equipos
        tengo que fijarme si funciona como deberia la opcion para agregar equipos (ya creada, ni estaba) 
        tengo que ver si no se rompre al agregar equipos impares (no rompre, pero no funca como debería)
        por ahora solo deja poner ligas impares
podes simular
podes guardar
    guardo lo simulado o cómo?
    guardo los equipos?
podes agregar una liga
    necesario para poder empear la simlucion
podes agregar copa interancional
    como, fijándote en cuantas ligas tenés?

ideas
peudo organizar las ligas poniendolas en un array, y los equipos dentro de ellas


1 = ver resumen
2 = eidtar ligas
    1 = crear liga
    2 = añadir equipo a liga
    3 = eliminar equipo de liga
3 = simular 
4 = guardar datos
5 = salir



"""