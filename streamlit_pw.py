import streamlit as st
import time

# Lista com as páginas do relatório (pageName de cada aba)
# Você precisa identificar os pageName corretos manualmente
pages = [
     	"f624eba97bb38c6282d6",
		"8e8e380329d0d0eed971",
		"0b8cc8b66f54517864d",
		"4c447571bff13334cf33",
		"6fde331acb98af207c25"
	
]

# Link base do seu relatório (sem pageName)
base_url = "https://app.powerbi.com/view?r=eyJrIjoiMTFkOGU0YjYtZTdmMy00NmNmLTk0YmYtNDQ3MGYyMzVkZmUwIiwidCI6Ijk0MTc0NTRiLTRhYWMtNDY5MS04MWIyLTc3NmU3OWI5MzA0YiJ9&embedImagePlaceholder=true"


# Tempo de troca (em segundos)
interval = 30

# Pega o tempo atual (em segundos desde a Epoch)
elapsed_time = int(time.time())

# Determina qual página mostrar com base no tempo
current_index = (elapsed_time // interval) % len(pages)
current_page = pages[current_index]

# Monta a URL com a página atual
url = f"{base_url}&pageName={current_page}"

# HTML com JavaScript para recarregar a página a cada 30 segundos
refresh_code = f"""
    <script>
        setTimeout(function(){{
            window.location.reload();
        }}, {interval * 1000}); // {interval} segundos
    </script>
"""

# Renderiza o HTML com auto-reload
st.components.v1.html(refresh_code, height=0)

# Exibe o Power BI em iframe
st.components.v1.iframe(url, width=1000, height=700)