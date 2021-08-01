#-*- encoding: utf-8 -*-
import os
import jinja2
import codecs
import re
from jinja2 import Template
import subprocess
import time as time_old

## aqui va lo del template
def getTemplate(tpl_path):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename)

scriptDirectory = os.path.dirname(os.path.abspath(__file__))
print(scriptDirectory)



###################################                 Parameters to build render template         #########################
###################################                 esto debe construirse con queries           #########################
loc_img_path = os.path.join(scriptDirectory,"img","img001.jpg")
loc_img_path = loc_img_path.replace(os.path.sep,"/")
print(loc_img_path)
proyecto = "Colibrí de la Montaña"
etapas = [(1,5),(6,15),(16,17),(18,20),(21,99)]
n_etapas = len(etapas)
etapa = 2
duracion_obra = 1457
modulo = "Pueblito"
fase = "Construcción"
texto1 = """El componente “Pueblo” se construirá a lo largo de dos fases (años 1 al 10) e integrará edificaciones relacionadas con actividades hoteleras y residenciales, actividades sociales, deportivas, artísticas y culturales, actividades comerciales y de servicios, pesca y venta de productos frescos del mar.

La fase 1 incluirá la construcción de dos hoteles boutique así como múltiples villas residenciales para alojar a visitantes (véase la tabla Construcción de producto inmobiliario para esta fase), familias de pescadores locales, trabajadores y operadores del condominio. Para las actividades comerciales y de servicios se construirán 25 edificaciones consistentes en tres restaurantes, cuatro mercados de misceláneos y productos del mar, siete comercios de productos diversos, una capilla, un módulo de escamoche, almacén y lavado de pescado, dos bodegas de refrigeración, un módulo de baños públicos y bodega, cinco establecimientos de servicios varios tales como un consultorio de atención médica de primer contacto, delegación municipal, una lavandería y dos oficinas. Para las actividades recreativas y culturales, en esta fase se construirá un gimnasio. Se construirá un estacionamiento para facilitar el ingreso a los hoteles boutique y áreas aledañas.

La totalidad de las edificaciones de este componente se clasificarán en dos sistemas constructivos: palafitos y edificación convencional (ver sistemas constructivos al final de este apartado), y respetarán una altura máxima de 8 m o dos niveles (incluyendo la planta baja y tomando en cuenta la altura a nivel de piso natural) para mantener la visibilidad hacia la costa; de acuerdo a lo que establece el POEL en relación a las edificaciones que se ubiquen a una distancia menor a 200 m de la Zona Federal Marítimo Terrestre.

La ubicación donde se desplantará este componente coincide con la actual localización del punto público de acceso vehicular a la playa, en donde existe un asentamiento humano de familias de pescadores conformado por seis palapas o enramadas, donde viven itinerantemente alrededor de 12 familias (ver Medidas de responsabilidad social).

Además, en este sitio se encuentra la infraestructura que actualmente alberga las instalaciones del Campamento de Conservación de Tortugas Marinas administrado por la Comisión Nacional de Áreas Naturales Protegidas (CONANP) en Chalacatepec. Dicha infraestructura será remplazada por instalaciones nuevas y diseñada de acuerdo al programa de necesidades apegado a los requerimientos de la normatividad ambiental vigente; para tal efecto, será necesario demoler las actuales (ver Demolición de las instalaciones del actual Campamento Tortuguero) y el Campamento será reubicado con la finalidad de mejorar las condiciones constructivas y operativas de las actuales instalaciones.

Además de la superficie edificable, como parte de las áreas exteriores del componente se construirán vialidades secundarias y estacionamientos de empedrado asentado en arena (ver Sistema constructivo de vialidades secundarias convencionales); terrazas y explanadas, áreas verdes ornamentales y deportivas, dos albercas y diversos andadores de acceso al mar; todo esto empleando sistemas constructivos convencionales.

Se construirán las redes secundarias de infraestructura hidráulica, sanitaria y de agua tratada requeridas para garantizar el abastecimiento de agua potable y la conducción del agua residual hacia su proceso de tratamiento, y desde el mismo, de vuelta a su origen para ser reutilizada en el riego de áreas verdes ornamentales. El componente cuenta con su propia Planta de Tratamiento al interior del mismo (ver componente Plantas de Tratamiento de aguas residuales y manejo de aguas residuales) y una línea de descarga de excedentes de agua tratada hasta un estanque artificial.

Se construirán además las obras secundarias de infraestructura eléctrica de baja tensión y de telecomunicaciones. La siguiente tabla muestra la totalidad de las redes de infraestructura a implementarse en esta fase."""

