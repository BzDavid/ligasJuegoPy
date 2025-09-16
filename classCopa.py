from random import shuffle
import classLiga
import sys
from logica import ganadorEntre_
class Copa:
    def __init__(self, participantes) -> None:
        self._participantes = participantes
        self._listaDeGrupos = []
        self._faseFinalGrupo1 = []
        self._faseFinalGrupo2 = []
        shuffle(self._participantes)
        self.anadirParticipantesAGrupos()
        self._campeon = None

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

    def campeon(self):
        return self._campeon

    def anadirListaDeParticipantes_(self, unaLista : list) -> None:
        self._participantes.extend(unaLista)
        self._listaDeGrupos.clear()
        self.anadirParticipantesAGrupos()
    

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
    

    def jugarCopa(self, temporada : int) -> None:
        print(f"\n🟢🟢🟡🟡🔴🔴 Comenzando la copa de la temporada número {temporada}...")
        self.jugarFaseDeGrupos()
        self.jugarFaseEliminatoria()
        self.jugarFinal()
    

    def jugarCopaEliminacionDirecta(self, temporada : int) -> None:
        print(f"\n🟢🟢🟡🟡🔴🔴 Comenzando la copa de la temporada número {temporada}...")
        self.establecerGruposFaseFinalParaEliminacionDirecta()
        self.jugarFaseEliminatoria() 
        self.jugarFinal()
    

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
        numeroDeGrupo = 1
    

    def jugarFaseDeGrupos(self) -> None:
        numeroDeJornada = 1
        for i in range(3):
            print(f"Jornada número {numeroDeJornada}: ==========================")
            self.jugarFecha()
            numeroDeJornada += 1
        numeroDeJornada = 1
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
    

    def jugarFaseEliminatoria(self) -> None:
        while len(self._faseFinalGrupo1) >= 2:
            self.jugarUNAFaseEliminatoria(len(self._faseFinalGrupo1))
        
    def jugarUNAFaseEliminatoria(self, numeroDeEquiposAEliminar) -> None:
        self.jugarConEnfrentamientos_DelGrupoFinal_(list(range(0, int((len(self._faseFinalGrupo1) / 2)))), self._faseFinalGrupo1)
        self.jugarConEnfrentamientos_DelGrupoFinal_(list(range(int(len(self._faseFinalGrupo2) / 2), len(self._faseFinalGrupo2))), self._faseFinalGrupo2)
        self.avanzarEliminatoria(numeroDeEquiposAEliminar)
        self.faseFinalGrupo1PorNombre()

    
    def jugarConEnfrentamientos_DelGrupoFinal_(self, listaDelNumeroDeEnfrentamientos, listaDeLaFaseFinal) -> None:
        for i in listaDelNumeroDeEnfrentamientos:
            print(f"Partido número {i + 1}")
            listaDeLaFaseFinal.append(ganadorEntre_(self._faseFinalGrupo1[i], self._faseFinalGrupo2[i]))
            print("==========================")
            print("")

    def avanzarEliminatoria(self, numeroTotalDeListaPrevia) -> None:
        for equipo in self._faseFinalGrupo1[0:numeroTotalDeListaPrevia]:
            self._faseFinalGrupo1.remove(equipo)
        for equipo in self._faseFinalGrupo2[0:numeroTotalDeListaPrevia]:
            self._faseFinalGrupo2.remove(equipo)
    
    def jugarFinal(self) -> None:
        print("¡La gran final de la copa ha comenzado!")
        self._campeon = ganadorEntre_(self._faseFinalGrupo1[0], self._faseFinalGrupo2[0])
        print(f"¡{self._campeon.nombre()} es el campeón de la copa!")
        self.reiniciarCopa()

    def reiniciarCopa(self) -> None:
        for grupo in self._listaDeGrupos:
            grupo.reiniciarLiga() 
        self._faseFinalGrupo1.clear()
        self._faseFinalGrupo2.clear()

    def jugarCopaGuardandoResultados(self, rutaArchivo : str, temporada : int):
        with open(rutaArchivo, "a", encoding = "utf-8") as archivo:
            sys.stdout = archivo
            self.jugarCopa(temporada)
        sys.stdout = sys.__stdout__
 
# TODO: Luego veo cómo implementar la ida y vuelta