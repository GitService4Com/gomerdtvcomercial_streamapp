import streamlit as st
import time

# Lista com as páginas do relatório (pageName de cada aba)
# Você precisa identificar os pageName corretos manualmente
pages = [
     "https://app.powerbi.com/view?r=eyJrIjoiMTFkOGU0YjYtZTdmMy00NmNmLTk0YmYtNDQ3MGYyMzVkZmUwIiwidCI6Ijk0MTc0NTRiLTRhYWMtNDY5MS04MWIyLTc3NmU3OWI5MzA0YiJ9&pageName=f624eba97bb38c6282d6",
		"https://app.powerbi.com/view?r=eyJrIjoiMTFkOGU0YjYtZTdmMy00NmNmLTk0YmYtNDQ3MGYyMzVkZmUwIiwidCI6Ijk0MTc0NTRiLTRhYWMtNDY5MS04MWIyLTc3NmU3OWI5MzA0YiJ9&pageName=8e8e380329d0d0eed971",
		"https://app.powerbi.com/view?r=eyJrIjoiMTFkOGU0YjYtZTdmMy00NmNmLTk0YmYtNDQ3MGYyMzVkZmUwIiwidCI6Ijk0MTc0NTRiLTRhYWMtNDY5MS04MWIyLTc3NmU3OWI5MzA0YiJ9&pageName=0b8cc8b66f54517864d",
		"https://app.powerbi.com/view?r=eyJrIjoiMTFkOGU0YjYtZTdmMy00NmNmLTk0YmYtNDQ3MGYyMzVkZmUwIiwidCI6Ijk0MTc0NTRiLTRhYWMtNDY5MS04MWIyLTc3NmU3OWI5MzA0YiJ9&pageName=4c447571bff13334cf33",
		"https://app.powerbi.com/view?r=eyJrIjoiMTFkOGU0YjYtZTdmMy00NmNmLTk0YmYtNDQ3MGYyMzVkZmUwIiwidCI6Ijk0MTc0NTRiLTRhYWMtNDY5MS04MWIyLTc3NmU3OWI5MzA0YiJ9&pageName=6fde331acb98af207c25"
	
]

# Link base do seu relatório (sem pageName)
base_url = "https://app.powerbi.com/view?r=eyJrIjoiMTFkOGU0YjYtZTdmMy00NmNmLTk0YmYtNDQ3MGYyMzVkZmUwIiwidCI6Ijk0MTc0NTRiLTRhYWMtNDY5MS04MWIyLTc3NmU3OWI5MzA0YiJ9&embedImagePlaceholder=true"

# Tempo de troca (em segundos)
interval = 30

# Pega o tempo atual (em segundos) desde o início da execução
elapsed_time = int(time.time())

# Determina qual página mostrar com base no tempo
current_index = (elapsed_time // interval) % len(pages)
current_page = pages[current_index]

# Monta a URL com a página atual
url = f"{base_url}&pageName={current_page}"

# Exibe o Power BI em iframe
st.components.v1.iframe(url, width=1000, height=700)
