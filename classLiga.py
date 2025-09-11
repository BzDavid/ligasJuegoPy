from random import shuffle
import sys
import classEquipo as CE
import classCopa as CC
import logica
class Liga:
    def __init__(self, participantes : list):
        self._participantes = participantes
        self._primerSegmentoDeEquipos = []
        self._segundoSegmentoDeEquipos = []
        self.actualizarEquiposParticipantes()
        self._ultimoCampeon = None

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
                CE.Equipo(str(input("Nombre del primer equipo?: "))),
                CE.Equipo(str(input("Nombre del segundo equipo?: ")))
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
        
    def jugarLigaGuardandoResultados(self, rutaArchivo : str, temporada : int):
        with open(rutaArchivo, "a", encoding = "utf-8") as archivo:
            sys.stdout = archivo
            self.jugarLiga(temporada)
        sys.stdout = sys.__stdout__

class LigaPrimera(Liga):
    def __init__(self, participantes):
        super().__init__(participantes)

    def jugarLiga(self, temporada : int) -> None:
        print(f"\n🟢🟢🟡🟡🔴🔴 Comenzando la temporada número {temporada}...")
        super().jugarLiga()
        print(f"¡El campeón de la liga es: {self._participantes[0].nombre()}!")
        print(f"{self._participantes[len(self._participantes) - 2].nombre()} va a jugar la promoción para permanecer en la liga!")
        print(f"El equipo que desciende es: {self._participantes[len(self._participantes) - 1].nombre()}")
        print("")
        self.imprimirEstadisticasTotalesDeEquipos()
        print("¡La temporada ha terminado!")
        print("")

    def queEquiposDescienden(self) -> list:
        return [self._participantes[int((self.participantes().size() - 2))].nombre(), self._participantes[int((self.participantes().size() - 1))].nombre()]

    def jugarPromocion(self, otraLiga) -> None:
        print("¡La promoción ha comenzado!")
        return logica.jugarIdaYVueltaYDarResultados(self._participantes[len(self._participantes) - 2], otraLiga.participantes()[1])
    
    def eliminarUltimosDos(self):
        self._participantes.pop(int(len(self._participantes) - 1))
        self._participantes.pop(int(len(self._participantes) - 1))

class LigaSegunda(Liga) :
    def __init__(self, participantes):
        super().__init__(participantes)

    def jugarLiga(self, temporada : int):
        print(f"\n🟢🟢🟡🟡🔴🔴 Comenzando la temporada número {temporada}...")
        super().jugarLiga()
        print(f"Campeón y ascenso de la liga: {self._participantes[0].nombre()}")
        print(f"¡{self._participantes[1].nombre()} deberá jugar la promoción para ascender!")
        print("")
        self.imprimirEstadisticasTotalesDeEquipos()
        print("¡La temporada ha terminado!")
        print("")
    
    def queEquiposAscienden(self):
        return list(map(lambda unEquipo: unEquipo.nombre(), self._participantes[0:2]))

    def eliminarPrimerosDos(self):
        self._participantes.pop(0)
        self._participantes.pop(0)

class Confederacion:
    def __init__(self, listaPrimeraDiv, listaSegundaDiv):
        self.ligaPrimera = LigaPrimera(participantes = listaPrimeraDiv)
        self.ligaSegunda = LigaSegunda(participantes = listaSegundaDiv)
        self.copaPrimera = CC.Copa(participantes = listaPrimeraDiv)
        self.copaSegunda = CC.Copa(participantes = listaSegundaDiv)
        self._clasificadosInter = []

    def nombreDelCampeonLigaPrimera(self):
        return self.ligaPrimera.ultimoCampeon().nombre()

    def nombreDelCampeonLigaSegunda(self):
        return self.ligaSegunda.ultimoCampeon().nombre()

    def nombreDelCampeonCopaPrimera(self):
        return self.copaPrimera.campeon().nombre()
    
    def nombreDelCampeonCopaSegunda(self):
        return self.copaSegunda.campeon().nombre()

    def jugarLigaPrimera(self, temporada):
        self.ligaPrimera.jugarLiga(temporada)

    def jugarLigaSegunda(self, temporada):
        self.ligaSegunda.jugarLiga(temporada)
        
    def jugarPromocion(self):
        self.aplicarCambiosDeCategoria()
        print("")
        
    def reiniciarLigas(self):
        self.ligaPrimera.reiniciarLiga()
        self.ligaSegunda.reiniciarLiga()
        
    def jugarCopaPrimera(self, temporada):
        self.copaPrimera.jugarCopa(temporada)

    def jugarCopaSegunda(self, temporada):  
        self.copaSegunda.jugarCopa(temporada)

    def agregarClasificadosInternacionales(self):
        self._clasificadosInter.extend(self.clasificadosACopaInternacionalHastaAhora())

    def getClasificadosInternacionales(self):
        return self._clasificadosInter

    def jugarTodasLasCompeticionesGuardando(self, temporada : int):
        self.copaPrimera.jugarCopaGuardandoResultados("ligas/Copa_1_Resultados.txt", temporada)
        self.copaSegunda.jugarCopaGuardandoResultados("ligas/Copa_2_Resultados.txt", temporada)
        self.ligaPrimera.jugarLigaGuardandoResultados("ligas/Liga_1_Resultados.txt", temporada)
        self.ligaSegunda.jugarLigaGuardandoResultados("ligas/Liga_2_Resultados.txt", temporada)
        self.agregarClasificadosInternacionales()
        logica.jugarCompeticionYGuardarResultados(self.jugarPromocion, "ligas/Liga_2_Resultados.txt")
        self.reiniciarLigas()

    def jugarTodasLasCompeticionesImprimiendo(self, temporada : int):
        self.jugarCopaPrimera(temporada)
        self.jugarCopaSegunda(temporada)
        self.jugarLigaPrimera(temporada)
        self.jugarLigaSegunda(temporada)
        self.agregarClasificadosInternacionales()
        self.jugarPromocion()
        self.reiniciarLigas()
        
    def aplicarCambiosDeCategoria(self):
        equiposQueAscienden = [self.ligaSegunda.participantes()[0]]
        equiposQueDescienden = [self.ligaPrimera.participantes()[int(len(self.ligaPrimera.participantes()) - 1)]]
        ligaTemporal = self.ligaPrimera.jugarPromocion(self.ligaSegunda)
        print(f"¡El ganador de la promoción es {ligaTemporal[0].nombre()}!")
        equiposQueAscienden.append(ligaTemporal[0])
        equiposQueDescienden.append(ligaTemporal[1])
        self.ligaPrimera.eliminarUltimosDos()
        self.ligaSegunda.eliminarPrimerosDos()
        self.ligaPrimera.anadirListaDeEquipos(equiposQueAscienden)
        self.ligaSegunda.anadirListaDeEquipos(equiposQueDescienden)


    def participantesDeLigaPrimera(self):
        return self.ligaPrimera.participantes()
    
    def participantesDeLigaSegunda(self):
        return self.ligaSegunda.participantes() 

    def clasificadosACopaInternacionalHastaAhora(self):
        clasificados = [self.copaPrimera.campeon()]
        if (self.ligaPrimera.primero() in clasificados):
            clasificados.append(self.ligaPrimera.segundo())
            clasificados.append(self.ligaPrimera.tercero())
        elif(self.ligaPrimera.segundo() in clasificados):
            clasificados.append(self.ligaPrimera.primero())
            clasificados.append(self.ligaPrimera.tercero())
        else:
            clasificados.append(self.ligaPrimera.primero())
            clasificados.append(self.ligaPrimera.segundo())
        return clasificados