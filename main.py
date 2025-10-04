import streamlit as st
import pandas
# ---- Título da página
st.header("Cálculo de Salário Médio da Empresa")
# --- campos de entrada de dados
salario_total = st.number_input(label="Salário Total da Empresa:", format="%2f")
trabalhador_total = st.number_input(label="Trabalhador Total da Empresa:", format="%0f")
# --- Colunas
if st.button(label="Calcular Salário Médio Da Empresa", use_container_width=True):
    if salario_total > 0:
        if trabalhador_total > 0:
            resultado = salario_total/trabalhador_total
            resultado = st.write(f"**{resultado:.2f}**")
        else:
            st.info("Informe Trabalhador Total da Empresa")
    else:
        st.info("Informe Salário Total da Empresa")






