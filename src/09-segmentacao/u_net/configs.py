import torch
import torch.nn as nn

from modelo import UNet

SEED = 42
F_LOSS = nn.BCEWithLogitsLoss()
OTIMIZADOR = torch.optim.Adam
TAXA_APRENDIZADO = 1e-4
NUM_EPOCAS = 25
TAM_BATCH = 4
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
SUAVIZACAO = 1e-8

def pegar_modelo():
    modelo = UNet(in_channels=3, num_classes=1, dropout_rate=0.1, batchnorm=True)
    return modelo
