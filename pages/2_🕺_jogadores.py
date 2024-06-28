import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Player",
    page_icon="🏃‍♂️",
    layout = "wide"
)


df_data = st.session_state['data']

#filtrar dados por clubes e colocalo em uma caixa de seleção
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clube',clubes)

#filtrar o meu filtro de clubes por nome de atletas 
df_players = df_data[df_data['Club'] == club]
players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox('Jogadores',players)

#montando a tela 2 de cima para baixo 
player_stats = df_data[df_data["Name"] == player].iloc[0]

#comecando pela foto dele
st.image(player_stats["Photo"])
#Nome dele :
st.title(player_stats['Name'])
#colocando as informações na tela usando o markdown 
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

#colocando as informações em colunas 
col1, col2, col3 = st.columns(3)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100}") 
#formatando o peso para kilos e com 2 casas decimais
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
#colocando uma linha para separar 
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
#construindo a barrinha de peogresso
st.progress(int(player_stats['Overall']))


col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")



