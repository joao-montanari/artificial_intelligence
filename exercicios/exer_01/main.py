import pandas as pd
import numpy as ny

mistura_01 = [22.02, 23.83, 26.67, 25.38, 25.49, 23.5, 25.9, 24.89]
mistura_02 = [21.49, 22.67, 24.62, 24.18, 22.78, 22.56, 24.46, 23.79]
mistura_03 = [20.33, 21.67, 24.67, 22.45, 22.29, 21.95, 20.49, 21.81]

boxplot = pd.dataframe.boxplot(column=['Grupo 1', 'Grupo 2'], grid = False)
print(boxplot)