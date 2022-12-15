import cv2
import pytesseract

imagem = cv2.imread("img.jpg")

caminho = r"C:\Users\tulio\AppData\Local\Tesseract-OCR"

pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

texto = pytesseract.image_to_string(imagem)

print(texto)