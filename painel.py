import  os
import pandas as pd
import streamlit as st

st.title('Painel')

#criando 3 colunas
col1, col2, col3 = st.beta_columns(3)

#input de números
input_num = st.number_input(
       'Escreva um número entre 0 e 10',
       min_value = 0,
       max_value = 10,
       value = 0,
       step = 1
)
col2.inp
st.write('O número inputado foi: ', input_num)
#input de texto
input_txt = st.text_input(
      'Escreva uma palavra com até 5 letras',
      value = 'juiz',
      max_chars = 10
)
st.write('A palavra inputada foi: ', input_txt)
#################################################################

uploaded_file = st.file_uploader("Buscar Arquivo",type=['xlsx','xls','csv','txt'])

if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    #st.write(file_details)

    dados = pd.read_excel(uploaded_file)

pastas = os.listdir('C:\ArquivosSimAm') # dir is your directory path
quantidade_pasta = len(pastas)
st.info(str(quantidade_pasta) + " folder.")
st.warning(pastas)
data_load_state = st.text('Carregando dados...')
for pasta in pastas:

    files = next(os.walk('C:\ArquivosSimAm' + '\\' +pasta))[2]
    st.info(str(len(files)) + ' files' + ' na pasta ' + pasta)
    st.info(files)
data_load_state.text('Finalizado...')

# Carregando dados no grafico
#st.bar_chart(3,8)

import hiplot as hip
data = [{'dropout':0.1, 'lr': 0.001, 'Perdido': 10.0, 'Otimo': 'SGD'},
        {'dropout':0.15, 'lr': 0.01, 'Perdido': 3.5, 'Otimo': 'Adam'},
        {'dropout':0.3, 'lr': 0.1, 'Perdido': 4.5, 'Otimo': 'Adam'}]
hip.Experiment.from_iterable(data).display_st()


from streamlit_echarts import st_echarts

