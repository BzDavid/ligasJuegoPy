from random import shuffle
import classLiga
import sys
from logica import ganadorEntre_ParaCopas
import classEquipo
class Copa:
    def __init__(self, participantes) -> None:
        self._participantes = participantes
        self._listaDeGrupos = []
        self._faseFinalGrupo1 = []
        self._faseFinalGrupo2 = []
        shuffle(self._participantes)
        self.anadirParticipantesAGrupos()
        self._campeon = classEquipo.Equipo("NoHay")

    # Funciones de retorno

    def _listaDeGrupos(self) -> None:
        return self._listaDeGrupos

    def faseFinalGrupo1(self) -> None:
        return self._faseFinalGrupo1

    def faseFinalGrupo1PorNombre(self) -> None:
        return list(map(lambda equipo: equipo.nombre(), self._faseFinalGrupo1))

    def faseFinalGrupo2PorNombre(self) -> None:
        return list(map(lambda equipo: equipo.nombre(), self._faseFinalGrupo2))

    def faseFinalGrupo2(self) -> None:
        return self._faseFinalGrupo2
    
    def participantes(self) -> None:
        return self._participantes

    def campeon(self) -> classEquipo.Equipo: 
        return self._campeon  
    
    def ListaDelCeroHastaMitadDeLaLongitudDeLaFaseFinalDelGrupo1(self) -> list:
        "Hace una lista arrancando del cero hasta la mitad del tamaño de la lista faseFinalGrupo1"
        "Si la lista midiera 8, la lista seria [0, 1, 2, 3] (dejando afuera el cuatro)"
        return list(range(0, int((len(self._faseFinalGrupo1) / 2))))
    
    def ListaDeMitadLongitudHastaLaLongitudDeLaFaseFinalDelGrupo2(self) -> list:
        return list(range(int(len(self._faseFinalGrupo2) / 2), len(self._faseFinalGrupo2)))

    #----------------------------------------------------------------------------------
    def jugarCopa(self, temporada : int, esConIdaYVuelta : bool = False) -> None:
        "Prec. Deben haber si o si una cantidad de ligas que sean el numero dos o cualquier múltiplo de cuatro"
        "Prec. Si esConIdaYVuelta es true, se juega con ida y vuelta"
        print(f"\n🟢🟢🟡🟡🔴🔴 Comenzando la copa de la temporada número {temporada}...")
        self.jugarFaseDeGrupos(esConIdaYVuelta)
        self.jugarFaseEliminatoria(esConIdaYVuelta)
        self.jugarFinal(esConIdaYVuelta)
    
    def jugarCopaConEliminacionDirecta(self, temporada : int, esConIdaYVuelta : bool = False) -> None:
        print(f"\n🟢🟢🟡🟡🔴🔴 Comenzando la copa de la temporada número {temporada}...")
        self.establecerGruposFaseFinalParaEliminacionDirecta()
        self.jugarFaseEliminatoria(esConIdaYVuelta) 
        self.jugarFinal(esConIdaYVuelta)

    def anadirParticipantesAGrupos(self) -> None:
        numeroIndice = 0
        for i in range(int(len(self._participantes) / 4)):
            self._listaDeGrupos.append(classLiga.Liga(
                participantes = [
                    self._participantes[numeroIndice],
                    self._participantes[numeroIndice + 1],
                    self._participantes[numeroIndice + 2],
                    self._participantes[numeroIndice + 3]
                ]
            ))
            numeroIndice += 4

    def establecerGruposFaseFinalParaEliminacionDirecta(self) -> None:
        shuffle(self._participantes)
        self._faseFinalGrupo1.clear()
        self._faseFinalGrupo1.extend(self._participantes[
            0 :
            int(len(self._participantes) - (len(self._participantes) / 2))])
        self._faseFinalGrupo2.clear()
        self._faseFinalGrupo2.extend(self._participantes[
            int(len(self._participantes) - (len(self._participantes) / 2)) :
            int(len(self._participantes))])    

    def jugarFecha(self) -> None:
        numeroDeGrupo = 1
        for grupo in self._listaDeGrupos:
            print(f"Grupo número {numeroDeGrupo}:")
            print("")
            numeroDeGrupo += 1
            grupo.jugarFecha()
            grupo.ordenarPorPuntos()
            grupo.imprimirEstadoDeLiga()
            print("")
    

    def jugarFaseDeGrupos(self, esConIdaYVuelta : bool) -> None:
        numeroDeJornada = 1
        for i in range(6 if(esConIdaYVuelta) else 3):
            print(f"Jornada número {numeroDeJornada}: ==========================")
            self.jugarFecha()
            numeroDeJornada += 1
        self.avanzarDeFase()

    def avanzarDeFase(self) -> None:
        for grupo in self._listaDeGrupos:
            self._faseFinalGrupo1.append(grupo.participantes()[0]) 
            self._faseFinalGrupo2.append(grupo.participantes()[1])
        print("Primeros que avanzan a la fase final:")
        print(self.faseFinalGrupo1PorNombre())
        print("")
        print("Segundos que avanzan a la fase final:")
        print(self.faseFinalGrupo2PorNombre())
        print("")
        shuffle(self._faseFinalGrupo1)
        shuffle(self._faseFinalGrupo2)

    def jugarFaseEliminatoria(self, esConIdaYVuelta : bool) -> None:
        while len(self._faseFinalGrupo1) >= 2:
            self.jugarUNAFaseEliminatoria(len(self._faseFinalGrupo1), esConIdaYVuelta)
        
    def jugarUNAFaseEliminatoria(self, numeroDeEquiposAEliminar, esConIdaYVuelta : bool) -> None:
        self.jugarConEnfrentamientos_DelGrupoFinal_(self.ListaDelCeroHastaMitadDeLaLongitudDeLaFaseFinalDelGrupo1(), self._faseFinalGrupo1, esConIdaYVuelta)
        self.jugarConEnfrentamientos_DelGrupoFinal_(self.ListaDeMitadLongitudHastaLaLongitudDeLaFaseFinalDelGrupo2(), self._faseFinalGrupo2, esConIdaYVuelta)
        self.avanzarEliminatoria(numeroDeEquiposAEliminar)
        self.faseFinalGrupo1PorNombre()

    def jugarConEnfrentamientos_DelGrupoFinal_(self, listaDelNumeroDeEnfrentamientos : list, listaDeLaFaseFinal : list, esConIdaYVuelta : bool) -> None:
        for i in listaDelNumeroDeEnfrentamientos:
            print(f"Partido número {i + 1}")
            self.enfrentarAlNumero_DeLAFaseFinalDeGruposYAgregarAlGanadorALista_EnModo_(i, listaDeLaFaseFinal, esConIdaYVuelta)
            print("==========================")
            print("")

    def enfrentarAlNumero_DeLAFaseFinalDeGruposYAgregarAlGanadorALista_EnModo_(self, numeroDePosicion : int, listaDeLaFaseFinal: list, esConIdaYVuelta: bool):
        if(esConIdaYVuelta):
            listaDeLaFaseFinal.append(ganadorEntre_ParaCopas(self._faseFinalGrupo1[numeroDePosicion], self._faseFinalGrupo2[numeroDePosicion])) # TODO
        else: 
            listaDeLaFaseFinal.append(ganadorEntre_ParaCopas(self._faseFinalGrupo1[numeroDePosicion], self._faseFinalGrupo2[numeroDePosicion])) 

    def avanzarEliminatoria(self, numeroTotalDeListaPrevia) -> None:
        for equipo in self._faseFinalGrupo1[0:numeroTotalDeListaPrevia]:
            self._faseFinalGrupo1.remove(equipo)
        for equipo in self._faseFinalGrupo2[0:numeroTotalDeListaPrevia]:
            self._faseFinalGrupo2.remove(equipo)
    
    def jugarFinal(self, esConIdaYVuelta : bool = False) -> None:
        print("¡La gran final de la copa ha comenzado!")
        if(esConIdaYVuelta):
            self._campeon = ganadorEntre_ParaCopas(self._faseFinalGrupo1[0], self._faseFinalGrupo2[0]) # TODO
        else:
            self._campeon = ganadorEntre_ParaCopas(self._faseFinalGrupo1[0], self._faseFinalGrupo2[0])
        print(f"¡{self._campeon.nombre()} es el campeón de la copa!")
        self.reiniciarCopa()

    def reiniciarCopa(self) -> None:
        for grupo in self._listaDeGrupos:
            grupo.reiniciarLiga() 
        self._faseFinalGrupo1.clear()
        self._faseFinalGrupo2.clear()

    def jugarCopaGuardandoResultados(self, rutaArchivo : str, temporada : int, esConIdaYVuelta : bool = False):
        with open(rutaArchivo, "a", encoding = "utf-8") as archivo:
            sys.stdout = archivo
            self.jugarCopa(temporada, esConIdaYVuelta)
        sys.stdout = sys.__stdout__