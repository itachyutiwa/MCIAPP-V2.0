import pandas as pd

benef = pd.read_excel("E:\\CONTROLES DELEGUES MCI-CARE CI\\SN ASCOMA\\data\\SN ASCOMA BENEFS A 2022.xlsx")
cotisation = pd.read_excel("E:\\CONTROLES DELEGUES MCI-CARE CI\\SN ASCOMA\\data\\SN ASCOMA COTISATION 2022.xlsx")
consommation = pd.read_excel("E:\\CONTROLES DELEGUES MCI-CARE CI\\SN ASCOMA\\data\\SN ASCOMA CONSOS 2022.xlsx")

#PRESTA AVEC DATE SOINS APRES DATE SORTIE: BENF x CONSO
merged_df = pd.merge(consommation, benef, on='Num Police', how='inner')
merged_df = merged_df[['Num Police','Date Soins','Date Sortie']].dropna() 
liste_ = list(set(merged_df[(merged_df['Date Soins'].gt(merged_df['Date Sortie']))]['Num Police'].apply(lambda x: str(x).replace(" ",""))))
df = consommation[consommation["Num Police"].apply(lambda x: str(x).replace(" ","")).isin(liste_)]
print(df)