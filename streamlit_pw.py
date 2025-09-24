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

# Intervalo de troca em milissegundos (30 segundos)
interval_ms = 30000

# Código HTML com JavaScript para trocar as páginas
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            margin: 0;
            padding: 0;
        }}
        iframe {{
            width: 100%;
            height: 100vh; /* usa toda a altura da tela visível */
            border: none;
        }}
    </style>
    <script type="text/javascript">
        let pages = {pages};
        let index = 0;

        function updateIframe() {{
            let iframe = document.getElementById("powerbi-frame");
            iframe.src = "{base_url}&pageName=" + pages[index];
            index = (index + 1) % pages.length;
        }}

        window.onload = function() {{
            updateIframe();
            setInterval(updateIframe, {interval_ms});
        }};
    </script>
</head>
<body>
    <iframe id="powerbi-frame" allowfullscreen="true"></iframe>
</body>
</html>
"""

# Exibe o HTML com altura dinâmica (viewport height)
st.components.v1.html(html_code, height=1500)  # você pode ajustar aqui se quiser mais espaço