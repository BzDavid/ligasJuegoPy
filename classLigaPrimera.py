from classLiga import Liga
from logica import jugarIdaYVueltaYDarResultados
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
        return jugarIdaYVueltaYDarResultados(self._participantes[len(self._participantes) - 2], otraLiga.participantes()[1])
    
    def eliminarUltimosDos(self):
        self._participantes.pop(int(len(self._participantes) - 1))
        self._participantes.pop(int(len(self._participantes) - 1))
