import pytesseract
from PIL import Image

i = 0
while i < 4:
 img = Image.open(r'C:\Users\pro24\Desktop\convert\pdftest' + str(i) + '.jpg')
 pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
 result = pytesseract.image_to_string(img)
 i += 1
 with open('pdf' + str(i) + '.txt', mode ='w') as file:
  file.write(result)
  print('done')