import torch

import configs as cfg
from prep_dados import pegar_loades
from metricas import calcular_dice, calcular_acuracia_pixel, calcular_iou

def treinar(aumento: bool):
    device = cfg.DEVICE
    print(f"Treinando com: {device}")
    modelo = cfg.pegar_modelo()
    modelo.to(device)
    otim = cfg.OTIMIZADOR(modelo.parameters(), lr=cfg.TAXA_APRENDIZADO)
    loader_treino, loader_teste = pegar_loades(aumento)

    for epoca in range(cfg.NUM_EPOCAS):
        modelo.train()
        perda_total_treino = 0.0

        for img, msc in loader_treino:
            img = img.to(device)
            msc = msc.unsqueeze(1).to(device).float()

            otim.zero_grad()

            saidas = modelo(img)
            saida_p = saidas['out']
            saida_a = saidas['aux']

            perda_p = cfg.F_LOSS(saida_p, msc)
            perda_a = cfg.F_LOSS(saida_a, msc)
            perda = perda_p + 0.4*perda_a

            perda.backward()
            otim.step()
            perda_total_treino += perda.item()
        
        modelo.eval()
        perda_total_teste = 0.0
        dice_total = 0.0
        acuracia_total = 0.0
        iou_total = 0.0

        with torch.no_grad():
            for img, msc in loader_teste:
                img = img.to(device)
                msc = msc.unsqueeze(1).to(device).float()

                saidas = modelo(img)
                saida_p =saidas['out']

                perda = cfg.F_LOSS(saida_p, msc)
                perda_total_teste += perda.item()

                dice_total += calcular_dice(saida_p, msc)
                acuracia_total += calcular_acuracia_pixel(saida_p, msc)
                iou_total += calcular_iou(saida_p, msc)
        print(f'Epoca {epoca+1}:')
        print(f'- Perda no treino: {perda_total_treino/len(loader_treino):.4f}')
        print(f'- Perda no teste: {perda_total_teste/len(loader_teste):.4f}')
        print(f'- DICE: {dice_total/len(loader_teste):.4f}')
        print(f'- Pixel Accuracy: {acuracia_total/len(loader_teste):.4f}')
        print(f'- IoU: {iou_total/len(loader_teste):.4f}')

    return modelo