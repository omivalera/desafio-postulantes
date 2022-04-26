from fastapi import FastAPI, status, HTTPException
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse

import pandas as pd
import json

#Se declaran las variables para manipular el contenido de la tabla
url = 'https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714'
df = pd.read_csv(url + '.csv', sep=';', nrows=None, header=0, index_col=False, encoding='utf-8')
df.shape

#Se inicia FastApi
app = FastAPI()

#Se define una funcion donde se parsea en json el contenido de la tabla
def parse_csv(df):
    res = df.to_json(orient='records', double_precision = 10, force_ascii = False, date_unit = "ms", default_handler = None, indent=4)
    parsed = json.loads(res)
    return parsed

#EndPoints

@app.get('/jsonresponse', tags=["Respuesta en Json"])
def respuesta_Json(url = url + '.csv'):
    return parse_csv(df)     

@app.get("/htmlresponse", tags=["Respuesta en HTML"])
def respuesta_HTML():
    """
    HTML RESPONSE
    En esta operacion se devuelve el valor de la tabla en formato HTML
    """
    return HTMLResponse(content=df.to_html(), status_code=200)