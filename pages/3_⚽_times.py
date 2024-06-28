import streamlit as st


st.set_page_config(
    page_title="Times",
    page_icon="⚽",
    layout = "wide"
)

#carregando dados na pagina 
df_data = st.session_state['data']

#filtrar dados por clubes e colocalo em uma caixa de seleção
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clube',clubes)

df_filtered = df_data[df_data["Club"] == club].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']


#dentro do meu dat frame vou colocar uma config em formato de discionario passando cada config de cada coluna
st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall" ,format="%d", min_value=0,max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", 
                                                    min_value=0, max_value=df_filtered["Wage(£)"].max()),
                 "Photo":st.column_config.ImageColumn(),
                 "Flag":st.column_config.ImageColumn(),

             })
