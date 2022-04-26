# La solución fue desarrollada en Python con FastApi

- Formato de respuesta en Json 
```json
[
  {
    "ID": 1,
    "Razón Social": "BIRCHMOUNT INVESTMENTS LIMITED",
    "País": "CANADÁ",
    "DR Inscripción": "DR XV ",
    "Resolución Inscripción": "7553",
    "Fecha Inscripción": " 08-10-2008",
    "Vigencia Hasta": "jun-21",
    "DR Actualización": "DR XV ",
    "Resolución Actualización": "1327",
    "Fecha Actualización": " 25-06-2020",
    "Estado": "PENDIENTE"
  },
  {
    "ID": 2,
    "Razón Social": "AB SVENSK EXPORTKREDIT",
    "País": "SUECIA",
    "DR Inscripción": "DR XV ",
    "Resolución Inscripción": "8962",
    "Fecha Inscripción": " 10-11-2008",
    "Vigencia Hasta": "jun-22",
    "DR Actualización": "DR XV ",
    "Resolución Actualización": "1687",
    "Fecha Actualización": " 21-07-2021",
    "Estado": "ACTUALIZADO"
  },
  {
    "ID": 3,
    "Razón Social": "BARRICK GOLD (PASCUAL LAMA) LIMITED",
    "País": "JERSEY",
    "DR Inscripción": "DGC ",
    "Resolución Inscripción": "349",
    "Fecha Inscripción": " 12-11-2008",
    "Vigencia Hasta": "jun-22",
    "DR Actualización": "DR XV ",
    "Resolución Actualización": "1791",
    "Fecha Actualización": " 28-07-2021",
    "Estado": "ACTUALIZADO"
  }...
]
```

# Instalación
- pip install fastapi uvicorn pandas
- uvicorn scrapp:app --reload
# Visualización
- Entrar en la documentación interactiva de FastApi [Link]http://127.0.0.1:8000/docs
- Abir endpoint
- Click en Try it Out
- Click Execute
![image]https://raw.githubusercontent.com/omivalera/omivalera.github.io/master/assets/images/h17351.JPG
# Desafio Postulantes

Con el fin de seleccionar a nuestros 2 developers, tenemos el siguente desafio.

De la siguente URL [Link](https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714.html) es necesario crear un código que sea capaz de parsear la pagina web y devolver un json con esta información.
![image](https://user-images.githubusercontent.com/3030497/164536276-9eb79d10-4fb0-4943-a15f-2536a8586330.png)

El JSON de respuesta puede venir en el formato que estimes conveniente.

## Preguntas Frecuentes

- Tipos de entrega, cualquiera de los siguiente sirve
  - API caso generico
  - API caso particular
  - Script para el caso particular
- Lenguaje: El que más te guste
- Plazo de Entrega: Indefinido, iremos entrevistando a los que van terminando primero.

----------------------------------------------------------------

