from logica import generar
class Equipo:
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre
        self._puntos = 0
        self._golesAFavor = 0
        self._golesEnContra = 0
        self._golesEnPartido = 0
        self._golesGlobales = 0
        self._partidosGanados = 0
        self._partidosPerdidos = 0
        self._partidosEmpatados = 0
        self._partidosGlobalesJugados = 0
        self._confederacion

    
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
    
    def golesGlobales(self) -> int:
        return self._golesGlobales
    
    def partidosGanados(self) -> int:
        return self._partidosGanados
    
    def partidosPerdidos(self) -> int:
        return self._partidosPerdidos
    
    def partidosEmpatados(self) -> int:
        return self._partidosEmpatados

    def diferenciaDeGoles(self) -> int:
        return self._golesAFavor - self._golesEnContra
    
    def partidosJugados(self) -> int:
        return self._partidosGanados + self._partidosPerdidos + self._partidosEmpatados
    
    def nombre(self) -> str:
        return self._nombre
    
    def confederacion(self):
        return self._confederacion 
    
    def statGoles(self) -> list:
        return [self._golesAFavor, self._golesEnContra, self.diferenciaDeGoles()]
    
    def stats(self) -> list: 
        return [self._nombre, self._puntos, self.diferenciaDeGoles()]

    def fullStats(self) -> list:
        return [self._nombre, self.partidosJugados(), self._partidosGanados, self._partidosEmpatados, self._partidosPerdidos, self._golesAFavor, self._golesEnContra, self.diferenciaDeGoles(), self._puntos] 

    def dicDeStats(self) -> dict:
        return {
            "Equipo" : self._nombre, 
            "PJ" : self.partidosJugados(),
            "PG" : self._partidosGanados,
            "PE" : self._partidosEmpatados,
            "PP" : self._partidosPerdidos,
            "GF" : self._golesAFavor,
            "GC" : self._golesEnContra, 
            "DG" : self.diferenciaDeGoles(),
            "Pts" : self._puntos 
            }
        
    def establecerConfederacion(self, unaConfederacion) -> None:
        self._confederacion = unaConfederacion

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
        self._golesGlobales = 0
        self._partidosGanados = 0
        self._partidosPerdidos = 0
        self._partidosEmpatados = 0

    def sumarDerrota(self) -> None:
        self._partidosPerdidos += 1

    def gana(self, unRival) -> None:
        self._puntos += 3
        self._partidosGanados += 1
        unRival.sumarDerrota()

    def empata(self) -> None:
        self._puntos += 1
        self._partidosEmpatados += 1

    def jugarPartidoIYV(self) -> None:
        if (self._partidosGlobalesJugados == 2):
            self._partidosGlobalesJugados = 0
            self._golesGlobales = 0
        self.jugarPartidoEspecial()
        self.sumarGolesActualesAGolesGlobales()
        self._partidosGlobalesJugados += 1

    def sumarGolesActualesAGolesGlobales(self) -> None:
        self._golesGlobales += self.golesEnPartido

    def reiniciarGolesGlobales(self) -> None:
        self._golesGlobales = 0