import streamlit as st
import time

# Lista de URLs públicas do Power BI (uma para cada aba simulada)
power_bi_links = [
        "https://app.powerbi.com/view?r=eyJrIjoiMTFkOGU0YjYtZTdmMy00NmNmLTk0YmYtNDQ3MGYyMzVkZmUwIiwidCI6Ijk0MTc0NTRiLTRhYWMtNDY5MS04MWIyLTc3NmU3OWI5MzA0YiJ9&pageName=f624eba97bb38c6282d6",
		"https://app.powerbi.com/view?r=eyJrIjoiMGVjYzVjZjktMjAxYy00NzkxLTkxMDUtMmM1Y2VlZGQ4OTc1IiwidCI6Ijk0MTc0NTRiLTRhYWMtNDY5MS04MWIyLTc3NmU3OWI5MzA0YiJ9"
]

# Tempo em segundos para trocar de aba
switch_interval = 30

# Armazena o tempo da última troca
if 'last_switch' not in st.session_state:
    st.session_state.last_switch = time.time()
    st.session_state.page_index = 0

# Verifica se passou o tempo de troca
if time.time() - st.session_state.last_switch > switch_interval:
    st.session_state.page_index = (st.session_state.page_index + 1) % len(power_bi_links)
    st.session_state.last_switch = time.time()

# Mostra o iframe com o relatório atual
st.components.v1.iframe(power_bi_links[st.session_state.page_index], height=600)

# Adiciona auto-refresh usando JavaScript
st.markdown(
    f"""
    <script>
        setTimeout(function(){{
            window.location.reload();
        }}, {switch_interval * 1000});
    </script>
    """,
    unsafe_allow_html=True
)