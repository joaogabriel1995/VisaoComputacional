import pytesseract as ocr
import cv2

def visualizar(imagem):
    cv2.imshow("Imagem_1", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def OCR(imagem_ocr):
    print(ocr.image_to_string(imagem_ocr))



if __name__=="__main__":
    ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    url_imagem = r"D:\Arquivos Pessoais\Faculdade\Python\Tesseract-Curso\imagens\Imagem_1.png"
    imagem = cv2.imread(url_imagem)
    
    visualizar(imagem)
    OCR(imagem)
