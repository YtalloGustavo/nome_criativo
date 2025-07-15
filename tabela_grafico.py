import pandas as pd
import matplotlib.pyplot as ptt

tabela = pd.DataFrame({
    'Idades': [19, 45, 31, 72],
    'Nomes': ['Ytallo', 'João', 'Maria', 'Kid Bengala']
})

ptt.hist(tabela['Idades'])