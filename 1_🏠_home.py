import streamlit as st
import webbrowser as wb
import pandas as pd 
from datetime import datetime
import time



#carregando o conjunto de dados em cache para  facilitar o acesso e e diminuir o custo computacional 
#usar o index_col = 0 para atribuir os indeces a uma unica coluna que começa em 0
if "data" not in st.session_state:
    df_data = pd.read_csv('C:/Users/nunop/Desktop/My_GitHub/streamlit_fifa_test/datasets/CLEAN_FIFA23_official_data.csv',index_col=0)
    #so usaremos dados de jogadorem com contratos validos até o ano em que rodar o codigo
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    # excluir jogadorem que não tem valores registrados 
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by = 'Overall',ascending=False)
    st.session_state['data'] = df_data


#implementando textos 
st.markdown('# FIFA2023 OFFICIAL DATASET !⚽')
#futuramente colocar meu perfil do linkedin
st.sidebar.markdown('Desenvolvido por [Nuno Henrique Albuquerque Pires], estudante de engenharia da universidade federal de alagos(UFAL).')

#criando o botão 
btn = st.button("Acesse os dados na web !")
if btn :
    time.sleep(1)
    wb.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

#blablabla explicando o conjunto de dados 
st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)

