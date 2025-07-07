import classEquipo as CE
import classCopa as CC
import classLiga as CL
import sys

calverna = CE.Equipo(
    nombre = "Calverna"
) # Antes "Barco"

monteluz = CE.Equipo(
    nombre = "Monteluz"
) # Antes "Avión"

streinbruck = CE.Equipo(
    nombre = "Streinbr"
) # Antes "Tren"

rodanor = CE.Equipo(
    nombre = "Rodanor"
) # Antes "Coche"

novigrad = CE.Equipo(
    nombre = "Novigrad"
) # Antes "Bicicleta"

lormont = CE.Equipo(
    nombre = "Lormont"
) # Antes "Moto"

boravik = CE.Equipo(
    nombre = "Boravik"
) # Antes "Silenciadores"

veltsen = CE.Equipo(
    nombre = "Veltsen"
) # Antes "Fumetas"

victoria = CE.Equipo(
    nombre = "Victoria"
)

valdonza = CE.Equipo(
    nombre = "Valdonza"
)

cernovia = CE.Equipo(
    nombre = "Cernovia"
)

pardenos = CE.Equipo(
    nombre = "Pardenos"
)

tirana = CE.Equipo(
    nombre = "Tirana"
)

ferrosur = CE.Equipo(
    nombre = "Ferrosur"
)

dravus = CE.Equipo(
    nombre = "Dravus"
)

rogar = CE.Equipo(
    nombre = "Rogar"
)

#CE.Equipos de la Copa Internacional
rojos = CE.Equipo(
    nombre = "Rojos"
)

verdes = CE.Equipo(
    nombre = "Verdes"
)

negros = CE.Equipo(
    nombre = "Negros"
)

azules = CE.Equipo(
    nombre = "Azules"
)

invictos = CE.Equipo(
    nombre = "Invictos"
)

realistas = CE.Equipo(
    nombre = "Realistas"
)

blanquinegros = CE.Equipo(
    nombre = "Blanquinegros"
)

capitales = CE.Equipo(
    nombre = "Capitales"
)

rapaces = CE.Equipo(
    nombre = "Rapaces"
)

acetitas = CE.Equipo(
    nombre = "Acetitas"
)

fuertes = CE.Equipo(
    nombre = "Fuertes"
)

amplios = CE.Equipo(
    nombre = "Amplios"
)

reyes = CE.Equipo(
    nombre = "Reyes"
)


listaDeCampeones = [
    calverna, #El campeon de la liga
    monteluz, #El subcampeon de la liga
    cernovia, #El campeon de la copa de la primera
    #Los de otros continentes
    rojos,
    verdes,
    negros,
    azules,
    invictos,
    realistas,
    blanquinegros,
    capitales,
    rapaces,
    acetitas,
    fuertes,
    amplios,
    reyes
]

listaPrimera = [
    calverna,
    monteluz,
    streinbruck,
    rodanor,
    boravik,
    lormont,
    veltsen,
    cernovia
]

listaSegunda = [
    victoria,
    valdonza,
    pardenos,
    ferrosur,
    dravus,
    rogar,
    tirana,
    novigrad
]

liga1 = CL.LigaPrimera(
    participantes = listaPrimera
)

liga2 = CL.LigaSegunda(
    participantes = listaSegunda
)

copa1 = CC.Copa(
    participantes = listaPrimera
)

copa2 = CC.Copa(
    participantes = listaSegunda
)

copaInternacional = CC.Copa(
    participantes = listaDeCampeones
)

def initialize():
    print("¡Bienvenido a la simulación de la liga de fútbol!")
    print("Comenzando la temporada...")
    liga1.jugarLiga()
    print("¡La temporada ha terminado!")
    print("")
    liga2.jugarLiga()
    print("¡La temporada ha terminado!")
    print("")
    liga1.jugarPromocion(liga2)
    print("")
    liga1.reiniciarLiga()
    liga2.reiniciarLiga()
    print("Comienzan las copas...")
    copa1.jugarCopa()
    print("")
    copa2.jugarCopa()
    print("Comienza la copa internacional...")
    copaInternacional.jugarCopa()

with open("ligas/test.txt", "a", encoding = "utf-8") as archivo:
    sys.stdout = archivo
    initialize()

sys.stdout = sys.__stdout__