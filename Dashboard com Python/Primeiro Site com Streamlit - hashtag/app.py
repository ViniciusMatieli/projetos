import streamlit as st
import pandas as pd

st.set_page_config(page_title='Meu site Streamlit')

with st.container():
    st.subheader('Meu primeiro site com o Streamlit') # Subtitulo
    st.title('Dashboard de Contratos') #titulo
    st.write('Informações sobre os contratos fechados pela Hash&Co ao longo de maio') #escrever algo como o h1
    #adicionando um link, onde tem os [] é para ser clicavèl
    st.write('Vc quer aprender programação ? blz, acesse [aqui](https://www.youtube.com/@HashtagProgramacao)')

#geralmente, com se carrega dados, precisa-se colocar em uma def de carregamento de dados
    
@st.cache_data #faz ficar salvo no cache do navegador do cliente os dados
def carregar_dados():
    tabela = pd.read_csv('resultados.csv')
    return tabela

with st.container():
    st.write('---')
    dados = carregar_dados()
    qtds_dias = st.selectbox('Selecione o periodo',['7D','15D','21D','30D'])
    num_dias = int(qtds_dias.replace('D',''))
    dados = dados[-num_dias:]
    st.area_chart(dados,x='Data',y='Contratos')