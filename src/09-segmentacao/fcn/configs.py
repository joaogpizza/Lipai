import torch
import torch.nn as nn
from torchvision.models.segmentation import fcn_resnet50, FCN_ResNet50_Weights

SEED = 42
F_LOSS = nn.BCEWithLogitsLoss()
OTIMIZADOR = torch.optim.Adam
TAXA_APRENDIZADO = 1e-4
NUM_EPOCAS = 25
TAM_BATCH = 4
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
SUAVIZACAO = 1e-8

def pegar_modelo():
    modelo = fcn_resnet50(weights=FCN_ResNet50_Weights.DEFAULT)
    modelo.classifier[4] = nn.Conv2d(512,
                                     1,
                                     kernel_size=(1, 1),
                                     stride=(1, 1)
                                    )
    modelo.aux_classifier[4] = nn.Conv2d(256,
                                     1,
                                     kernel_size=(1, 1),
                                     stride=(1, 1)
                                    )
    return modelo
