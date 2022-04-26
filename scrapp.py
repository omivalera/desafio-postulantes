import pandas as pd
import json

#Se obtiene la url del sitio
url = 'https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714'

#Se obtiene los datos de la tabla CSV y se guardan en una variable 'df'
##La tabla es genera mediante Javascript el cual obtiene la informacion de un archivo CSV y lo plasma en la tabla
###En este caso se tomaron los datos del archivo CSV.
df = pd.DataFrame(pd.read_csv(url + '.csv', sep=';', nrows=None, header=0, index_col=False, encoding='utf-8'))
df.shape


#Convertimos y ordenamos los datos CSV en JSON
data_json = df.to_json(
    'scrappdata.json',
    orient='records', 
    double_precision = 10, 
    force_ascii = False, 
    date_unit = "ms", 
    default_handler = 
    None, 
    indent=4
    )
