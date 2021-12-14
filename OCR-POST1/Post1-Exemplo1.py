import pytesseract as ocr
import cv2


def visualizar(image_path):
    imagem = cv2.imread(image_path)
    cv2.imshow("Imagem 1", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return imagem


def OCR(imagem):
    print(ocr.image_to_string(imagem))


if __name__=="__main__":
    ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image_path = r"D:\Arquivos Pessoais\Faculdade\Python\Tesseract\imagens\Imagem_2.png"
    imagem  = visualizar(image_path)
    OCR(imagem)
