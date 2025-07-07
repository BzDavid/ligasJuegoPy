import random
class Liga:
    def __init__(self, participantes : list):
        self._participantes = participantes
        self._primerSegmentoDeEquipos = []
        self._segundoSegmentoDeEquipos = []
        self.actualizarEquiposParticipantes()

    def primerSegmentoPorNombre(self): 
        return list(map(lambda equipo: equipo.nombre(), self._primerSegmentoDeEquipos))

    def segundoSegmentoPorNombre(self):
        return list(map(lambda equipo: equipo.nombre(), self._segundoSegmentoDeEquipos))

    def participantesPorNombre(self):
        return list(map(lambda equipo: equipo.nombre(), self._participantes))

    def participantesPorPuntos(self): 
        return list(map(lambda equipo: equipo.puntos(), self._participantes))

    def primerSegmentoDeEquipos(self):
        return self._primerSegmentoDeEquipos

    def participantes(self):
        return self._participantes

    def anadirListaDeEquipos(self, unaListaDeEquipos : list) -> None:
        self._participantes.extend(unaListaDeEquipos)
        self.actualizarEquiposParticipantes()

    def eliminarYAnadirLista(self, unaListaDeEquipos : list) -> None:
        self._participantes.clear()
        self.anadirListaDeEquipos(unaListaDeEquipos)

    def eliminarParticipante(self, unParticipante : str) -> None:
        if unParticipante in self._participantes:
            self._participantes.remove(unParticipante)
            self.actualizarEquiposParticipantes()
        else:
            raise ValueError(f"El participante {unParticipante} no está en la liga.")
        
    # def criterioOrdenamiento(equipoUno, equipoDos) -> bool:
    #     if (equipoUno.puntos() > equipoDos.puntos()):
    #         return equipoUno.diferenciaDeGoles() > equipoDos.diferenciaDeGoles()
    #     else:
    #         return equipoUno.puntos() > equipoDos.puntos()

    def ordenarPorPuntos(self) -> None:
        self._participantes.sort(key = lambda unEquipo: (unEquipo.puntos(), unEquipo.diferenciaDeGoles()), reverse = True)

    def imprimirEstadoDeLiga(self) -> None:
        self.ordenarPorPuntos()
        print("Estado de la Liga: ")
        print("")
        self.imprimirEstadisticasDeEquipos()

    def imprimirEstadisticasDeEquipos(self) -> None:
        posicion = 0
        for equipo in self._participantes:
            posicion += 1
            print(f"{posicion}. {equipo.stats()}")
        posicion = 0

    def imprimirEstadisticasTotalesDeEquipos(self) -> None:
        posicion = 0
        for equipo in self._participantes:
            posicion += 1
            print(f"{posicion}. {equipo.fullStats()}")
        posicion = 0

    def jugarUnaVuelta(self) -> None:
        for i in list(range(len(self._participantes) - 1)):
            print(f"Inicio de la fecha {i + 1} ==========================")
            self.jugarFecha()
            print("")
            self.imprimirEstadoDeLiga()

    def jugarLiga(self) -> None:
        self.jugarUnaVuelta()
        print("")
        print("Fin de la primera vuelta ==========================")
        print("")
        self.jugarUnaVuelta()
        print("")

    def reiniciarLiga(self) -> None:
        for equipo in self._participantes:
            equipo.reiniciarEstadisticas()

    def jugarFecha(self) -> None:
        rangoDeEquipos = list(range(0, int(len(self._participantes) / 2)))
        for i in rangoDeEquipos:
            jugarPartido(
                self._primerSegmentoDeEquipos[i],
                self._segundoSegmentoDeEquipos[i])
        self.ordenarSegmentosParaSiguienteFecha()

    def ordenarSegmentosParaSiguienteFecha(self) -> None:
        self._segundoSegmentoDeEquipos.append(self._primerSegmentoDeEquipos[int(len(self._primerSegmentoDeEquipos) - 1)])
        self._primerSegmentoDeEquipos.extend([self._segundoSegmentoDeEquipos[1]] + self._primerSegmentoDeEquipos[0:int(len(self._primerSegmentoDeEquipos) - 1)])
        for equipo in self._primerSegmentoDeEquipos[0:int(len(self._primerSegmentoDeEquipos) / 2)]:
            self._primerSegmentoDeEquipos.remove(equipo)
        self._segundoSegmentoDeEquipos.pop(1)

    def actualizarEquiposParticipantes(self) -> None:
        random.shuffle(self._participantes)
        self._primerSegmentoDeEquipos.clear()
        self._primerSegmentoDeEquipos.extend(self._participantes[
            0 :
            int(len(self._participantes) - (len(self._participantes) / 2))])
        self._segundoSegmentoDeEquipos.clear()
        self._segundoSegmentoDeEquipos.extend(self._participantes[
            int(len(self._participantes) - (len(self._participantes) / 2)) :
            int(len(self._participantes))])
        
