import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np 
from simulation import simulate_projectile
from ai_advisor import get_optimization_suggestion
import utils

st.set_page_config(page_title="Simulador com IA", layout="wide")
st.title("🚀 Simulador de Projétil com Resistência do Ar")
st.markdown("Ajuste os parâmetros e veja a trajetória. Peça à IA para sugerir melhorias e maximizar o alcance.")

# Sidebar com controles
st.sidebar.header("Parâmetros")
v0 = st.sidebar.slider("Velocidade inicial (m/s)", min_value=10.0, max_value=200.0, value=50.0, step=1.0)
angle = st.sidebar.slider("Ângulo (graus)", min_value=0.0, max_value=90.0, value=45.0, step=1.0)
mass = st.sidebar.slider("Massa (kg)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
k = st.sidebar.slider("Coeficiente de arrasto (N·s/m)", min_value=0.0, max_value=2.0, value=0.1, step=0.01, format="%.3f")

# Simulação
t, x, y, vx, vy, alcance, tempo_voo = simulate_projectile(v0, angle, mass, k)

# Mostrar resultados em colunas
col1, col2, col3 = st.columns(3)
col1.metric("Alcance máximo", f"{alcance:.2f} m")
col2.metric("Tempo de voo", f"{tempo_voo:.2f} s")
col3.metric("Velocidade final", f"{np.sqrt(vx[-1]**2 + vy[-1]**2):.2f} m/s")

# Gráfico da trajetória com Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x, y=y,
    mode='lines+markers',
    marker=dict(size=4, color=t, colorscale='Viridis', showscale=True, colorbar=dict(title="Tempo (s)")),
    line=dict(color='lightgray', width=2),
    name='Trajetória'
))
fig.update_layout(
    title="Trajetória do Projétil",
    xaxis_title="Distância horizontal (m)",
    yaxis_title="Altura (m)",
    hovermode='closest',
    width=800,
    height=500
)
st.plotly_chart(fig, use_container_width=True)

# Tabela de dados (opcional)
if st.checkbox("Mostrar dados da simulação"):
    df = pd.DataFrame({
        "Tempo (s)": t,
        "x (m)": x,
        "y (m)": y,
        "vx (m/s)": vx,
        "vy (m/s)": vy
    })
    st.dataframe(df.style.format("{:.2f}"))

# Botão para consultar a IA
st.markdown("---")
if st.button("🤖 Sugerir Otimização (IA Local)"):
    with st.spinner("Consultando IA..."):
        current = {"v0": v0, "angle": angle, "mass": mass, "k": k}
        results = {
            "range": alcance,
            "flight_time": tempo_voo,
            "vx_final": vx[-1] if len(vx) > 0 else 0,
            "vy_final": vy[-1] if len(vy) > 0 else 0
        }
        sugestao = get_optimization_suggestion(current, results)
    st.info("💡 **Sugestão da IA:**\n" + sugestao)

st.markdown("---")
st.caption("Simulação numérica (Euler). Arrasto linear: F = -k·v. A IA utiliza modelo local (Hermes 3) via LM Studio.")

