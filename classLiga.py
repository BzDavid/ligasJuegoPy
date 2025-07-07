import classEquipo as CE
class LigaPrimera(CE.Liga):
    def __init__(self, participantes):
        super().__init__(participantes)

    def jugarLiga(self) -> None:
        super().jugarLiga()
        print(f"¡El campeón de la liga es: {self._participantes[0].nombre()}!")
        print(f"{self._participantes[len(self._participantes) - 2].nombre()} va a jugar la promoción para permanecer en la liga!")
        print(f"El equipo que desciende es: {self._participantes[len(self._participantes) - 1].nombre()}")
        print("")
        self.imprimirEstadisticasTotalesDeEquipos()

    def queEquiposDescienden(self) -> list:
        return [self._participantes[int((self.participantes().size() - 2))].nombre(), self._participantes[int((self.participantes().size() - 1))].nombre()]

    def jugarPromocion(self, otraLiga) -> None:
        print("¡La promoción ha comenzado!")
        CE.jugarPartido(
            self._participantes[len(self._participantes) - 2],
            otraLiga.participantes()[1]
        )
           
        CE.jugarPartido(
            otraLiga.participantes()[1],
            self._participantes[len(self._participantes) - 2],
        )

class LigaSegunda(CE.Liga) :
    def __init__(self, participantes):
        super().__init__(participantes)

    def jugarLiga(self):
        super().jugarLiga()
        print(f"Campeón y ascenso de la liga: {self._participantes[0].nombre()}")
        print(f"¡{self._participantes[1].nombre()} deberá jugar la promoción para ascender!")
        print("")
        self.imprimirEstadisticasTotalesDeEquipos()
    
    def queEquiposAscienden(self):
        return list(map(lambda unEquipo: unEquipo.nombre(), self._participantes[0:2]))