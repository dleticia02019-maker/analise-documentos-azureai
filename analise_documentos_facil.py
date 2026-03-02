# analise_documentos_facil.py
"""
Versão fácil: Análise de documentos anti-fraude com Azure AI
Bootcamp DIO - Certificação IA-102
"""

from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# =====================
# INSIRA SUA CHAVE E ENDPOINT DO AZURE
# =====================
AZURE_KEY = "COLOQUE_SUA_CHAVE_AQUI"
AZURE_ENDPOINT = "COLOQUE_SEU_ENDPOINT_AQUI"

client = DocumentAnalysisClient(
    endpoint=AZURE_ENDPOINT,
    credential=AzureKeyCredential(AZURE_KEY)
)

# =====================
# FUNÇÃO PRONTA
# =====================
def analisar_documento_rapido(caminho_arquivo):
    with open(caminho_arquivo, "rb") as f:
        poller = client.begin_analyze_document("prebuilt-document", document=f)
        resultado = poller.result()
    
    print(f"\n--- Conteúdo do Documento ({caminho_arquivo}) ---")
    for i, pagina in enumerate(resultado.pages):
        print(f"\nPágina {i+1}:")
        for linha in pagina.lines:
            print(linha.content)
    return resultado

# =====================
# TESTE AUTOMÁTICO
# =====================
if __name__ == "__main__":
    # Coloque aqui um arquivo PDF ou imagem na mesma pasta do projeto
    arquivo_teste = "exemplo.pdf"
    
    try:
        analisar_documento_rapido(arquivo_teste)
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_teste}' não encontrado. Coloque um PDF ou imagem na mesma pasta.")
