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
    
def jugarPartido(equipoLocal, equipoVisitante) -> None: # Para la liga
    equipoLocal.jugarPartidoContra_(equipoVisitante)
    equipoVisitante.jugarPartidoContra_(equipoLocal)
    if (ganoElLocal(equipoLocal, equipoVisitante)):
        equipoLocal.gana(equipoVisitante)
    elif (empataronLosEquipos(equipoLocal, equipoVisitante)):
        equipoLocal.empata()
        equipoVisitante.empata()
    else:
        equipoVisitante.gana(equipoLocal)
    mostrarResultado(equipoLocal, equipoVisitante)

def ganadorEntre_(equipoLocal , equipoVisitante, verResultado : bool = True):
    equipoLocal.jugarPartidoEspecial()
    equipoVisitante.jugarPartidoEspecial()
    if (verResultado):
        mostrarResultado(equipoLocal, equipoVisitante)
    if (ganoElLocal(equipoLocal, equipoVisitante)):
        return equipoLocal
    elif (empataronLosEquipos(equipoLocal, equipoVisitante)):
        return jugarProrroga(equipoLocal, equipoVisitante, verResultado)
    else:
        return equipoVisitante

def jugarProrroga(equipoLocal, equipoVisitante, verResultado : bool = True):
    equipoLocal.jugarProrroga()
    equipoVisitante.jugarProrroga()
    if (verResultado):
        print("Es empate, procediendo a la prórroga: ")
        mostrarResultadoConSuspenso(equipoLocal, equipoVisitante)
    if (ganoElLocal(equipoLocal, equipoVisitante)):
        return equipoLocal
    elif (empataronLosEquipos(equipoLocal, equipoVisitante)):
        return jugarTandaDePenales(equipoLocal, equipoVisitante, verResultado)
    else:
        return equipoVisitante

def ganadorEntre_ParaCopas(equipoLocal , equipoVisitante):
    equipoLocal.jugarPartidoEspecial()
    equipoVisitante.jugarPartidoEspecial()
    mostrarResultadoConSuspenso(equipoLocal, equipoVisitante)
    if (ganoElLocal(equipoLocal, equipoVisitante)):
        return equipoLocal
    elif (empataronLosEquipos(equipoLocal, equipoVisitante)):
        return jugarProrroga(equipoLocal, equipoVisitante)
    else:
        return equipoVisitante

def jugarIdaYVueltaYDarResultados(equipoLocal, equipoVisitante) -> list:
    "El primero de la lista es el hipotético ganador"
    resultado = []
    resultado.append(ganadorEntre_IdaYVuelta(equipoLocal, equipoVisitante))
    if(equipoLocal in resultado):
        resultado.append(equipoVisitante)
    else:
        resultado.append(equipoLocal)
    return resultado

def ganadorEntre_IdaYVuelta(equipoLocal , equipoVisitante): # Función auxiliar, me maté pensando que servia para otra cosa mas que solo la func de arriba.
    for i in range(2):
        equipoLocal.jugarPartidoIYV()
        equipoVisitante.jugarPartidoIYV()
        mostrarResultadoConSuspenso(equipoLocal, equipoVisitante)
        mostrarResultadoDeEncuentroIYV(equipoLocal, equipoVisitante, i)
        print("")
    if (equipoLocal.golesGlobales() > equipoVisitante.golesGlobales()):
        return equipoLocal
    elif (equipoLocal.golesGlobales() == equipoVisitante.golesGlobales()):
        return jugarProrroga(equipoLocal, equipoVisitante)
    else:
        return equipoVisitante
    
# ----------------------------------------------------------------

# Esto es lo que era el objeto "resultadosPenales" ---------------
golesLocal = []

golesVisitante = []

def golesTotalesLocal() -> int:
    return sum(golesLocal)

def golesTotalesVisitante() -> int:
    return sum(golesVisitante)

def jugarTandaDePenales(equipoLocal, equipoVisitante, verResultado : bool = True):
    reiniciarTandaDePenales()
    for i in range(5):
        jugarUnaRondaDeTandaDePenales()
    jugarUnaRondaMasDePenalesSiEsNecesario()
    if (verResultado):
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

def mostrarResultadoConSuspenso(equipoLocal, equipoVisitante) -> None:
    print(f"{equipoLocal.nombre()} [{equipoLocal.golesEnPartido()}]")
    print(f"{equipoVisitante.nombre()} [{equipoVisitante.golesEnPartido()}]")

def mostrarListaDePenales(unaListaDeNumeroPenales : list[int], unEquipo) -> None:
    print(f"{unEquipo.nombre()}: {list(map(lambda x: visualizarPenal(x), unaListaDeNumeroPenales))}")

def visualizarPenal(unNumero : int) -> str:
    if (unNumero == 1):
        return "🟢"
    else:
        return "🔴"
    
def mostrarResultadoDeEncuentroIYV(equipoLocal, equipoVisitante, numeroDeEnfrentamiento : int):
    if(numeroDeEnfrentamiento == 0):
        print(f"{equipoLocal.nombre()} [{equipoLocal.golesEnPartido()}]")
        print(f"{equipoVisitante.nombre()} [{equipoVisitante.golesEnPartido()}]")
        print(f"Global: {equipoLocal.nombre()} [{equipoLocal.golesGlobales()}] - [{equipoVisitante.golesGlobales()}] {equipoVisitante.nombre()}")
    else:
        print(f"{equipoVisitante.nombre()} [{equipoVisitante.golesEnPartido()}]")
        print(f"{equipoLocal.nombre()} [{equipoLocal.golesEnPartido()}]")
        print(f"Global: {equipoVisitante.nombre()} [{equipoVisitante.golesGlobales()}] - [{equipoLocal.golesGlobales()}] {equipoLocal.nombre()}")
# ----------------------------------------------------------------

def jugarCompeticionYGuardarResultados(competicion, nombreArchivo : str):
    with open(nombreArchivo, "a", encoding = "utf-8") as archivo:
        sys.stdout = archivo
        competicion()
    sys.stdout = sys.__stdout__