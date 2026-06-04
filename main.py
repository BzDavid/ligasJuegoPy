import classes.classConfederacion as CL
import classes.classEquipo as CE
import classes.classCopa as CC
import json
import os
import sys

def descomprimirEquiposDeLista(listaParaDescomprimir: list[dict]) -> list[CE.Equipo]:
    listaDescomprimida: list[CE.Equipo] = []
    for equipo in listaParaDescomprimir:
        listaDescomprimida.append(CE.Equipo(**equipo))
    return listaDescomprimida

# Para cargar datos del archivo de los equipos
with open("equipos.json", "r") as listaEquipos:
    equiposCargados: list[list[dict]] = json.load(listaEquipos)
    nortePrimera: list[CE.Equipo] = descomprimirEquiposDeLista(equiposCargados[0])
    norteSegunda: list[CE.Equipo] = descomprimirEquiposDeLista(equiposCargados[1])
    estePrimera: list[CE.Equipo] = descomprimirEquiposDeLista(equiposCargados[2])
    surPrimera: list[CE.Equipo] = descomprimirEquiposDeLista(equiposCargados[3])
    oestePrimera: list[CE.Equipo] = descomprimirEquiposDeLista(equiposCargados[4])
    listaDeCampeones: list[CE.Equipo] = descomprimirEquiposDeLista(equiposCargados[5])
    # nortePrimera: list[CE.Equipo] = [CE.Equipo(**equipo) for equipo in equiposCargados[0]]
    # norteSegunda: list[CE.Equipo] = [CE.Equipo(**equipo) for equipo in equiposCargados[1]]
    # estePrimera: list[CE.Equipo] = [CE.Equipo(**equipo) for equipo in equiposCargados[2]]
    # surPrimera: list[CE.Equipo] = [CE.Equipo(**equipo) for equipo in equiposCargados[3]]
    # oestePrimera: list[CE.Equipo] = [CE.Equipo(**equipo) for equipo in equiposCargados[4]]
    # listaDeCampeones: list[CE.Equipo] = [CE.Equipo(**equipo) for equipo in equiposCargados[5]]
    temporada: int = equiposCargados[6][0]
    del equiposCargados

confederacionNorte: CL.Confederacion = CL.Confederacion(
    listaPrimeraDiv = nortePrimera,
    listaSegundaDiv = norteSegunda
)

ligaEste: CL.Confederacion = CL.Confederacion(listaPrimeraDiv = estePrimera)

ligaSur: CL.Confederacion = CL.Confederacion(listaPrimeraDiv = surPrimera)

ligaOeste: CL.Confederacion = CL.Confederacion(listaPrimeraDiv = oestePrimera)

copaInternacional: CC.Copa = CC.Copa(participantes = listaDeCampeones)

# El programa
def guardar() -> None:
    global temporada
    nortePrimeraDict: list = [equipo.dict() for equipo in confederacionNorte.participantesDeLigaPrimera()]
    norteSegundaDict: list = [equipo.dict() for equipo in confederacionNorte.participantesDeLigaSegunda()]
    ligaEsteDict: list = [equipo.dict() for equipo in ligaEste.ligaPrimera.participantes()]
    ligaSurDict: list = [equipo.dict() for equipo in ligaSur.ligaPrimera.participantes()]
    ligaOesteDict: list = [equipo.dict() for equipo in ligaOeste.ligaPrimera.participantes()]
    listaDeCampeonesDict: list = [equipo.dict() for equipo in clasificadosACopaInternacional()]
    temporada += 1

    with open("equipos.json", "w") as listaEquipos:
        json.dump([nortePrimeraDict, norteSegundaDict, ligaEsteDict, ligaSurDict, ligaOesteDict, listaDeCampeonesDict, [temporada]], listaEquipos, indent = 4)

def registrarCampeones() -> None:
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

# def campeonesSinEquiposDePrimera() -> list:
#     campeonesDeTodasLasConfederaciones = confederacionNorte.getClasificadosInternacionales() + ligaEste.getClasificadosInternacionales() + ligaSur.getClasificadosInternacionales() + ligaOeste.getClasificadosInternacionales()
#     return campeonesDeTodasLasConfederaciones
    
def clasificadosACopaInternacional() -> list:
    campeonesDeTodasLasConfederaciones = confederacionNorte.getClasificadosInternacionales() + ligaEste.getClasificadosInternacionales() + ligaSur.getClasificadosInternacionales() + ligaOeste.getClasificadosInternacionales()
    return campeonesDeTodasLasConfederaciones 

def jugarGuardando() -> None:
    copaInternacional.jugarCopaGuardandoResultados("ligas/Copa_Internacional_Resultados.txt", temporada, True)
    confederacionNorte.jugarTodasLasCompeticionesGuardando(temporada)
    copaInternacional.campeon().confederacion().agregarUnaPlazaACopaInternacional()
    ligaEste.jugarCompeticionesDePrimeraImprimiendo(temporada)
    ligaSur.jugarCompeticionesDePrimeraImprimiendo(temporada)
    ligaOeste.jugarCompeticionesDePrimeraImprimiendo(temporada)
    registrarCampeones()
    guardar()

def jugarImprimiendo() -> None:
    copaInternacional.jugarCopa(temporada, True)
    confederacionNorte.jugarTodasLasCompeticionesImprimiendo(temporada)
    ligaEste.jugarCompeticionesDePrimeraImprimiendo(temporada)
    ligaSur.jugarCompeticionesDePrimeraImprimiendo(temporada)
    ligaOeste.jugarCompeticionesDePrimeraImprimiendo(temporada)

def main() -> None:
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

if __name__ == "__main__":
    main()