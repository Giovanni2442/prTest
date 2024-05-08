import fitz                 #Abre y lee pdf
from PIL import Image       #Abre las imagene para hacer lecturas
import pytesseract  as tess       #Reconocimiento Obtico de Imagenes
import io

tess.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe' 

def pruebas():
    #Ruta del Archivo pdf
    pdfDoc = "pdf/leer_pdf.pdf"

    #Abrir el archivo pdf
    doc = fitz.open(pdfDoc)

    pagina = doc.load_page(0)
    text = pagina.get_text("text")

    img = pagina.get_images(full=False)

    
    #img = doc.get_page_images(0,full = False)
    print(text)
    print(img)
    #print(img)

def imgpr():
    img = "pdf/img.png"
    img_open = Image.open(img)
    text = tess.image_to_string(img_open)
    print(text)

def elemnts():

#Notas :
#   - Hacer un ciclo for para capturar las imagenes, ya que solo captura el logo
#   - hacer un analisis lexico para interpretar la información ya extraida
#   - colocar todo en una matriz u arreglo
    Array = []
    
    dirPdf = "pdf/D-0759_R-2.pdf"

    pdf = fitz.open(dirPdf)
    page = pdf.load_page(0)

    #Obtener Texto del Pdf
    text = page.get_text("text")
    lines = text.split("\n")

    #print(lines)
    #print(text)

    #Pasar el texto obtenido a una nueva lista 
    for i in text.splitlines():
        if i  != " ":
            Array.append(i)
            #print(Array)

    #extrClGaug(Array)

    for j in range(len(Array)):
        print(f"{j}  : {Array[j]}")

    #--Diccionarios de Datos por Sección --
    GENERAL = {
        "FIN_PROCESO" : Array[0],
        "FECHA" : Array[349],
        "PT" : Array[0],         #Colocar entradas de texto en estos casos
        "PTPR" : Array[0],       #Colocar entradas de texto en estos casos
        "UNIDAD" : Array[0],      #Colocar entradas de texto en estos casos
        "CLIENTE" : Array[350],
        "PRODUCTO" : Array[353],
        "COD_PC" : Array[351],
        "ASESOR" :  Array[354],
        "TIPO_EMPAQUE" : Array[355],
        "ESTC_PROD" :  Array[358],
        "PROD_EMP" : Array[357]
    }

    EXTRUSION = {
        "MATERIAL" : Array[360],
        "DINAJE" : Array[361],
        "FORMULA" : Array[362],
        "FORMULA_2" : Array[363],

        #"CALIBRE_MICRAS" : extrClGaug(Array)[1],
        #"CALIBRE_GAUGES" : extrClGaug(Array)[0],
        "TOLERANCIA" : extrClGaug(Array)[2],
        "TIPO_BOBINA" : Array[365],
        "TIPO_TRATADO" : Array[366],
        "ANCHO_BOBINA_MTS" : Array[366],
        "ANCHO_BOBINA_CM" : Array[366],
        "TOLERANCIA" : Array[366],

    }

    #print(extrClGaug(Array)[2])
    #print(int(extrAnchBob(Array)[0]) / 100)

    for i in range(len(extrAnchBob(Array))):
        pass
        #print(f"Index : {i}  : {extrAnchBob(Array)[i]}")
    #extrAnchBob(Array)


# -- FUNCIONES DE CALCULO --
#NOTA : Colocar todas las funciones en una clase y obtenerlas como Objetos

    # --EXTRUSION --

#Funcion: Calcula el calibre en Micars con base al calibre en GAUGES
def extrClGaug(txt):
    micras = txt[364]
    res = micras.split(" ") #Separa los elementos al encontrar algun espacio
    #Mejorar la logica del "if"
    #print(len(res))
    if len(res) == 4:    
        res2 =  ( int(res[0]) / 4 )
        res[1] = res2   #Remplaza el elemento del Split con el resultado de res2
    else:
        res2 =  ( int(res[0]) / 4 )
        res[1] = res2   #Remplaza el elemento del Split con el resultado de res2
        res[2] = 'N/A'
    return res

def extrAnchBob(txt):
    arrayPru = ["",""]
    aux = []
    ancho = txt[367]
    res = ancho.split(" ")
    
    for i in range(len(res)):
        if res[i].strip():       # Se arregla un error donde el elemento "4" esta vacio 
            aux.append(res[i])
            #print(f"{i} : {res[i]}")
            #print(f"{i} : {res[i]}")
    #print(len(aux))

    #Verificar si existe alguna tolerancia para
    #el ancho de la bobina

    #Code aux
    #aux.index("N/A")

    if len(aux) == 4:
        aux.append("N/A")
        return aux
    else:
        return aux
    #print(aux.index())
    #return aux

elemnts()
#imgpr()
#pruebas()
    

    

