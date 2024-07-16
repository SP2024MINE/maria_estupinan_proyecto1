import streamlit as st
from sodapy import Socrata
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv

#load_dotenv('.env')
#TOKEN_APP = os.getenv("TOKEN_SODAPY")
#DATASET_ID = os.getenv("DATASET_ID")

st.title('Contratos')

st.write('Mi primer aplicativo para contratos')

#Selector de contratos, cargo datos de contratos desde sodapy y le permito al usuario escoger
#un contrato a visualizar

client = Socrata("www.datos.gov.co", None)


consulta = """SELECT id_contrato, nombre_entidad, departamento, descripcion_del_proceso, valor_del_contrato, fecha_de_firma
WHERE fecha_de_firma >='2024-01-01'
LIMIT 100000
"""

results = client.get("jbjy-vk9h", query = consulta)
results_df = pd.DataFrame.from_records(results)

contrato = st.selectbox("Seleccione un contrato", results_df['id_contrato'], placeholder='Seleccione un contrato único', disabled=False)

dataset_contrato= results_df[results_df['id_contrato'] == contrato].T

st.dataframe(dataset_contrato)

## Visualización de contratos por departamento

st.write('Visualización de contratos por departamento')


results_df['departamento'] = results_df['departamento'].str.upper()


### Usamos sns para visualizar los contratos por departamento

fig, ax = plt.subplots()
sns.countplot(data=results_df, x='departamento', ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)