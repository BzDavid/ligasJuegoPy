import classEquipo as CE
import classLiga as CL
import classCopa as CC
import json

# Para cargar datos del archivo
with open("equipos.json", "r") as listaEquipos:
    equiposCargados = json.load(listaEquipos)
    listaPrimera = [CE.Equipo(**equipo) for equipo in equiposCargados[0]]
    listaSegunda = [CE.Equipo(**equipo) for equipo in equiposCargados[1]]
    listaDeCampeones = [CE.Equipo(**equipo) for equipo in equiposCargados[2]]
    temporada = equiposCargados[3][0]
    del equiposCargados

exo = CL.Confederacion(
    listaPrimeraDiv = listaPrimera,
    listaSegundaDiv = listaSegunda
)

copaInternacional = CC.Copa(
    participantes = listaDeCampeones
)

# El programa
def guardar():
    global temporada
    listaPrimeraJ = [equipo.dict() for equipo in exo.participantesDeLigaPrimera()]
    listaSegundaJ = [equipo.dict() for equipo in exo.participantesDeLigaSegunda()]
    listaDeCampeonesJ = [equipo.dict() for equipo in campeonesSinEquiposDePrimera() + exo.getClasificadosInternacionales()]
    temporada += 1

    with open("equipos.json", "w") as listaEquipos:
        json.dump([listaPrimeraJ, listaSegundaJ, listaDeCampeonesJ, [temporada]], listaEquipos, indent = 4)

def campeonesSinEquiposDePrimera():
    datosDeCampeones = set([equipo.nombre() for equipo in listaDeCampeones])
    datosListaPrimera = set([equipo.nombre() for equipo in exo.participantesDeLigaPrimera()])
    datosListaSegunda = set([equipo.nombre() for equipo in exo.participantesDeLigaSegunda()])
    campeonesSinEquiposDePrimera = (datosDeCampeones - datosListaPrimera) - datosListaSegunda
    return [CE.Equipo(nombre = equipo) for equipo in campeonesSinEquiposDePrimera]

def main():
    exo.jugarTodasLasCompeticionesGuardando(temporada)
    copaInternacional.jugarCopaGuardandoResultados("ligas/Copa_Internacional_Resultados.txt", temporada)
    guardar()

main()