import torch

from configs import SUAVIZACAO

def calcular_dice(saidas, mascaras):
    previsoes = (saidas > 0).float().flatten()
    mascaras = mascaras.flatten()
    
    intersecao = (previsoes * mascaras).sum()
    soma = previsoes.sum() + mascaras.sum()
    
    dice = (2.0 * intersecao + SUAVIZACAO) / (soma + SUAVIZACAO)
    return dice.item()

def calcular_acuracia_pixel(saidas, mascaras):
    previsoes = (saidas > 0).float().flatten()
    mascaras = mascaras.flatten()
    
    corretos = (previsoes == mascaras).sum()
    total = mascaras.numel()
    
    acuracia = corretos / total
    return acuracia.item()

def calcular_iou(saidas, mascaras):
    previsoes = (saidas > 0).float().flatten()
    mascaras = mascaras.flatten()
    
    intersecao = (previsoes * mascaras).sum()
    uniao = previsoes.sum() + mascaras.sum() - intersecao
    
    iou = (intersecao + SUAVIZACAO) / (uniao + SUAVIZACAO)
    return iou.item()
