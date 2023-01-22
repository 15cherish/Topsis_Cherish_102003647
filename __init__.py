import pandas as pd
from Topsis_Cherish_102003647.topsis import topsis
df=pd.read_csv('dataaaa.csv')
topsis(df,"0.25,0.25,0.25,0.25,0.25","-,+,+,+,+")
