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

    
    dirPdf = "pdf/FichaTec.pdf"

    pdf = fitz.open(dirPdf)

    """"
    pagina = pdf.load_page(0)
    img_list = pagina.get_images(full=False)
    xref = img_list[0][0]
    base_image = pdf.extract_image(rxs)
    img_bytes = base_image["image"]

    #print(base_image)
    image = Image.open(io.BytesIO(img_bytes))
    image.show()
    text = tess.image_to_string(image)
    print(text)
    """

    page = pdf.load_page(0)
    img_list = page.get_images(full=False)
    xref = img_list[0][0]
    base_image = pdf.extract_image(xref)
    img_bytes = base_image["image"] 
    image = Image.open(io.BytesIO(img_bytes))
    #image.show()
    
    #Obtener Texto del Pdf
    text = page.get_text("text")
    #print(text)

    for i in text.splitlines():
        print(i)
    #print(type(text))
    #print(len(text))
elemnts()
#imgpr()
#pruebas()
    

    

