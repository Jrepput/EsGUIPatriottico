import urllib.request
import numpy as np
import cv2
from cairosvg import svg2png
import PySimpleGUI as sg

pb = 80
pn = 10
img = np.ones((500, 800), dtype=np.uint8) * 255
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img[0:500, 000:250] = [0, 255, 0]
img[0:500, 550:800] = [0, 0, 255]
img[100:400, 225:275] = [0, 0, 0]
img[350:400, 275:350] = [0, 0, 0]
img[100:150, 450:650] = [0, 0, 0]
img[100:400, 450:500] = [0, 0, 0]
img[350:400, 450:650] = [0, 0, 0]
img[250:400, 600:650] = [0, 0, 0]
img[250:300, 550:600] = [0, 0, 0]
print(img.shape)

'''url = "https://en.wikipedia.org/wiki/File:Flag_of_Italy.svg"
urllib.request.urlretrieve(url, "Flag_of_Italy.svg")
img = svg2png(bytestring=url)
pil_img = Image.open(BytesIO(img)).convert('RGBA')
pil_img.save('output/pil.png')
cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGBA2BGRA)
cv2.imwrite('cv.png', cv_img)
img = cv2.imread("cv.png")'''

sg.theme('DarkAmber')

gui_image = cv2.imencode('.png', img)[1].tobytes()
layout = [ [sg.Image(data=gui_image)] ]

window = sg.Window('Bandiera Italiana', layout)

while True:
  event, values = window.read()
  if event == sg.WINDOW_CLOSED or event == 'Quit':
    break

window.close()