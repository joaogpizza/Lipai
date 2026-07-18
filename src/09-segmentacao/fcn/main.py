import os
import torch
import numpy as np
from PIL import Image
import albumentations as A
from albumentations.pytorch import ToTensorV2

import configs as cfg
from paths import RAW, MASCARAS_SEM, MASCARAS_COM
from treino import treinar

def gerar_mascaras(modelo, pasta_destino):
    os.makedirs(pasta_destino, exist_ok=True)
    device = cfg.DEVICE
    modelo.eval()
    
    transformacao_inferencia = A.Compose([
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ToTensorV2()
    ])

    arquivos = [arquivo for arquivo in os.listdir(RAW) if arquivo.endswith('.tif')]

    with torch.no_grad():
        for arquivo in arquivos:
            caminho_imagem = os.path.join(RAW, arquivo)
            
            imagem_pil = Image.open(caminho_imagem).convert("RGB")
            imagem_np = np.array(imagem_pil)
            
            tensor_imagem = transformacao_inferencia(image=imagem_np)['image']
            tensor_imagem = tensor_imagem.unsqueeze(0).to(device)
            
            saidas = modelo(tensor_imagem)
            saida_p = saidas['out']
            
            mascara_predita = (saida_p > 0).squeeze().cpu().numpy()
            
            mascara_visivel = (mascara_predita * 255).astype(np.uint8)
            
            nome_puro = os.path.splitext(arquivo)[0]
            caminho_salvar = os.path.join(pasta_destino, f"{nome_puro}.png")
            Image.fromarray(mascara_visivel).save(caminho_salvar)

if __name__ == '__main__':
    print("Iniciando treinamento SEM aumento de dados...")
    modelo_sem = treinar(False)
    
    print("\nIniciando treinamento COM aumento de dados...")
    modelo_com = treinar(True)
    
    print("\nGerando previsões para o modelo SEM aumento...")
    gerar_mascaras(modelo_sem, MASCARAS_SEM)
    
    print("Gerando previsões para o modelo COM aumento...")
    gerar_mascaras(modelo_com, MASCARAS_COM)
    
    print("Processo finalizado com sucesso!")
