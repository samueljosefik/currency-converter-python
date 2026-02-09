import requests

def consultar_cotacoes():
    # URL da API de economia atualizada para 2026
    url = "https://economia.awesomeapi.com.br"
    
    try:
        response = requests.get(url)
        dados = response.json()
        
        # Pega os valores de compra (bid)
        dolar = dados['USDBRL']['bid']
        euro = dados['EURBRL']['bid']
        
        print("--- Cotacao Atualizada (2026) ---")
        print(f"Dolar: R$ {float(dolar):.2f}")
        print(f"Euro:  R$ {float(euro):.2f}")
        
    except Exception as e:
        print("Erro ao conectar com a API:", e)

if __name__ == "__main__":
    consultar_cotacoes()