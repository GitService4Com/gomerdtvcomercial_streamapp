import streamlit as st
import time

# Lista de URLs públicas do Power BI (uma para cada aba simulada)
power_bi_links = [
        "https://app.powerbi.com/view?r=eyJrIjoiMTFkOGU0YjYtZTdmMy00NmNmLTk0YmYtNDQ3MGYyMzVkZmUwIiwidCI6Ijk0MTc0NTRiLTRhYWMtNDY5MS04MWIyLTc3NmU3OWI5MzA0YiJ9&pageName=f624eba97bb38c6282d6",
		"https://app.powerbi.com/view?r=eyJrIjoiMGVjYzVjZjktMjAxYy00NzkxLTkxMDUtMmM1Y2VlZGQ4OTc1IiwidCI6Ijk0MTc0NTRiLTRhYWMtNDY5MS04MWIyLTc3NmU3OWI5MzA0YiJ9"
]

# Tempo entre trocas de aba (em segundos)
refresh_time = 30

# Posição atual (salva no estado da sessão)
if "page_index" not in st.session_state:
    st.session_state.page_index = 0
else:
    st.session_state.page_index = (st.session_state.page_index + 1) % len(power_bi_links)

# Mostra o iframe do Power BI
st.components.v1.iframe(power_bi_links[st.session_state.page_index], height=600)

# Aguarda e força recarregamento da página Streamlit
time.sleep(refresh_time)
st.experimental_rerun()