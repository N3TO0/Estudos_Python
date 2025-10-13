import re

# texto_datas = "O relatório R$ 1200 final é de 15/03/2024. A reunião foi 01/01/2025, mas a data limite é 30-06-2023. Validar 12/12/2022."

# codigo_padrao= r'R\$ (\d+)'

# filtragem=re.findall(codigo_padrao, texto_datas)

# print(filtragem)

# :-----------------------------------------------------------------------

# artigo = """Entre em contato conosco em suporte@minhaempresa.com.br ou
# vendas@minhaempresa.org. Você pode me encontrar em
# meu.email@pessoal.com. Ou, se preferir, use um-email_invalido@.com
# ou somente texto sem email."""

# filtro= r'[\w\.-]+@[\w\.-]+\.[\w]{2,4}'

# email_filtros= re.findall(filtro,artigo)

# print(email_filtros)

# :-----------------------------------------------------------------------

texto_datas = "O relatório final é de 15/03/2024. A reunião foi 01/01/2025, mas a data limite é 30-06-2023. Validar 12/12/2022."

filtro = r'(\d{2})/(\d{2})/(\d{4})'

filtragem=re.findall(filtro,texto_datas)

print(filtragem)