texto2 = """Previo al inicio de los procesos de obra, las actividades del componente incluyen la construcción de edificaciones de carácter provisional denominadas Obras temporales, las cuales se ubicarán en la brecha existente que bordea el componente al límite sureste así como en el sitio donde será la explanada central del componente el cual presenta Cobertura No Forestal; dichos espacios tendrán la finalidad de servir como áreas auxiliares de trabajo y almacenamiento desde donde los trabajadores se desplazarán al lugar de trabajo corres-pondiente. Estas obras no formarán parte del componente pero son necesarias para alber-gar de forma temporal trabajadores, insumos, maquinaria, equipos, etc.; y serán retiradas una vez concluida la totalidad del componente al término de la fase 2."""








tabla1 = [["Tipo de red", "VFO", "DTF", "CNF"],
          ["Hidráulica", 1.4, 0.3, 0.2],
          ["Sanitaria", 1.4, 0.4, 0.2],
          ["Agua tratada", 1.6, 0.4, 0.2],
          ["Telecomunicaciones", 1.2, 0.6, 0.2],
          ["Eléctrica aérea", 0.2, 0, 0.1],
          ["Eléctrica subterránea", 1.0, 0.5, 0.3]]
titulo1 = "Longitudes de infraestructura a implementar por categoría del POEL (km)"
anchos1 = [5,"N","N","N"]

titulo2 = "Frecuencia de actividades de obras provisionales"
tabla2 = [["Actividades", "Jornadas/fase"],
["Recepción y distribución de insumos", 1457],
["Administración de las instalaciones", 1457],
["Limpieza y revisión de las instalaciones, incluye: talleres, bodegas y casetas; revisión de muebles de baño como lavabos, inodoro, coladeras, así como grifos y cañerías", 625],
["Almacenamiento de equipos, maquinaria, refacciones y herramienta", 1457],
["Descanso, preparación y alimentación del personal", 182],
["Limpieza general y recolección de residuos y aguas residuales", 273],
["Vigilancia de las instalaciones", 4372],
["Mantenimiento de áreas de circulación, patios y áreas exteriores.", 31],
["Revisión y limpieza de las instalaciones y equipos de cocina", 5],
["Mantenimiento menor de maquinaria", 165]]


anchos2 = [7,"N"]


titulo3 = "Datos generales del componente para esta fase"

tabla3 = [["Superficie aprovechable total (ha)", 6.74],
["Superficie edificable (ha)", 1.30],
["Superficie a construir no edificable (ha)", 5.45],
["Macrolotes del plan maestro", "Pueblo"],
["UGA POEL", "101, 151"],
["Niveles máximos construidos", 2],
["Cuartos totales construidos", 150]]
anchos3 = [7,"N"]

titulo4 = "Implementación de procesos constructivos por tipo de ecosistema"
header4 = ["Proceso constructivo", "Categoría del POEL", "Superficie (ha)"]
dicc4 = {"Palafitos": [["Vegetación forestal", 0.29],
	                   ["Duna Terciaria Vegetación forestal", 0.47],
	                   ["Duna Terciaria Cobertura no forestal", 0],
	                   ["Cobertura no forestal", 0.24]],
"Edificaciones convencionales":	[["Vegetación forestal", 0.27],
	                             ["Duna Terciaria Vegetación forestal", 0.02],
	                             ["Cobertura no forestal", 0]],
"Vialidades secundarias":	[["Vegetación forestal", 0.98],
	                         ["Duna Terciaria Vegetación forestal", 0.31],
	                         ["Cobertura no forestal", 0.13]],
"Albercas convencionales": [["Duna Terciaria Vegetación forestal", 0.01],
                            ["Cobertura no forestal", 0.01]],
"Cuerpo de agua artificial": [["Vegetación forestal", 0.02]],
"Áreas verdes ornamentales": [["Vegetación forestal", 0.06],
                            ["Duna Terciaria Vegetación forestal", 0.09],
                            ["Duna Terciaria Cobertura no forestal", 0],
                            ["Cobertura no forestal", 0.03]],
"Terrazas, patios y explanadas": [["Vegetación forestal", 1.38],
                                ["Duna Terciaria Vegetación forestal", 1.65],
                                ["Duna Terciaria Cobertura no forestal", 0.01],
                                ["Cobertura no forestal", 0.49]],
"Instalación hidrosanitaria y de agua tratada secundaria": [["Vegetación forestal", 0],
                                                            ["Duna Terciaria Vegetación forestal", 0],
                                                            ["Duna Terciaria Cobertura no forestal", 0],
                                                            ["Cobertura no forestal", 0]],
"Instalación eléctrica aérea secundaria": [["Vegetación forestal", 0.21],
                                           ["Cobertura no forestal", 0.08]],
"Instalación eléctrica y de telecomunicaciones subterránea secundaria": [["Vegetación forestal", 0],
                                                                        ["Duna Terciaria Vegetación forestal", 0],
                                                                        ["Cobertura no forestal", 0]],
"Demolición de Campamento": [["Tortuguero actual Cobertura no forestal", 0.10],
                            ["Obras provisionales temporales Cobertura no forestal", 0.24]]}


