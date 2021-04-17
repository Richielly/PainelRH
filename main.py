import os
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time


st.title('Painel')

uploaded_file = st.file_uploader("Buscar Arquivo",type=['xlsx','xls','csv','txt'])


if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    #st.write(file_details)

    dados = pd.read_excel(uploaded_file)
            #st.write(dados.query("sistema" + "== " + selecao_coluna[0]))
            #st.write(dados.query("sistema" + "== " + "sistema"))

    if st.sidebar.checkbox('Por Sistema'):
           # Contando dados
        
        #grafico = dados.groupby(['Data inicio das férias']).sum()
        grafico = dados.groupby(by='sistema').size()
        st.info(type(grafico))
        st.info(grafico)
        st.bar_chart(grafico)
        st.line_chart(grafico)

#pastas = os.listdir('C:\ArquivosSimAm') # dir is your directory path
#quantidade_pasta = len(pastas)
#st.info(str(quantidade_pasta) + " folder.")
#st.warning(pastas)
#data_load_state = st.text('Carregando dados...')
#for pasta in pastas:
#    files = next(os.walk('C:\ArquivosSimAm' + '\\' +pasta))[2]
#    st.info(str(len(files)) + ' files' + ' na pasta ' + pasta)

#data_load_state.text('Finalizado...')

# CArregando dados
#teste = []
#while len(teste) < quantidade_pasta:
#    teste.append(0)
#teste.insert(9,12)

#st.bar_chart(teste)