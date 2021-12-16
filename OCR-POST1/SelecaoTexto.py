import pytesseract as ocr
import cv2
from pytesseract import Output
from PIL import ImageFont, Image, ImageDraw
import numpy as np




class BoxTexto:

    def __init__(self, img_path, nome_janela="Imagem"):

        self.img_path = img_path
        self.nome_janela =  nome_janela
        self.Imagem = cv2.imread(self.img_path)


    def visualizar_img(self):

        cv2.imshow(str(self.nome_janela), self.Imagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def escreve_texto(self, texto, x, y, img, fonte=r"D:\Arquivos Pessoais\Faculdade\Python\Tesseract\Fontes\calibri.ttf", tamanho_texto=32):
        
        fonte = ImageFont.truetype(fonte, tamanho_texto) 
        img_pil = Image.fromarray(img) #estamos trabalhando com um tipo numpy.ndarray precisamos converter para o formato do PIL imagem.
        draw = ImageDraw.Draw(img_pil) #Passamos a imagem que queremos fazer o desenho em cima.
        draw.text((x, y - tamanho_texto), texto, font=fonte) #escolhemos a posição x, a posição y deslocamos o tamanho do texto para ficar uniforme, texto e fonte
        img = np.array(img_pil) #transformamos em um formato np.array
        return img

  

    def draw_box(self, confiança=40, cor=(255,100,0)):

        self.resultado = ocr.image_to_data(self.Imagem, lang="por", output_type=Output.DICT)
        array = []
        img = self.Imagem.copy()
        for i in range(0,len(self.resultado["text"])):

            if float(self.resultado["conf"][i]) > confiança:
                array.append(i)


        for i in array:

            x=self.resultado["left"][i]
            y=self.resultado["top"][i]
            w =self.resultado["width"][i]
            h =self.resultado["height"][i]
            cv2.rectangle(img,(x,y), (x+w, y+h),cor, 2)
            texto = self.resultado["text"][i]
            #cv2.putText(img, texto, (x, y-10),cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0,0,255))
            img =self.escreve_texto(texto, x, y, img)

        cv2.imshow("box",img)            
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    
    
    




if __name__=="__main__":
    
    image_path = r"D:\Arquivos Pessoais\Faculdade\Python\Tesseract\imagens\teste02.jpg"
    imagem1 = BoxTexto(image_path)
    imagem1.visualizar_img()
    imagem1.draw_box()