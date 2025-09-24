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



# Intervalo de troca em milissegundos (ex: 30 segundos = 30000)
interval_ms = 30000

# Código HTML com JavaScript para trocar de aba automaticamente
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <script type="text/javascript">
        let pages = {pages};
        let index = 0;

        function updateIframe() {{
            let iframe = document.getElementById("powerbi-frame");
            iframe.src = "{base_url}&pageName=" + pages[index];
            index = (index + 1) % pages.length;
        }}

        window.onload = function() {{
            updateIframe();  // Carrega a primeira aba
            setInterval(updateIframe, {interval_ms});  // Troca a cada 30s
        }};
    </script>
</head>
<body>
    <iframe id="powerbi-frame" width="1000" height="700" frameborder="0" allowFullScreen="true"></iframe>
</body>
</html>
"""

# Renderiza o HTML no Streamlit
st.components.v1.html(html_code, height=750)