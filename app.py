import streamlit as st
import pandas as pd
import json

demo_json_data = json.loads(open("data/candidatos.json", "r").read())

st.write("Onde eles investem?")

st.write("Relação dos candidatos a prefeitos do RJ")

candidatosdf = pd.DataFrame([{"candidato": candidato["nomeCompleto"], "partido": candidato["partido"]["sigla"]} for candidato in demo_json_data["candidatos"]])

st.dataframe(candidatosdf)


