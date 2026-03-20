import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

LM_STUDIO_URL = os.getenv("LM_STUDIO_URL", "http://localhost:1234/v1/chat/completions")
LM_MODEL = os.getenv("LM_MODEL", "hermes-3-llama-3.2-3b")

def get_optimization_suggestion(current_params, results):
    """
    Envia os parâmetros e resultados atuais para a IA, solicitando sugestões
    para maximizar o alcance.
    
    Parâmetros:
        current_params: dict com 'v0', 'angle', 'mass', 'k'
        results: dict com 'range', 'flight_time', 'vx_final', 'vy_final'
    
    Retorna:
        string com a sugestão da IA
    """
    prompt = f"""
    Você é um especialista em física e otimização de trajetórias.
    Analise os seguintes dados de simulação de um projétil com arrasto linear:

    Parâmetros atuais:
    - Velocidade inicial: {current_params['v0']:.1f} m/s
    - Ângulo: {current_params['angle']:.1f} graus
    - Massa: {current_params['mass']:.2f} kg
    - Coeficiente de arrasto: {current_params['k']:.3f} N·s/m

    Resultados:
    - Alcance: {results['range']:.2f} m
    - Tempo de voo: {results['flight_time']:.2f} s
    - Velocidade horizontal final: {results['vx_final']:.2f} m/s
    - Velocidade vertical final: {results['vy_final']:.2f} m/s

    Por favor, sugira novos valores para os parâmetros (especialmente ângulo e velocidade) que possam aumentar o alcance. Explique brevemente a lógica física por trás da sua sugestão. Responda em português, de forma direta e útil.
    """
    
    payload = {
        "model": LM_MODEL,
        "messages": [
            {"role": "system", "content": "Você é um engenheiro de simulação que fornece recomendações baseadas em física. Responda de forma clara e objetiva."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 400
    }
    
    try:
        response = requests.post(LM_STUDIO_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Erro ao consultar IA: {e}\nVerifique se o LM Studio está rodando e o modelo está carregado."
    
    