anchos4 = [2.4,4,"N"]

titulo5 = "Generación de aguas residuales para esta fase"
tabla5 = [["Tipo", "Unidad", "Cantidad"],
["Domésticas", "m³", 0],
["Industriales", "m³", 628],
["Agrícolas y pecuarias", "m³", 0]]
totales5 = ["Total", 628]
anchos5 = [5,"N","N"]


titulo6 = "Generación de residuos para esta fase (t)"
tabla6 = [["Tipo", "Cantidad"],
["Residuos sólidos urbanos", 4.3],
["Residuos de manejo especial", 10.6],
["Residuos peligrosos", 0.0]]
totales6 = ["Total", 14.9]
anchos6 = [6,"N"]

titulo7 = "Personal"
header7 = [[["Tipo","\multirow{2}"],["Cantidad por categoría del POEL","\multicolumn{4}"],["Total fase","\multirow{2}"]],
           [["~"],["CNF"],["SBC"],["VSS"],["VFO"],["~"]]]
tabla7 = [["Obrero/Jornalero", 20, 10, 10, 0, 39],
["Oficial/Técnico", 15, 8, 8, 0, 31],
["Especializado", 3, 2, 2, 0, 7]]
totales7 = ["Total", 38, 20, 20, 0, 77]
anchos7 = [4,"N","N","N","N","N"]



titulo8 = "Construcción de producto inmobiliario para esta fase"
header8 = [[["Categorías del POEL","\multirow{2}"], ["Cobertura del suelo","\multirow{2}"], ["Número de cuartos", "\multicolumn{3}"]],
            [["~"],["~"],["Hoteleros"], ["Villas*"], ["Total"]]]


dicc8 = {"Vegetación forestal":         [["Matorral crasicaule", 11, 18, 56],
                                        ["Matorral espinoso costero", 11, 0, 11]],
"Duna Terciaria Vegetación forestal":   [["Matorral crasicaule", 0, 0, 0],
                                        ["Matorral espinoso costero", 40, 10, 65]],
"Duna Terciaria Cobertura no forestal": [["Cobertura alterada", 0, 0, 0]],
"Cobertura no forestal":                [["Cobertura alterada", 18, 0, 18]]}
totales8 = ["Gran Total", 150]
anchos8 = [3,3,"N","N","N"]



#######################################              end parameters                     #######################


hlines = ["~~-~~","~~~~~","~~-~~","~~-~~"]
for e in range(0,n_etapas):
    hlines[0] += "~"
    hlines[1] += "-"
    hlines[2] += "-"
    hlines[3] += "~"
hlines[0] += "~"
hlines[1] += "~"
hlines[2] += "~"
hlines[3] += "~"

context = {
    'loc_img_path': loc_img_path,
    'proyecto': proyecto,
    'etapa': etapa,
    'etapas': etapas,
    'n_etapas': n_etapas,
    'hlines': hlines,
    'modulo': modulo,
    'fase': fase,
    'duracion_obra': f"{duracion_obra:,}",
    'texto1': texto1,
    'texto2': texto2,
    'tabla1': tabla1,
    'titulo1': titulo1,
    'anchos1': anchos1,
    'tabla2': tabla2,
    'titulo2': titulo2,
    'anchos2': anchos2,
    'tabla3': tabla3,
    'titulo3': titulo3,
    'anchos3': anchos3,
    'titulo4': titulo4,
    'anchos4': anchos4,
    'dicc4': dicc4,
    'header4': header4,
    'titulo5': titulo5,
    'tabla5': tabla5,
    'totales5': totales5,
    'anchos5': anchos5,
    'titulo6': titulo6,
    'tabla6': tabla6,
    'totales6': totales6,
    'anchos6': anchos6,
    'titulo7': titulo7,
    'tabla7': tabla7,
    'totales7': totales7,
    'anchos7': anchos7,
    'header7': header7,
    'titulo8': titulo8,
    'header8': header8,
    'dicc8': dicc8,
    'totales8': totales8,
    'anchos8': anchos8
}
tex_path = os.path.join(scriptDirectory,"test_ficha.tex")
print(tex_path)
print(os.path.join(scriptDirectory,"template_ficha.jinja"))
template = getTemplate(os.path.join(scriptDirectory,"template_ficha.jinja"))

with codecs.open (tex_path, "w", "utf-8") as miFile:
    output = template.render(context)
    output = re.sub(r'\{§', '{', output)
    output = re.sub(r'§\}', '}', output)

    # jinja returns unicode - so `output` needs to be encoded to a bytestring
    # before writing it to a file
    miFile.write(output)

tex_path = tex_path.replace("/", "\\\\")

print(tex_path)

time_old.sleep(1)
os.chdir(scriptDirectory)
subprocess.run(["xelatex", "-interaction=nonstopmode", tex_path],shell=True)
