"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
 
    texto=['sexo','tipo_de_emprendimiento','idea_negocio','línea_credito']
    for i in texto:
        df[i]=df[i].str.upper().str.replace('.','').str.replace('-','').str.replace('_','').str.replace(' ','')
    df.monto_del_credito=df['monto_del_credito'].str.replace('$','').str.replace(',','').astype(float)
    df.fecha_de_beneficio=pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)
    df.barrio=df['barrio'].str.upper().str.replace('_','-').str.replace('-',' ')

    df=df.dropna()
    df=df.drop_duplicates()

    return df
