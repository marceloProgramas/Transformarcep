import requests
import os
import json

def transform(endereco: str) -> list[float]:    
    cep = endereco.replace('-', '').strip()
    url = f"https://cep.awesomeapi.com.br/json/{cep}"

    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            return([float(dados["lat"]), float(dados['lng'])])
        elif response.status_code == 404:
            print("ERRO 404: Esse CEP não foi encontrado na base de dados da API.")
        else:
            print(f"Erro na API. Resposta do servidor:\n{response.text}")

    except requests.exceptions.RequestException as e:
        print(f"\nERRO DE CONEXÃO: Não foi possível alcançar o servidor.\nDetalhes: {e}")
    return[]