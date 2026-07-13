""" Responsável pelo cálculo dos DICEs """

import os
from pathlib import Path

import cv2
import numpy as np

DIRETORIO = os.path.dirname(os.path.abspath(__file__))
PATH_MASCARAS = os.path.join(DIRETORIO, "data\\mascaras")
PATH_SIMPLES = os.path.join(PATH_MASCARAS, "simples")
PATH_ADAPTATIVA = os.path.join(PATH_MASCARAS, "adaptativa")
PATH_OTSU = os.path.join(PATH_MASCARAS, "otsu")
PATH_GOLDEN = Path(os.path.join(DIRETORIO, "data\\golden"))

def calculo_dice(gold, masc, soma):
    intersecao = cv2.bitwise_and(gold, masc)
    inter = 2 * (np.count_nonzero(intersecao))
    soma = inter / ((np.count_nonzero(gold)) + (np.count_nonzero(masc)))
    return soma

soma_simples = 0
soma_adaptativa = 0
soma_otsu = 0
total = 0

for caminho in PATH_GOLDEN.iterdir():
    golden = cv2.imread(str(caminho))

    path_masc_simples = str(os.path.join(PATH_SIMPLES,
                                     (caminho.with_suffix(".tif")).name
                                    ))
    masc_simples = cv2.imread(path_masc_simples)
    soma_simples += calculo_dice(golden, masc_simples, soma_simples)

    path_masc_adaptativa = str(os.path.join(PATH_ADAPTATIVA,
                                     (caminho.with_suffix(".tif")).name
                                    ))
    masc_adaptativa = cv2.imread(path_masc_adaptativa)
    soma_adaptativa += calculo_dice(golden, masc_adaptativa, soma_adaptativa)

    path_masc_otsu = str(os.path.join(PATH_OTSU,
                                     (caminho.with_suffix(".tif")).name
                                    ))
    masc_otsu = cv2.imread(path_masc_otsu)
    soma_otsu += calculo_dice(golden, masc_otsu, soma_otsu)

    total += 1

print(f"Média DICE simples: {soma_simples / total}")
print(f"Média DICE adaptativa: {soma_adaptativa / total}")
print(f"Média DICE otsu: {soma_otsu / total}")
