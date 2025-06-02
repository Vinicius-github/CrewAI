from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama
import yaml
import os

llm = Ollama(model="mistral")

def carregar_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)
    
# === Carregar apenas o agente de análise de dados ===
agente_cfg = carregar_yaml("agents/analyze_data.yaml")
analyze_data = agente_cfg["analyze_data"]

print("Agente de Análise de Dados Carregado:", analyze_data)

