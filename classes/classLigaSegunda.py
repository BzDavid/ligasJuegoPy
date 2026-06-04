import classLiga as CL
class LigaSegunda(CL.Liga):
    def __init__(self, participantes: list):
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
