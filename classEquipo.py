from logica import generar
class Equipo:
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre
        self._puntos = 0
        self._golesAFavor = 0
        self._golesEnContra = 0
        self._golesEnPartido = 0

    def __str__(self):
        return self._nombre
    
    def dict(self):
        return {
            "nombre" : self._nombre 
        }
    
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
        self._golesEnPartido = max(generar() - 2, 0)

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