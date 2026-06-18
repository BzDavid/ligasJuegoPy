import classModel.classConfederacion as CL
import classModel.classEquipo as CE
import classModel.classCopa as CC
import json
import os
import sys
from pathlib import Path
from random import shuffle

isRunningInConsole: bool = False
equiposCargados: list[list[dict]]
nortePrimera: list[CE.Equipo]
norteSegunda: list[CE.Equipo]
estePrimera: list[CE.Equipo]
surPrimera: list[CE.Equipo]
oestePrimera: list[CE.Equipo]
listaDeCampeones: list[CE.Equipo]
temporada: int

def descomprimirEquiposDeLista(listaParaDescomprimir: list[dict]) -> list[CE.Equipo]:
    listaDescomprimida: list[CE.Equipo] = []
    for equipo in listaParaDescomprimir:
        listaDescomprimida.append(CE.Equipo(**equipo))
    return listaDescomprimida

rutaDelJson: Path = Path(__file__).parent / "equipos.json"
# Para cargar datos del archivo de los equipos
with open(rutaDelJson, "r") as listaEquipos:
    equiposCargados = json.load(listaEquipos)
    nortePrimera = descomprimirEquiposDeLista(equiposCargados[0])
    norteSegunda = descomprimirEquiposDeLista(equiposCargados[1])
    estePrimera = descomprimirEquiposDeLista(equiposCargados[2])
    surPrimera = descomprimirEquiposDeLista(equiposCargados[3])
    oestePrimera = descomprimirEquiposDeLista(equiposCargados[4])
    listaDeCampeones = descomprimirEquiposDeLista(equiposCargados[5])
    temporada = equiposCargados[6][0]
    del equiposCargados

confederacionNorte: CL.Confederacion = CL.Confederacion(
    listaPrimeraDiv = nortePrimera,
    listaSegundaDiv = norteSegunda
)

ligaEste: CL.Confederacion = CL.Confederacion(listaPrimeraDiv = estePrimera)

ligaSur: CL.Confederacion = CL.Confederacion(listaPrimeraDiv = surPrimera)

ligaOeste: CL.Confederacion = CL.Confederacion(listaPrimeraDiv = oestePrimera)

copaInternacional: CC.Copa = CC.Copa(participantes = listaDeCampeones)

confederaciones: list[CL.Confederacion] = [confederacionNorte, ligaEste, ligaOeste, ligaSur]

del nortePrimera
del norteSegunda
del estePrimera
del surPrimera
del oestePrimera

# El programa
def guardar() -> None:
    global temporada
    nortePrimeraDict: list = [equipo.toDict() for equipo in confederacionNorte.participantesDeLigaPrimera()]
    norteSegundaDict: list = [equipo.toDict() for equipo in confederacionNorte.participantesDeLigaSegunda()]
    ligaEsteDict: list = [equipo.toDict() for equipo in ligaEste.ligaPrimera.participantes()]
    ligaSurDict: list = [equipo.toDict() for equipo in ligaSur.ligaPrimera.participantes()]
    ligaOesteDict: list = [equipo.toDict() for equipo in ligaOeste.ligaPrimera.participantes()]
    listaDeCampeonesDict: list = [equipo.toDict() for equipo in clasificadosACopaInternacional()]
    temporada += 1

    with open(rutaDelJson, "w") as listaEquipos:
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
    
def clasificadosACopaInternacional() -> list[CE.Equipo]:
    iteracion: int = 0
    listaParaDejarAfueraAUnEquipoDeUnaConfederacion: list[bool] = [True, False, False]
    shuffle(listaParaDejarAfueraAUnEquipoDeUnaConfederacion)
    clasificadosDeConfederacionesNoCampeonas: list[CE.Equipo] = []
    for confederacion in confederacionesNoCampeonas():
        clasificadosDeConfederacionesNoCampeonas = clasificadosDeConfederacionesNoCampeonas + confederacion.getClasificadosInternacionales(listaParaDejarAfueraAUnEquipoDeUnaConfederacion[iteracion])
        iteracion += 1
    clasificadosDeTodasLasConfederaciones = confederacionCampeona()[0].getClasificadosInternacionales() + clasificadosDeConfederacionesNoCampeonas
    return clasificadosDeTodasLasConfederaciones 

def confederacionDelEquipo_(unEquipo: CE.Equipo) -> CL.Confederacion:
    confederacionesLocal: list[CL.Confederacion] = confederaciones.copy()
    for confederacion in confederacionesLocal:
        if(confederacion.equipo_EstaEnEstaConfederacion(unEquipo.nombre())):
            return confederacion
    return None

def establecerCampeonInternacionalASuConfederacion(unEquipo: CE.Equipo) -> None:
    confederacionDelEquipo_(unEquipo).agregarEquipoCampeonDeCopaInternacional(unEquipo.nombre())

def confederacionesNoCampeonas() -> list[CL.Confederacion]:
    confederacionesLocal: list[CL.Confederacion] = confederaciones.copy()
    for confederacion in confederacionesLocal:
        if(confederacion._equipoCampeonDeCopaInternacional != None):
            confederacionesLocal.remove(confederacion)
    return confederacionesLocal

def confederacionCampeona() -> list[CL.Confederacion]:
    confederacionesLocal: list[CL.Confederacion] = confederaciones.copy()
    for confederacion in confederacionesLocal:
        if(confederacion._equipoCampeonDeCopaInternacional != None):
            return [confederacion]
    return None

def jugarGuardando() -> None:
    copaInternacional.jugarCopaGuardandoResultados("ligas/Copa_Internacional_Resultados.txt", temporada, True)
    establecerCampeonInternacionalASuConfederacion(copaInternacional.campeon())
    confederacionNorte.jugarTodasLasCompeticionesGuardando(temporada)
    ligaEste.jugarCompeticionesDePrimeraImprimiendo(temporada, isRunningInConsole)
    ligaSur.jugarCompeticionesDePrimeraImprimiendo(temporada, isRunningInConsole)
    ligaOeste.jugarCompeticionesDePrimeraImprimiendo(temporada, isRunningInConsole)
    registrarCampeones()
    guardar()

def jugarImprimiendo() -> None:
    copaInternacional.jugarCopaImprimiendo(temporada, isRunningInConsole, True)
    confederacionNorte.jugarTodasLasCompeticionesImprimiendo(temporada, isRunningInConsole)
    ligaEste.jugarCompeticionesDePrimeraImprimiendo(temporada, isRunningInConsole)
    ligaSur.jugarCompeticionesDePrimeraImprimiendo(temporada, isRunningInConsole)
    ligaOeste.jugarCompeticionesDePrimeraImprimiendo(temporada, isRunningInConsole)

def segundaOpcion() -> None:
    jugarGuardando()
    os.startfile(r"ligas")

def primeraOpcion() -> None:
    jugarImprimiendo()

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
    isRunningInConsole = True
    main()