import fitz                 #Abre y lee pdf
from PIL import Image       #Abre las imagene para hacer lecturas
import pytesseract as tess         #Reconocimiento Obtico de Imagenes
import io


def elemnts():
    dirPdf = "pdf/leer_pdf.pdf"

    pdf = fitz.open(dirPdf)

    pagina = pdf.load_page(0)
    img_list = pagina.get_images(full=False)
    rxs = img_list[0][0]
    base_image = pdf.extract_image(rxs)
    img_bytes = base_image["image"]

    image = Image.open(io.BytesIO(img_bytes))
    text = tess.image_to_string(image)
    print(text)
elemnts()