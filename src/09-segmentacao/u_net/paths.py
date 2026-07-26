import os

DIRETORIO = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(DIRETORIO, "data")
RAW = os.path.join(DATA, "raw")
GOLDEN = os.path.join(DATA, "golden")
MASCARAS = os.path.join(DATA, "mascaras")
MASCARAS_SEM = os.path.join(MASCARAS, "sem_aumento")
MASCARAS_COM = os.path.join(MASCARAS, "com_aumento")
