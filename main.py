from random import randint
import classLiga as CL
import classEquipo as CE
import classCopa as CC
import json
import os
import sys

# Para cargar datos del archivo de los equipos
with open("equipos.json", "r") as listaEquipos:
    equiposCargados = json.load(listaEquipos)
    nortePrimera = [CE.Equipo(**equipo) for equipo in equiposCargados[0]]
    norteSegunda = [CE.Equipo(**equipo) for equipo in equiposCargados[1]]
    estePrimera = [CE.Equipo(**equipo) for equipo in equiposCargados[2]]
    surPrimera = [CE.Equipo(**equipo) for equipo in equiposCargados[3]]
    oestePrimera = [CE.Equipo(**equipo) for equipo in equiposCargados[4]]
    listaDeCampeones = [CE.Equipo(**equipo) for equipo in equiposCargados[5]]
    temporada = equiposCargados[6][0]
    del equiposCargados

confederacionNorte = CL.Confederacion(
    listaPrimeraDiv = nortePrimera,
    listaSegundaDiv = norteSegunda
)

ligaEste = CL.Confederacion(listaPrimeraDiv = estePrimera)

ligaSur = CL.Confederacion(listaPrimeraDiv = surPrimera)

ligaOeste = CL.Confederacion(listaPrimeraDiv = oestePrimera)

copaInternacional = CC.Copa(
    participantes = listaDeCampeones
)

# El programa
def guardar():
    global temporada
    nortePrimeraDict = [equipo.dict() for equipo in confederacionNorte.participantesDeLigaPrimera()]
    norteSegundaDict = [equipo.dict() for equipo in confederacionNorte.participantesDeLigaSegunda()]
    ligaEsteDict = [equipo.dict() for equipo in ligaEste.ligaPrimera.participantes()]
    ligaSurDict = [equipo.dict() for equipo in ligaSur.ligaPrimera.participantes()]
    ligaOesteDict = [equipo.dict() for equipo in ligaOeste.ligaPrimera.participantes()]
    listaDeCampeonesDict = [equipo.dict() for equipo in clasificadosACopaInternacional()]
    temporada += 1

    with open("equipos.json", "w") as listaEquipos:
        json.dump([nortePrimeraDict, norteSegundaDict, ligaEsteDict, ligaSurDict, ligaOesteDict, listaDeCampeonesDict, [temporada]], listaEquipos, indent = 4)

def registrarCampeones():
    with open("ligas/Campeones.txt", "a", encoding = "utf-8") as archivo:
        sys.stdout = archivo
        print(f"Temporada {temporada}:")
        print(f"🥇 - {confederacionNorte.nombreDelCampeonLigaPrimera()}")
        print(f"🏆 - {confederacionNorte.nombreDelCampeonCopaPrimera()}")
        print(f"🥈 - {confederacionNorte.nombreDelCampeonLigaSegunda()}")
        print(f"🔔 - {confederacionNorte.nombreDelCampeonCopaSegunda()}")
        print(f"⭐ - {copaInternacional.campeon().nombre()}")
        print("")
    sys.stdout = sys.__stdout__

def campeonesSinEquiposDePrimera():
    campeonesDeTodasLasConfederaciones = confederacionNorte.getClasificadosInternacionales() + ligaEste.getClasificadosInternacionales() + ligaSur.getClasificadosInternacionales() + ligaOeste.getClasificadosInternacionales()
    return campeonesDeTodasLasConfederaciones
    
def clasificadosACopaInternacional():
    campeonesDeTodasLasConfederaciones = confederacionNorte.getClasificadosInternacionales() + ligaEste.getClasificadosInternacionales() + ligaSur.getClasificadosInternacionales() + ligaOeste.getClasificadosInternacionales()
    return campeonesDeTodasLasConfederaciones 

def jugarGuardando():
    copaInternacional.jugarCopaGuardandoResultados("ligas/Copa_Internacional_Resultados.txt", temporada, True)
    confederacionNorte.jugarTodasLasCompeticionesGuardando(temporada)
    #copaInternacional.campeon().confederacion().agregarUnaPlazaACopaInternacional()
    ligaEste.jugarCompeticionesDePrimeraImprimiendo(temporada)
    ligaSur.jugarCompeticionesDePrimeraImprimiendo(temporada)
    ligaOeste.jugarCompeticionesDePrimeraImprimiendo(temporada)
    registrarCampeones()
    guardar()

def jugarImprimiendo():
    copaInternacional.jugarCopa(temporada, True)
    confederacionNorte.jugarTodasLasCompeticionesImprimiendo(temporada)
    ligaEste.jugarCompeticionesDePrimeraImprimiendo(temporada)
    ligaSur.jugarCompeticionesDePrimeraImprimiendo(temporada)
    ligaOeste.jugarCompeticionesDePrimeraImprimiendo(temporada)

def main():
    opcion = ""
    print("Bienvenido a juegoLigas, una simulacion sencilla de una liga. Puedes guardar una simulación o solo imprimirla. Elige tu preferencia a continuación, ingresando el número y luego presionando enter:")
    while 1 + 1 == 2:
        print("[1]: Jugar ligas y guardar el progreso")
        print("[2]: Jugar ligas pero solo imprimirlas")
        print("[3]: Salir y cerrar esta ventana")
        opcion = input("Ingrese el número de alguna de las opciones: ")
        if(opcion == "1"):
            jugarGuardando()
            os.startfile(r"ligas")
            input("Simulación terminada, se abrió la carpeta en donde se encuentra la simulación. " \
            "ingrese cualquier tecla para continuar: ")
        elif(opcion == "2"):
            jugarImprimiendo()
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

[ligas]

ligas[equipos]

"""
