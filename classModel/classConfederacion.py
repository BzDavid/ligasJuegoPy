import sys
from .classCopa import Copa
from .classLigaPrimera import LigaPrimera
from .classLigaSegunda import LigaSegunda
from .classEquipo import Equipo
from logica import jugarCompeticionYGuardarResultados

class Confederacion:
    def __init__(self, listaPrimeraDiv: list[Equipo], listaSegundaDiv: list[Equipo] = []) -> None:
        self.ligaPrimera: LigaPrimera = LigaPrimera(participantes = listaPrimeraDiv)
        self.ligaSegunda: LigaSegunda = LigaSegunda(participantes = listaSegundaDiv)
        self.copaPrimera: Copa = Copa(participantes = listaPrimeraDiv)
        self.copaSegunda: Copa = Copa(participantes = listaSegundaDiv)
        self._clasificadosInter: list[Equipo] = []
        # self._tengoPlazaDeCampeon: bool = False
        # self.establecerConfederacionALosEquipos()

    def establecerConfederacionALosEquipos(self) -> None:
        for equipoDePrimera in self.ligaPrimera.participantes():
            equipoDePrimera.establecerConfederacion(self)
        for equipoDeSegunda in self.ligaSegunda.participantes():
            equipoDeSegunda.establecerConfederacion(self)

    def nombreDelCampeonLigaPrimera(self) -> str:
        return self.ligaPrimera.ultimoCampeon().nombre()

    def nombreDelCampeonLigaSegunda(self) -> str:
        return self.ligaSegunda.ultimoCampeon().nombre()

    def nombreDelCampeonCopaPrimera(self) -> str:
        return self.copaPrimera.campeon().nombre()
    
    def nombreDelCampeonCopaSegunda(self) -> str:
        return self.copaSegunda.campeon().nombre()

    def jugarLigaPrimera(self, temporada : int) -> None:
        self.ligaPrimera.jugarLiga(temporada)

    def jugarLigaSegunda(self, temporada : int) -> None:
        self.ligaSegunda.jugarLiga(temporada)
        
    def jugarPromocion(self) -> None:
        self.aplicarCambiosDeCategoria()
        print("")
        
    def reiniciarLigas(self) -> None:
        self.ligaPrimera.reiniciarLiga()
        self.ligaSegunda.reiniciarLiga()
        
    def jugarCopaPrimera(self, temporada : int) -> None:
        self.copaPrimera.jugarCopa(temporada)

    def jugarCopaSegunda(self, temporada : int) -> None:  
        self.copaSegunda.jugarCopa(temporada)

    def agregarClasificadosInternacionales(self) -> None:
        self._clasificadosInter: list[Equipo] = []
        self._clasificadosInter.extend(self.clasificadosACopaInternacionalHastaAhora())

    def getClasificadosInternacionales(self) -> list[Equipo]:
        return self._clasificadosInter

    def jugarTodasLasCompeticionesGuardando(self, temporada : int) -> None:
        self.copaPrimera.jugarCopaGuardandoResultados("ligas/Copa_1_Resultados.txt", temporada)
        self.copaSegunda.jugarCopaGuardandoResultados("ligas/Copa_2_Resultados.txt", temporada)
        self.ligaPrimera.jugarLigaGuardandoResultados("ligas/Liga_1_Resultados.txt", temporada)
        self.ligaSegunda.jugarLigaGuardandoResultados("ligas/Liga_2_Resultados.txt", temporada)
        self.agregarClasificadosInternacionales()
        jugarCompeticionYGuardarResultados(self.jugarPromocion, "ligas/Liga_2_Resultados.txt")
        self.reiniciarLigas()

    def jugarTodasLasCompeticionesImprimiendo(self, temporada : int) -> None:
        DEBUG = False # True para que se imprima por consola
        if (not DEBUG):
            from JuegoLigasUI import TextRedirector
            from JuegoLigasUI_Support import _w1
            WidgetDeTexto = TextRedirector(_w1)
            sys.stdout = WidgetDeTexto
        self.jugarCopaPrimera(temporada)
        self.jugarCopaSegunda(temporada)
        self.jugarLigaPrimera(temporada)
        self.jugarLigaSegunda(temporada)
        self.agregarClasificadosInternacionales()
        self.jugarPromocion()
        self.reiniciarLigas()
        if (not DEBUG):
            sys.stdout = sys.__stdout__

    def jugarCompeticionesDePrimeraImprimiendo(self, temporada : int) -> None:
        DEBUG = False # True para que se imprima por consola
        if (not DEBUG):
            from JuegoLigasUI import TextRedirector
            from JuegoLigasUI_Support import _w1
            WidgetDeTexto = TextRedirector(_w1)
            sys.stdout = WidgetDeTexto
        self.jugarCopaPrimera(temporada)
        self.jugarLigaPrimera(temporada)
        self.agregarClasificadosInternacionales()
        self.reiniciarLigas()
        if (not DEBUG):
            sys.stdout = sys.__stdout__
        
    def aplicarCambiosDeCategoria(self) -> None:
        equiposQueAscienden: list[Equipo] = [self.ligaSegunda.participantes()[0]]
        equiposQueDescienden: list[Equipo] = [self.ligaPrimera.participantes()[int(len(self.ligaPrimera.participantes()) - 1)]]
        ligaTemporal: list[Equipo] = self.ligaPrimera.jugarPromocion(self.ligaSegunda)
        print(f"¡El ganador de la promoción es {ligaTemporal[0].nombre()}!")
        equiposQueAscienden.append(ligaTemporal[0])
        equiposQueDescienden.append(ligaTemporal[1])
        self.ligaPrimera.eliminarUltimosDos()
        self.ligaSegunda.eliminarPrimerosDos()
        self.ligaPrimera.anadirListaDeEquipos(equiposQueAscienden)
        self.ligaSegunda.anadirListaDeEquipos(equiposQueDescienden)


    def participantesDeLigaPrimera(self) -> list[Equipo]:
        return self.ligaPrimera.participantes()
    
    def participantesDeLigaSegunda(self) -> list[Equipo]:
        return self.ligaSegunda.participantes() 

    # Deprecated
    # def clasificadosACopaInternacionalHastaAhora(self): 
    #     clasificados: list[Equipo] = self.ligaPrimera.topTres() if self._tengoPlazaDeCampeon else self.ligaPrimera.topDos()
    #     if (self.copaPrimera.campeon()) in clasificados:
    #         clasificados.append(self.ligaPrimera.cuarto() if self._tengoPlazaDeCampeon else self.ligaPrimera.tercero())
    #     else: 
    #         clasificados.append(self.copaPrimera.campeon())
    #     return clasificados
    
    def clasificadosACopaInternacionalHastaAhora(self):
        clasificados: list[Equipo] = self.ligaPrimera.topTres()
        if (self.copaPrimera.campeon() in clasificados):
            clasificados.append(self.ligaPrimera.cuarto())
        else: 
            clasificados.append(self.copaPrimera.campeon())
        return clasificados
    
    def agregarUnaPlazaACopaInternacional(self) -> None:
        self._tengoPlazaDeCampeon = True

    def equipo_EstaEnEstaConfederacion(self, nombreEquipo: str):
        return self.ligaPrimera.equipo_EstaEnEstaLiga(nombreEquipo) or self.ligaSegunda.equipo_EstaEnEstaLiga(nombreEquipo)