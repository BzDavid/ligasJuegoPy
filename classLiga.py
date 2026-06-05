import sys
import logica
from random import shuffle
from classEquipo import Equipo

class Liga:
    def __init__(self, participantes: list[Equipo], nombreDeLiga: str = "Liga"):
        self._nombreDeLiga: str = nombreDeLiga
        self._participantes: list[Equipo] = participantes
        self._primerSegmentoDeEquipos: list[Equipo] = []
        self._segundoSegmentoDeEquipos: list[Equipo] = []
        self.actualizarEquiposParticipantes()
        self._ultimoCampeon: Equipo = None

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

    def participantes(self) -> list[Equipo]:
        return self._participantes
    
    def topTres(self):
        return self.topDos() + [self.tercero()]
    
    def topDos(self):
        return [self.primero(), self.segundo()]
    
    def primero(self):
        if(len(self._participantes) < 1): 
            print("No hay tantos equipos")
            return None
        return self._participantes[0]

    def segundo(self):
        if(len(self._participantes) < 2): 
            print("No hay tantos equipos")
            return None
        return self._participantes[1]

    def tercero(self):
        if(len(self._participantes) < 3): 
            print("No hay tantos equipos")
            return None
        return self._participantes[2]
    
    def cuarto(self):
        if(len(self._participantes) < 4): 
            print("No hay tantos equipos")
            return None
        return self._participantes[3]
    
    def ultimo(self):
        if(len(self._participantes) < 1): 
            print("No hay tantos equipos")
            return None
        return self._participantes[int(len(self._participantes) - 1)]
    
    def ultimoCampeon(self):
        return self._ultimoCampeon

    def crearDosEquiposYAnadirlos(self):
        self.anadirListaDeEquipos(
            [
                Equipo(str(input("Nombre del primer equipo?: "))),
                Equipo(str(input("Nombre del segundo equipo?: ")))
            ]
        )

    def anadirEquipo(self, unEquipo):
        self._participantes.append(unEquipo)

    def anadirListaDeEquipos(self, unaListaDeEquipos : list) -> None:
        self._participantes.extend(unaListaDeEquipos)
        self.actualizarEquiposParticipantes()

    def eliminarYAnadirLista(self, unaListaDeEquipos : list) -> None:
        self._participantes.clear()
        self.anadirListaDeEquipos(unaListaDeEquipos)

    def eliminarParticipantePorNombre(self, nombreDelParticipante : str) -> None:
        for equipo in self._participantes:
            if equipo.nombre() == nombreDelParticipante:
                self._participantes.remove(equipo)
                break

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

    def imprimirEstadisticasTotalesDeEquipos(self) -> None:
        posicion = 0
        for equipo in self._participantes:
            posicion += 1
            print(f"{posicion}. {equipo.fullStats()}")

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
        self._ultimoCampeon = self._participantes[0]

    def reiniciarLiga(self) -> None:
        for equipo in self._participantes:
            equipo.reiniciarEstadisticas()

    def jugarFecha(self) -> None:
        rangoDeEquipos = list(range(0, int(len(self._participantes) / 2)))
        for i in rangoDeEquipos:
            logica.jugarPartido(
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
        shuffle(self._participantes)
        self._primerSegmentoDeEquipos.clear()
        self._primerSegmentoDeEquipos.extend(self._participantes[
            0 :
            int(len(self._participantes) - (len(self._participantes) / 2))])
        self._segundoSegmentoDeEquipos.clear()
        self._segundoSegmentoDeEquipos.extend(self._participantes[
            int(len(self._participantes) - (len(self._participantes) / 2)) :
            int(len(self._participantes))])

    def dict(self):
        return {
            "participantes" : [equipo.dict() for equipo in self._participantes],
            "nombreDeLiga" : self._nombreDeLiga
        }
        
    def jugarLigaGuardandoResultados(self, rutaArchivo : str, temporada : int):
        with open(rutaArchivo, "a", encoding = "utf-8") as archivo:
            sys.stdout = archivo
            self.jugarLiga(temporada)
        sys.stdout = sys.__stdout__