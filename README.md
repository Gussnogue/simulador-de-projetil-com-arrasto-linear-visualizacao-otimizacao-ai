# 🚀 Simulador de Projétil com Otimização por IA Local

Simulador físico interativo que calcula a trajetória de um projétil com arrasto linear e utiliza um modelo de linguagem (Hermes 3) rodando localmente no LM Studio para sugerir parâmetros que maximizem o alcance.

---

## 🛠️ Stack Principal

| **Linguagem** | **Frameworks & Bibliotecas** | **IA Local** | **Visualização** |
|---------------|------------------------------|--------------|------------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) | ![LM Studio](https://img.shields.io/badge/LM_Studio-0A0A0A?style=flat-square&logo=ai&logoColor=white) ![Hermes 3](https://img.shields.io/badge/Hermes_3-3B-FFD700?style=flat-square) | ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white) |

---

## ✨ Funcionalidades

- 🔢 **Simulação numérica** (Euler) de projétil com resistência do ar proporcional à velocidade.
- 🎛️ **Controles interativos** no Streamlit (velocidade, ângulo, massa, arrasto).
- 📈 **Visualização dinâmica** com Plotly (trajetória colorida por tempo).
- 🤖 **IA local** que analisa os resultados e recomenda novos parâmetros com justificativa física.
- 📊 **Exportação de dados** em tabela para análise detalhada.

---

## 🚀 Como Executar

1. **Clone o repositório**
  ```bash
  git clone https://github.com/Gussnogue/simulador-projetil-ia-local.git
  cd simulador-projetil-ia-local
  ```

2. **Crie e ative um ambiente virtual**

  ```bash
  python -m venv venv
  source venv/bin/activate   # Linux/Mac
  venv\Scripts\activate      # Windows
  ```

3. **Instale as dependências**
   
  ```bash
  pip install -r requirements.txt
  ```

4. **Execute o app**
  ```bash
 streamlit run app.py
  ```

## 📁 Estrutura de Pastas
```bash
simulador-projetil-ia-local/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── app.py                 # Interface Streamlit
├── simulation.py          # Lógica de simulação (NumPy)
├── ai_advisor.py          # Comunicação com LM Studio
└── utils.py               # Funções auxiliares
```
## 📊 Exemplo de Uso
Ajuste os controles na barra lateral (velocidade inicial, ângulo, massa, arrasto).

Observe a trajetória no gráfico e as métricas (alcance, tempo de voo).

Clique em “🤖 Sugerir Otimização”, a IA local analisará os parâmetros atuais e recomendará novos valores para maximizar o alcance, explicando o raciocínio físico.

## 📄 Licença
MIT License – sinta-se à vontade para usar, modificar e contribuir.
