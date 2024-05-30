import streamlit as st
import pandas as pd
import plotly.express as px

#criação do design da pagina, o parametro wide usa toda a parte dos dados utilizados (o csv)
st.set_page_config(layout="wide")

#quais analises fazer; Faturamento mensal de:

#Faturamento por unidade
#tipo do produto mais vendidos
#contribuição por filial
#desempenho  das forma de pagamento
#como estão as  avaliações das filiais

df = pd.read_csv('supermarket_sales.csv',sep=';',decimal=',') #abrir o arquivo com pandas
df['Date'] = pd.to_datetime(df['Date']) #datime para data
df=df.sort_values(['Date']) #ordenando 
df['Month'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))#o x é todas as linhas da coluna Date
month = st.sidebar.selectbox('Mês',df['Month'].unique()) #sadebar significa barra lateral

#Filtrando informações

df_filtered = df[df['Month'] == month]

col1,col2 = st.columns(2)
col3,col4,col5 = st.columns(3)

fig_date = px.bar(df_filtered, x='Date',y='Total',color = 'City',title='Faturamento por dia')
col1.plotly_chart(fig_date,use_container_width=True)

fig_prod = px.bar(df_filtered, x='Date',y='Product line',color = 'City',title='Faturamento por tipo de produto',orientation='h')
col2.plotly_chart(fig_prod,use_container_width=True)

city_total = df_filtered.groupby('City')[['Total']].sum().reset_index()
fig_city = px.bar(city_total, x='City',y='Total',title='Faturamento por filial')
col3.plotly_chart(fig_city,use_container_width=True)

fig_pag = px.pie(df_filtered,values= 'Total',names='Payment', title='Faturamento por tipo de pagamento')
col4.plotly_chart(fig_pag,use_container_width=True)

city_total = df_filtered.groupby('City')[['Rating']].mean().reset_index()
fig_rat = px.bar(df_filtered, x= 'City',y='Rating',title='Avaliação')
col5.plotly_chart(fig_rat,use_container_width=True)