class Equipo:
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre
        self._puntos = 0
        self._golesAFavor = 0
        self._golesEnContra = 0
        self._golesEnPartido = 0

    def __str__(self):
        return self._nombre
    
    def puntos(self) -> int:
        return self._puntos

    def golesAFavor(self) -> int:
        return self._golesAFavor

    def golesEnContra(self) -> int:
        return self._golesEnContra

    def golesEnPartido(self) -> int:
        return self._golesEnPartido

    def diferenciaDeGoles(self) -> int:
        return self._golesAFavor - self._golesEnContra
    
    def nombre(self) -> str:
        return self._nombre
    
    def statGoles(self) -> list:
        return [self._golesAFavor, self._golesEnContra, self.diferenciaDeGoles()]
    
    def stats(self) -> list: 
        return [self._nombre, self._puntos, self.diferenciaDeGoles()]

    def fullStats(self) -> list:
        return [self._nombre, self._puntos, self._golesAFavor, self._golesEnContra, self.diferenciaDeGoles()]

    def jugarPartidoContra_(self, unRival) -> None:
        self._golesEnPartido = generar()
        self._golesAFavor += self._golesEnPartido
        unRival.sumarGolesEnContra(self._golesEnPartido)

    def jugarPartidoEspecial(self):
        self._golesEnPartido = generar()
        
    def jugarProrroga(self):
        self._golesEnPartido = max(generar() - 3, 0)

    def sumarGolesEnContra(self, goles: int) -> None:
        self._golesEnContra += goles

    def reiniciarEstadisticas(self) -> None:
        self._puntos = 0
        self._golesAFavor = 0
        self._golesEnContra = 0
        self._golesEnPartido = 0

    def gana(self):
        self._puntos += 3

    def empata(self):
        self._puntos += 1

# Esto es lo que era el objeto "resultados" ---------------
def rango():
    return random.randint(1, 6)
    
def generar():
    resultado = rango() - rango()
    if resultado < 0:
        return 0
    else:
        return resultado

def jugarPartido(equipoLocal: Equipo, equipoVisitante: Equipo) -> None:
    equipoLocal.jugarPartidoContra_(equipoVisitante)
    equipoVisitante.jugarPartidoContra_(equipoLocal)
    if (equipoLocal.golesEnPartido() > equipoVisitante.golesEnPartido()):
        equipoLocal.gana()
    elif (equipoLocal.golesEnPartido() == equipoVisitante.golesEnPartido()):
        equipoLocal.empata()
        equipoVisitante.empata()
    else:
        equipoVisitante.gana()
    mostrarResultado(equipoLocal, equipoVisitante)

def ganadorEntre_(equipoLocal : Equipo, equipoVisitante: Equipo) -> Equipo:
    equipoLocal.jugarPartidoEspecial()
    equipoVisitante.jugarPartidoEspecial()
    mostrarResultado(equipoLocal, equipoVisitante)
    if (equipoLocal.golesEnPartido() > equipoVisitante.golesEnPartido()):
        return equipoLocal
    elif (equipoLocal.golesEnPartido() == equipoVisitante.golesEnPartido()):
        return jugarProrroga(equipoLocal, equipoVisitante)
    else:
        return equipoVisitante

def jugarProrroga(equipoLocal: Equipo, equipoVisitante: Equipo) -> Equipo:
    equipoLocal.jugarProrroga()
    equipoVisitante.jugarProrroga()
    print("Es empate, procediendo a la prórroga: ")
    mostrarResultado(equipoLocal, equipoVisitante)
    if (equipoLocal.golesEnPartido() > equipoVisitante.golesEnPartido()):
        return equipoLocal
    elif (equipoLocal.golesEnPartido() == equipoVisitante.golesEnPartido()):
        return jugarTandaDePenales(equipoLocal, equipoVisitante)
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

def jugarTandaDePenales(equipoLocal: Equipo, equipoVisitante: Equipo) -> Equipo:
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

def mostrarResultadosDePenales(equipoLocal: Equipo, equipoVisitante: Equipo) -> None:
    mostrarListaDePenales(golesLocal, equipoLocal)
    mostrarListaDePenales(golesVisitante, equipoVisitante)

def quienGanoTandaDePenales(equipoLocal : Equipo, equipoVisitante : Equipo) -> Equipo:
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

def mostrarResultado(equipoLocal: Equipo, equipoVisitante: Equipo) -> None:
    print(f"{equipoLocal.nombre()} [{equipoLocal.golesEnPartido()}] - [{equipoVisitante.golesEnPartido()}] {equipoVisitante.nombre()}")

def mostrarListaDePenales(unaListaDeNumeroPenales : list[int], unEquipo: Equipo) -> None:
    print(f"{unEquipo.nombre()}: {list(map(lambda x: visualizarPenal(x), unaListaDeNumeroPenales))}")

def visualizarPenal(unNumero : int) -> None:
    if (unNumero == 1):
        return "🟢"
    else:
        return "🔴"
# ----------------------------------------------------------------