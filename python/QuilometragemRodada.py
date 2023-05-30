import random
import pandas as pd

# Geração aleatória de quilometragem por mês
quilometragem_por_mes = [random.randint(20, 5000) for _ in range(1000)]

# Criação do DataFrame com a coluna de quilometragem por mês
df = pd.DataFrame(quilometragem_por_mes, columns=['Quilometragem por Mês'])

# Salvando o DataFrame em um arquivo CSV
df.to_csv('quilometragem.csv', index=False)
