import random
import sys
def rango():
    return random.randint(1, 6)
def generar():
    resultado = rango() - rango()
    if resultado < 0:
        return 0
    else:
        return resultado

def ganoElLocal(equipoLocal, equipoVisitante) -> bool:
    return equipoLocal.golesEnPartido() > equipoVisitante.golesEnPartido()

def empataronLosEquipos(equipoLocal, equipoVisitante) -> bool:
    return equipoLocal.golesEnPartido() == equipoVisitante.golesEnPartido()
    
def jugarPartido(equipoLocal, equipoVisitante) -> None:
    equipoLocal.jugarPartidoContra_(equipoVisitante)
    equipoVisitante.jugarPartidoContra_(equipoLocal)
    if (ganoElLocal(equipoLocal, equipoVisitante)):
        equipoLocal.gana()
    elif (empataronLosEquipos(equipoLocal, equipoVisitante)):
        equipoLocal.empata()
        equipoVisitante.empata()
    else:
        equipoVisitante.gana()
    mostrarResultado(equipoLocal, equipoVisitante)

def ganadorEntre_(equipoLocal , equipoVisitante):
    equipoLocal.jugarPartidoEspecial()
    equipoVisitante.jugarPartidoEspecial()
    mostrarResultado(equipoLocal, equipoVisitante)
    if (ganoElLocal(equipoLocal, equipoVisitante)):
        return equipoLocal
    elif (empataronLosEquipos(equipoLocal, equipoVisitante)):
        return jugarProrroga(equipoLocal, equipoVisitante)
    else:
        return equipoVisitante

def ganadorEntre_IdaYVuelta(equipoLocal , equipoVisitante):
    globalGolesLocal = 0
    globalGolesVisitante = 0
    for i in range(2):
        equipoLocal.jugarPartidoEspecial()
        equipoVisitante.jugarPartidoEspecial()
        mostrarResultado(equipoLocal, equipoVisitante)
        globalGolesLocal += equipoLocal.golesEnPartido()
        globalGolesVisitante += equipoVisitante.golesEnPartido()
        print(f"El global es [{globalGolesLocal}] - [{globalGolesVisitante}]")
        print("")
    if (globalGolesLocal > globalGolesVisitante):
        return equipoLocal
    elif (globalGolesLocal == globalGolesVisitante):
        return jugarProrroga(equipoLocal, equipoVisitante)
    else:
        return equipoVisitante

def jugarProrroga(equipoLocal, equipoVisitante):
    equipoLocal.jugarProrroga()
    equipoVisitante.jugarProrroga()
    print("Es empate, procediendo a la prórroga: ")
    mostrarResultado(equipoLocal, equipoVisitante)
    if (ganoElLocal(equipoLocal, equipoVisitante)):
        return equipoLocal
    elif (empataronLosEquipos(equipoLocal, equipoVisitante)):
        return jugarTandaDePenales(equipoLocal, equipoVisitante)
    else:
        return equipoVisitante
    
def jugarIdaYVueltaYDarResultados(equipoLocal, equipoVisitante) -> list:
    resultado = []
    resultado.append(ganadorEntre_IdaYVuelta(equipoLocal, equipoVisitante))
    if(equipoLocal in resultado):
        resultado.append(equipoVisitante)
    else:
        resultado.append(equipoLocal)
    return resultado

# ----------------------------------------------------------------

# Esto es lo que era el objeto "resultadosPenales" ---------------
golesLocal = []

golesVisitante = []

def golesTotalesLocal() -> int:
    return sum(golesLocal)

def golesTotalesVisitante() -> int:
    return sum(golesVisitante)

def jugarTandaDePenales(equipoLocal, equipoVisitante):
    reiniciarTandaDePenales()
    for i in range(5):
        jugarUnaRondaDeTandaDePenales()
    jugarUnaRondaMasDePenalesSiEsNecesario()
    print("Resultados de la tanda de penales: ")
    mostrarResultadosDePenales(equipoLocal, equipoVisitante)
    return quienGanoTandaDePenales(equipoLocal, equipoVisitante)
    

def reiniciarTandaDePenales() -> None:
    golesLocal.clear()
    golesVisitante.clear()

def jugarUnaRondaDeTandaDePenales() -> None:
    golesLocal.append(esGolDePenal(rango()))
    golesVisitante.append(esGolDePenal(rango()))

def jugarUnaRondaMasDePenalesSiEsNecesario() -> None:
    while golesTotalesLocal() == golesTotalesVisitante():
        jugarUnaRondaDeTandaDePenales()

def mostrarResultadosDePenales(equipoLocal, equipoVisitante) -> None:
    mostrarListaDePenales(golesLocal, equipoLocal)
    mostrarListaDePenales(golesVisitante, equipoVisitante)

def quienGanoTandaDePenales(equipoLocal , equipoVisitante ):
    if (golesTotalesLocal() > golesTotalesVisitante()):
        return equipoLocal
    else:
        return equipoVisitante

def esGolDePenal(unNumero : int) -> int:
    if (unNumero > 2):
        return 1
    else:
        return 0
    
# ----------------------------------------------------------------

# Esto es lo que era el objeto "mensajes" ---------------

def mostrarResultado(equipoLocal, equipoVisitante) -> None:
    print(f"{equipoLocal.nombre()} [{equipoLocal.golesEnPartido()}] - [{equipoVisitante.golesEnPartido()}] {equipoVisitante.nombre()}")

def mostrarListaDePenales(unaListaDeNumeroPenales : list[int], unEquipo) -> None:
    print(f"{unEquipo.nombre()}: {list(map(lambda x: visualizarPenal(x), unaListaDeNumeroPenales))}")

def visualizarPenal(unNumero : int) -> str:
    if (unNumero == 1):
        return "🟢"
    else:
        return "🔴"
# ----------------------------------------------------------------

def jugarCompeticionYGuardarResultados(competicion, nombreArchivo : str):
    with open(nombreArchivo, "a", encoding = "utf-8") as archivo:
        sys.stdout = archivo
        competicion()
    sys.stdout = sys.__stdout__