""" Implementação S18A1 """

import os
from pathlib import Path

import cv2
import mahotas
import numpy as np

DIRETORIO = os.path.dirname(os.path.abspath(__file__))
PATH_MASCARAS = os.path.join(DIRETORIO, "data\\mascaras")
PATH_SIMPLES = os.path.join(PATH_MASCARAS, "simples")
PATH_ADAPTATIVA = os.path.join(PATH_MASCARAS, "adaptativa")
PATH_OTSU = os.path.join(PATH_MASCARAS, "otsu")
DATA = Path(os.path.join(DIRETORIO, "data\\raw"))

os.makedirs(PATH_SIMPLES, exist_ok=True)
os.makedirs(PATH_ADAPTATIVA, exist_ok=True)
os.makedirs(PATH_OTSU, exist_ok=True)

for caminho in DATA.iterdir():
    if caminho.suffix.lower() in {".tif", ".tiff"}:
        img = cv2.imread(str(caminho))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        borrada = cv2.GaussianBlur(img, (5, 5), 0)
        
        # Primeiro: simples
        t = 100
        t, mascara = cv2.threshold(borrada,
                                       t,
                                       255,
                                       cv2.THRESH_BINARY_INV
                                    )
        cv2.imwrite(filename=(os.path.join(PATH_SIMPLES, caminho.name)), img=mascara)

        # Segundo: adaptativo
        mascara = cv2.adaptiveThreshold(borrada,
                                       255,
                                       cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY_INV,
                                       11,
                                       4
                                    )
        cv2.imwrite(filename=(os.path.join(PATH_ADAPTATIVA, caminho.name)), img=mascara)

        # Terceiro: Otsu
        t = mahotas.thresholding.otsu(borrada)
        mascara = img.copy()
        mascara[mascara > t] = 255
        mascara[mascara < 255] = 0
        mascara = cv2.bitwise_not(mascara)
        cv2.imwrite(filename=(os.path.join(PATH_OTSU, caminho.name)), img=mascara)
