import os
import multiprocessing

import numpy as np
import albumentations as A
import torch

from torch import nn
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from albumentations.pytorch import ToTensorV2
from sklearn.model_selection import train_test_split

from paths import RAW, GOLDEN
from configs import SEED, TAM_BATCH

class ConjuntoDadosTif(Dataset):
    def __init__(self, lista_arquivos, transformacoes):
        self.lista_arquivos = lista_arquivos
        self.transformacoes = transformacoes

    def __len__(self):
        return len(self.lista_arquivos)

    def __getitem__(self, indice):
        nome = self.lista_arquivos[indice]
        
        path_completo_imagem = os.path.join(RAW, f"{nome}.tif")
        path_completo_mascara = os.path.join(GOLDEN, f"{nome}.png")

        imagem = np.array(Image.open(path_completo_imagem).convert("RGB"))
        mascara = np.array(Image.open(path_completo_mascara).convert("L"))

        mascara_binaria = (mascara > 0).astype(np.int64)

        aumentado = self.transformacoes(image=imagem, mask=mascara_binaria)
        imagem_transformada = aumentado['image']
        mascara_transformada = aumentado['mask'].long()

        return imagem_transformada, mascara_transformada

def pegar_loades(aumento: bool):
    transformacoes_sem_aumento = A.Compose([
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ToTensorV2()
    ])

    transformacoes_com_aumento = A.Compose([
        A.HorizontalFlip(p=0.2),
        A.VerticalFlip(p=0.2),
        A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.1, rotate_limit=45, p=0.2),
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ToTensorV2()
    ])

    arquivos_totais = [
        os.path.splitext(arquivo)[0] 
        for arquivo in os.listdir(RAW) 
        if arquivo.endswith('.tif')
    ]

    arquivos_treino, arquivos_teste = train_test_split(
        arquivos_totais, 
        test_size=0.2, 
        random_state=SEED
    )

    if not aumento:
        dataset_treino_normal = ConjuntoDadosTif(arquivos_treino, transformacoes_sem_aumento)
        dataset_teste_normal = ConjuntoDadosTif(arquivos_teste, transformacoes_sem_aumento)
        carregador_treino = DataLoader(dataset_treino_normal, batch_size=TAM_BATCH, shuffle=True, pin_memory=True)
        carregador_teste = DataLoader(dataset_teste_normal, batch_size=TAM_BATCH, shuffle=False, pin_memory=True)
    else:
        dataset_treino_aumentado = ConjuntoDadosTif(arquivos_treino, transformacoes_com_aumento)
        dataset_teste_aumentado = ConjuntoDadosTif(arquivos_teste, transformacoes_sem_aumento)
        carregador_treino = DataLoader(dataset_treino_aumentado, batch_size=TAM_BATCH, shuffle=True, pin_memory=True)
        carregador_teste = DataLoader(dataset_teste_aumentado, batch_size=TAM_BATCH, shuffle=False, pin_memory=True)

    return carregador_treino, carregador_teste
